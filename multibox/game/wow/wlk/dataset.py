# -*- coding: utf-8 -*-

"""
Example Google Sheet: https://docs.google.com/spreadsheets/d/19m889kimzCkbfoc2Q2YOcwN5eYX3Gfja392ns2N6KBQ/edit?gid=180066775#gid=180066775
"""

import typing as T
import enum
import json
import dataclasses

import jinja2
import polars as pl
from pathlib_mate import Path
from ordered_set import OrderedSet


class SpreadSheetTabEnum(str, enum.Enum):
    account = "account"
    character = "character"
    build = "build"
    build_group = "build_group"


@dataclasses.dataclass
class Account:
    account: str = dataclasses.field()
    password: str = dataclasses.field()


@dataclasses.dataclass
class Character:
    character: str = dataclasses.field()
    account: str = dataclasses.field()
    nth_char: int = dataclasses.field()

    account_obj: Account = dataclasses.field()


@dataclasses.dataclass
class Build:
    build: str = dataclasses.field()
    character: str = dataclasses.field()
    spec: str = dataclasses.field()
    window: int = dataclasses.field()

    character_obj: Character = dataclasses.field()


@dataclasses.dataclass
class BuildGroup:
    build_group: str = dataclasses.field()
    build_list: T.List[Build] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Dataset:
    accounts: T.List[Account] = dataclasses.field()
    characters: T.List[Character] = dataclasses.field()
    builds: T.List[Build] = dataclasses.field()
    build_groups: T.List[BuildGroup] = dataclasses.field()

    @classmethod
    def from_excel(cls, path_excel: T.Union[str, Path]):
        path_excel = Path(path_excel)
        # fmt: off
        df_account = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.account.value, schema_overrides={"account": pl.Utf8, "password": pl.Utf8})
        df_character = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.character.value)
        df_build = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.build.value)
        df_build_group = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.build_group.value)
        # fmt: on

        # validation
        if df_account["account"].n_unique() != df_account.shape[0]:
            raise ValueError("Found duplicated account in sheet 'account'")

        if (
            df_character.join(
                df_account,
                on="account",
                how="inner",
                coalesce=True,
            ).shape[0]
            != df_character.shape[0]
        ):
            raise ValueError(
                "Found character without a valid account in sheet 'character'"
            )

        if (
            df_build.join(
                df_character,
                on="character",
                how="inner",
                coalesce=True,
            ).shape[0]
            != df_build.shape[0]
        ):
            raise ValueError("Found build without a valid character in sheet 'build'")

        if (
            df_build_group.join(
                df_build,
                on="build",
                how="inner",
                coalesce=True,
            ).shape[0]
            != df_build_group.shape[0]
        ):
            raise ValueError(
                "Found build group without a valid build in sheet 'build_group'"
            )

        # convert
        accounts = [Account(**dct) for dct in df_account.to_dicts()]
        _accounts_mapping = {acc.account: acc for acc in accounts}
        characters = [
            Character(**dct, account_obj=_accounts_mapping[dct["account"]])
            for dct in df_character.to_dicts()
        ]
        _characters_mapping = {char.character: char for char in characters}
        builds = [
            Build(**dct, character_obj=_characters_mapping[dct["character"]])
            for dct in df_build.to_dicts()
        ]
        _builds_mapping = {b.build: b for b in builds}
        build_groups = [
            BuildGroup(
                build_group=name,
                build_list=[_builds_mapping[dct["build"]] for dct in sub_df.to_dicts()],
            )
            for (name,), sub_df in df_build_group.group_by(
                "build_group", maintain_order=True
            )
        ]

        return cls(
            accounts=accounts,
            characters=characters,
            builds=builds,
            build_groups=build_groups,
        )

    def to_module(
        self,
        dir_module: Path,
        overwrite: bool = False,
    ):
        path_accounts_json = dir_module / "accounts.json"
        acc_data = {acc.account: acc.password for acc in self.accounts}
        if path_accounts_json.exists():
            if overwrite is False:
                raise FileExistsError(f"{path_accounts_json} already exists.")
        path_accounts_json.write_text(json.dumps(acc_data, indent=4))

        path_character_py = dir_module / "dataset.py"
        path_tpl = Path.dir_here(__file__) / "dataset.py.jinja2"
        tpl = jinja2.Template(path_tpl.read_text())
        content = tpl.render(dataset=self)
        if path_character_py.exists():
            if overwrite is False:
                raise FileExistsError(f"{path_character_py} already exists.")
        path_character_py.write_text(content)
