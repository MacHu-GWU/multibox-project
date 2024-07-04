# -*- coding: utf-8 -*-

"""
Example Google Sheet: https://docs.google.com/spreadsheets/d/19m889kimzCkbfoc2Q2YOcwN5eYX3Gfja392ns2N6KBQ/edit?gid=180066775#gid=180066775
"""

import typing as T
import sys
import copy
import enum
import subprocess
import dataclasses

import jinja2
import polars as pl
from pathlib_mate import Path
from ordered_set import OrderedSet
from hotkeynet.api import KeyMaker

from ...wow.account import Account
from ...wow.window import Window
from .character import Character
from .talent import Talent
from .client import Client
from .mode import Mode


class SpreadSheetTabEnum(str, enum.Enum):
    account = "account"
    character = "character"
    build = "build"
    build_group = "build_group"
    client = "client"
    target_leader = "target_leader"
    mode = "mode"


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


class TargetLeaderTabColumnEnum(str, enum.Enum):
    setup = "setup"
    window = "window"
    keyboard = "keyboard"


class ModeTabColumnEnum(str, enum.Enum):
    mode = "mode"
    target_leader = "target_leader"


dir_home = Path.home()


@dataclasses.dataclass
class Dataset:
    # fmt: off
    accounts: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)
    characters: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)
    builds: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)
    build_groups: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)
    clients: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)
    target_leaders: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)
    modes: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)
    # fmt: on

    @classmethod
    def from_excel(cls, path_excel: T.Union[str, Path]):
        path_excel = Path(path_excel)
        # fmt: off
        df_account = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.account.value, schema_overrides={"account": pl.Utf8, "password": pl.Utf8})
        df_character = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.character.value)
        df_build = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.build.value)
        df_build_group = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.build_group.value)
        df_target_leader = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.target_leader.value)
        df_client = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.client.value)
        df_mode = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.mode.value)
        # fmt: on

        # validation
        if df_account["account"].n_unique() != df_account.shape[0]:  # pragma: no cover
            raise ValueError("Found duplicated account in sheet 'account'")

        if (
            df_character["character"].n_unique() != df_character.shape[0]
        ):  # pragma: no cover
            df_not_unique = (
                df_character[CharacterTabColumnEnum.character.value]
                .value_counts()
                .filter(pl.col("count") > 1)
            )
            print(df_not_unique)
            raise ValueError("Found duplicated character in sheet 'account'")
        df_character_joined = df_character.join(
            df_account,
            on=AccountTabColumnEnum.account.value,
            how="inner",
            coalesce=True,
        )
        if df_character_joined.shape[0] != df_character.shape[0]:  # pragma: no cover
            raise ValueError(
                "Found character without a valid account in sheet 'character'"
            )

        if (
            df_build[BuildTabColumnEnum.build.value].n_unique() != df_build.shape[0]
        ):  # pragma: no cover
            df_not_unique = (
                df_build[BuildTabColumnEnum.build.value]
                .value_counts()
                .filter(pl.col("count") > 1)
            )
            print(df_not_unique)
            raise ValueError("Found duplicated build in sheet 'build'")
        df_build_joined = df_build.join(
            df_character_joined,
            on=CharacterTabColumnEnum.character.value,
            how="inner",
            coalesce=True,
        )
        if df_build_joined.shape[0] != df_build.shape[0]:  # pragma: no cover
            raise ValueError("Found build without a valid character in sheet 'build'")

        df_build_group_joined = df_build_group.join(
            df_build_joined,
            on=BuildTabColumnEnum.build.value,
            how="inner",
            coalesce=True,
        )
        if (
            df_build_group_joined.shape[0] != df_build_group.shape[0]
        ):  # pragma: no cover
            raise ValueError(
                "Found build group without a valid build in sheet 'build_group'"
            )

        if df_client["client"].n_unique() != df_client.shape[0]:  # pragma: no cover
            df_not_unique = (
                df_client[ClientTabColumnEnum.client.value]
                .value_counts()
                .filter(pl.col("count") > 1)
            )
            print(df_not_unique)
            raise ValueError("Found duplicated client in sheet 'client'")

        if df_mode["mode"].n_unique() != df_mode.shape[0]:  # pragma: no cover
            df_not_unique = (
                df_mode[ModeTabColumnEnum.mode.value]
                .value_counts()
                .filter(pl.col("count") > 1)
            )
            print(df_not_unique)
            raise ValueError("Found duplicated mode in sheet 'mode'")

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

        clients = {
            dct[ClientTabColumnEnum.client.value]: dct for dct in df_client.to_dicts()
        }

        target_leaders = {}
        for (setup,), sub_df in df_target_leader.group_by(
            TargetLeaderTabColumnEnum.setup.value, maintain_order=True
        ):
            mapping = {
                dct[TargetLeaderTabColumnEnum.window.value]: dct[
                    TargetLeaderTabColumnEnum.keyboard.value
                ]
                for dct in sub_df.to_dicts()
            }
            target_leaders[setup] = mapping

        modes = {dct[ModeTabColumnEnum.mode.value]: dct for dct in df_mode.to_dicts()}

        return cls(
            accounts=accounts,
            builds=builds,
            build_groups=build_groups,
            clients=clients,
            target_leaders=target_leaders,
            modes=modes,
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
        dct = dict(dct)
        dct.pop(ClientTabColumnEnum.client.value)
        return Client(**dct)

    def get_mode(
        self,
        mode: str,
        mode_class: T.Type[Mode] = Mode,
    ) -> Mode:
        dct = self.modes[mode]

        def get_active_login_chars(type: str) -> OrderedSet[Character]:
            chars = OrderedSet()
            for i in range(1, 1 + 3):
                value = dct[f"{type}_chars_include{i}"]
                if value:
                    chars.update(self.get_build_group(value))
                value = dct[f"{type}_chars_exclude{i}"]
                if value:
                    chars.difference_update(self.get_build_group(value))
            return chars

        target_leader = dct[ModeTabColumnEnum.target_leader.value]
        mapping = self.target_leaders[target_leader]
        target_leader_key_mapper = {
            Window.make(index).label: KeyMaker(key=keyboard)
            for index, keyboard in mapping.items()
        }

        mode = mode_class(
            name=dct[ModeTabColumnEnum.mode.value],
            client=self.get_client(dct["client"]),
            active_chars=get_active_login_chars("active"),
            login_chars=get_active_login_chars("login"),
            target_leader_key_mapper=target_leader_key_mapper,
            leader1=self.get_character(dct["leader1"]) if dct["leader1"] else None,
            leader2=self.get_character(dct["leader2"]) if dct["leader2"] else None,
            tank1=self.get_character(dct["tank1"]) if dct["tank1"] else None,
            tank2=self.get_character(dct["tank2"]) if dct["tank2"] else None,
            dr_pala1=self.get_character(dct["dr_pala1"]) if dct["dr_pala1"] else None,
            dr_pala2=self.get_character(dct["dr_pala2"]) if dct["dr_pala2"] else None,
        )

        return mode

    def to_module(
        self,
        dir_module: Path,
        import_ds: str = (
            "try:\n"
            "    from .gen_dataset import ds\n"
            "except ImportError:\n"
            "    from gen_dataset import ds\n"
        ),
        import_mode: str = (
            "try:\n"
            "    from .mode import Mode\n"
            "except ImportError:\n"
            "    from multibox.game.wow.wlk.api import Mode\n"
        ),
        dataset_var_name: str = "ds",
        overwrite: bool = False,
        test: bool = False,
    ):
        path_character_py = dir_module / "dataset.py"
        path_tpl = Path.dir_here(__file__) / "dataset.py.jinja2"
        tpl = jinja2.Template(path_tpl.read_text())
        content = tpl.render(
            dataset=self,
            import_ds=import_ds,
            import_mode=import_mode,
            dataset_var_name=dataset_var_name,
        )
        if path_character_py.exists():
            if overwrite is False:
                raise FileExistsError(f"{path_character_py} already exists.")
        path_character_py.write_text(content)
        if test:
            print("Test the generated script ...")
            with path_character_py.parent.temp_cwd():
                subprocess.run([sys.executable, f"{path_character_py}"], check=True)
            print("✅Test passed.")

    @classmethod
    def locate_excel(
        cls,
        prefix: str,
        dir: Path = dir_home.joinpath("Downloads"),
    ) -> Path:
        """
        Locate the excel file in the given directory. Usually it is your
        ``${HOME}/Downloads`` directory.

        这个函数可以方便地找到你刚从 Google Sheet 上下载下来的 excel 文件.
        """
        lst = list(
            Path.sort_by_ctime(
                [
                    path
                    for path in dir.select_by_ext(".xlsx")
                    if path.basename.startswith(prefix)
                ]
            )
        )
        if lst:
            return lst[-1]  # use the latest one
        else:  # pragma: no cover
            raise FileNotFoundError(
                f"Cannot find any excel file start with '{prefix}' in {dir}"
            )
