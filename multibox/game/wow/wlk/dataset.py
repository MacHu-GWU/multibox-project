# -*- coding: utf-8 -*-

"""
Example Google Sheet: https://docs.google.com/spreadsheets/d/19m889kimzCkbfoc2Q2YOcwN5eYX3Gfja392ns2N6KBQ/edit?gid=180066775#gid=180066775
"""

import typing as T
import copy
import enum
import json
import dataclasses

import jinja2
import polars as pl
from pathlib_mate import Path
from ordered_set import OrderedSet

from ...wow.account import Account
from ...wow.window import Window
from .character import Character
from .talent import Talent
from .client import Client


class SpreadSheetTabEnum(str, enum.Enum):
    account = "account"
    character = "character"
    build = "build"
    build_group = "build_group"
    client = "client"


class AccountTabColumnEnum(str, enum.Enum):
    account = "account"
    password = "password"


class CharacterTabColumnEnum(str, enum.Enum):
    character = "character"
    account = "account"
    nth_char = "nth_char"


class BuildTabColumnEnum(str, enum.Enum):
    build = "build"
    character = "character"
    spec = "spec"
    window = "window"


class BuildGroupTabColumnEnum(str, enum.Enum):
    build_group = "build_group"
    build = "build"


class ClientTabColumnEnum(str, enum.Enum):
    client = "client"


@dataclasses.dataclass
class Dataset:
    accounts: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)
    characters: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(
        default_factory=dict
    )
    builds: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)
    build_groups: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(
        default_factory=dict
    )
    clients: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_excel(cls, path_excel: T.Union[str, Path]):
        path_excel = Path(path_excel)
        # fmt: off
        df_account = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.account.value, schema_overrides={"account": pl.Utf8, "password": pl.Utf8})
        df_character = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.character.value)
        df_build = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.build.value)
        df_build_group = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.build_group.value)
        df_client = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.client.value)
        # fmt: on

        # validation
        if df_account["account"].n_unique() != df_account.shape[0]:
            raise ValueError("Found duplicated account in sheet 'account'")

        if df_character["character"].n_unique() != df_character.shape[0]:
            raise ValueError("Found duplicated character in sheet 'account'")
        df_character_joined = df_character.join(
            df_account,
            on=AccountTabColumnEnum.account.value,
            how="inner",
            coalesce=True,
        )
        if df_character_joined.shape[0] != df_character.shape[0]:
            raise ValueError(
                "Found character without a valid account in sheet 'character'"
            )

        if df_build[BuildTabColumnEnum.build.value].n_unique() != df_build.shape[0]:
            raise ValueError("Found duplicated build in sheet 'account'")
        df_build_joined = df_build.join(
            df_character_joined,
            on=CharacterTabColumnEnum.character.value,
            how="inner",
            coalesce=True,
        )
        if df_build_joined.shape[0] != df_build.shape[0]:
            raise ValueError("Found build without a valid character in sheet 'build'")

        df_build_group_joined = df_build_group.join(
            df_build_joined,
            on=BuildTabColumnEnum.build.value,
            how="inner",
            coalesce=True,
        )
        if df_build_group_joined.shape[0] != df_build_group.shape[0]:
            raise ValueError(
                "Found build group without a valid build in sheet 'build_group'"
            )

        # convert
        accounts = {
            dct[AccountTabColumnEnum.account.value]: dct
            for dct in df_account.to_dicts()
        }
        builds = {
            dct[BuildTabColumnEnum.build.value]: dct
            for dct in df_build_joined.to_dicts()
        }

        build_groups = {}
        for (build_group,), sub_df in df_build_group_joined.group_by(
            BuildGroupTabColumnEnum.build_group.value, maintain_order=True
        ):
            dct = {
                BuildGroupTabColumnEnum.build_group.value: build_group,
                "build_list": list(sub_df[BuildGroupTabColumnEnum.build.value]),
            }
            build_groups[build_group] = dct

        headers = list(df_client.columns)
        headers.remove(ClientTabColumnEnum.client.value)
        clients = {header: dict() for header in headers}
        for dct in df_client.to_dicts():
            attr = dct[ClientTabColumnEnum.client.value]
            for header in headers:
                try:
                    value = int(dct[header])
                except:
                    value = dct[header]
                clients[header][attr] = value

        return cls(
            accounts=accounts,
            builds=builds,
            build_groups=build_groups,
            clients=clients,
        )

    def get_account(self, account: str) -> Account:
        dct = copy.copy(self.accounts[account])
        return Account(
            username=dct[AccountTabColumnEnum.account.value],
            password=dct[AccountTabColumnEnum.password.value],
        )

    def get_character(self, build: str) -> Character:
        dct = self.builds[build]
        return Character(
            account=self.get_account(dct[AccountTabColumnEnum.account.value]),
            name=dct[CharacterTabColumnEnum.character.value],
            window=Window.make(dct[BuildTabColumnEnum.window.value]),
            nth_char=dct[CharacterTabColumnEnum.nth_char.value],
            talent=Talent[dct[BuildTabColumnEnum.spec.value]],
        )

    def get_build_group(self, build_group: str) -> OrderedSet[Character]:
        dct = self.build_groups[build_group]
        chars = list()
        for build in dct["build_list"]:
            chars.append(self.get_character(build))
        return OrderedSet(chars)

    def get_client(self, client: str) -> Client:
        dct = self.clients[client]
        return Client(**dct)

    def to_module(
        self,
        dir_module: Path,
        import_line: str = "from .gen_dataset import ds",
        dataset_var_name: str = "ds",
        overwrite: bool = False,
    ):
        path_character_py = dir_module / "dataset.py"
        path_tpl = Path.dir_here(__file__) / "dataset.py.jinja2"
        tpl = jinja2.Template(path_tpl.read_text())
        content = tpl.render(
            dataset=self,
            import_line=import_line,
            dataset_var_name=dataset_var_name,
        )
        if path_character_py.exists():
            if overwrite is False:
                raise FileExistsError(f"{path_character_py} already exists.")
        path_character_py.write_text(content)
