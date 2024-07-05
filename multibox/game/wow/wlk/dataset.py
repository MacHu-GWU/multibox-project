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

import attrs
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


class BuildGroupTabColumnEnum(str, enum.Enum):
    build_group = "build_group"
    build = "build"
    window = "window"


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


def strip_whitespace(
    df: pl.DataFrame,
    col: T.Union[str, T.List[str]],
) -> pl.DataFrame:
    """
    把表格中的某些列的字符串两边的空格去掉.
    """
    if isinstance(col, str):
        cols = [col]
    else:
        cols = col
    return df.with_columns([pl.col(col).str.strip_chars() for col in cols])


def find_not_unique(df: pl.DataFrame, col: str) -> pl.DataFrame:
    df_not_unique = df[col].value_counts().filter(pl.col("count") > 1)
    return df_not_unique


def validate_uniqueness(df: pl.DataFrame, col: str, sheet: str):
    """
    确保一个表中的某一列是唯一的.
    """
    if df[col].n_unique() != df.shape[0]:  # pragma: no cover
        df_not_unique = find_not_unique(df, col)
        print(df_not_unique)
        raise ValueError(f"Found duplicated value in sheet {sheet!r}, column {col!r}")


def validate_inner_join(
    df_joined: pl.DataFrame,
    df: pl.DataFrame,
    on: str,
    sheet: str,
):
    """
    确保在 Join 两个表获取更多信息的时候, 没有出现因为左表 (fact 表) join 的 key 在右表中
    找不到而导致丢失数据的情况.
    """
    if df_joined.shape[0] != df.shape[0]:  # pragma: no cover
        df_not_valid = df.join(
            df_joined,
            on=on,
            how="anti",
        )
        print(df_not_valid)
        raise ValueError(f"Found {sheet!r} without a valid {on!r} in sheet {sheet!r}")


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

        # preprocess
        df_account = strip_whitespace(
            df=df_account,
            col=[
                AccountTabColumnEnum.account.value,
                AccountTabColumnEnum.password.value,
            ],
        )
        df_character = strip_whitespace(
            df=df_character,
            col=[
                CharacterTabColumnEnum.character.value,
                CharacterTabColumnEnum.account.value,
            ],
        )
        df_build = strip_whitespace(
            df=df_build,
            col=BuildTabColumnEnum.build.value,
        )
        df_build_group = strip_whitespace(
            df=df_build_group,
            col=[
                BuildGroupTabColumnEnum.build_group.value,
                BuildGroupTabColumnEnum.build.value,
            ],
        )
        df_client = strip_whitespace(
            df=df_client,
            col=ClientTabColumnEnum.client.value,
        )
        df_mode = strip_whitespace(
            df=df_mode,
            col=ModeTabColumnEnum.mode.value,
        )

        # validation
        validate_uniqueness(
            df=df_account,
            col=AccountTabColumnEnum.account.value,
            sheet=SpreadSheetTabEnum.account.value,
        )
        validate_uniqueness(
            df=df_character,
            col=CharacterTabColumnEnum.character.value,
            sheet=SpreadSheetTabEnum.character.value,
        )
        validate_uniqueness(
            df=df_build,
            col=BuildTabColumnEnum.build.value,
            sheet=SpreadSheetTabEnum.build.value,
        )
        validate_uniqueness(
            df=df_client,
            col=ClientTabColumnEnum.client.value,
            sheet=SpreadSheetTabEnum.client.value,
        )
        validate_uniqueness(
            df=df_mode,
            col=ModeTabColumnEnum.mode.value,
            sheet=SpreadSheetTabEnum.mode.value,
        )

        # data enrichment
        df_character_joined = df_character.join(
            df_account,
            on=AccountTabColumnEnum.account.value,
            how="inner",
            coalesce=True,
        )
        validate_inner_join(
            df_joined=df_character_joined,
            df=df_character,
            on=CharacterTabColumnEnum.account.value,
            sheet=SpreadSheetTabEnum.character.value,
        )

        df_build_joined = df_build.join(
            df_character_joined,
            on=BuildTabColumnEnum.character.value,
            how="inner",
            coalesce=True,
        )
        validate_inner_join(
            df_joined=df_build_joined,
            df=df_build,
            on=BuildTabColumnEnum.character.value,
            sheet=SpreadSheetTabEnum.build.value,
        )

        df_build_group_joined = df_build_group.join(
            df_build_joined,
            on=BuildGroupTabColumnEnum.build.value,
            how="inner",
            coalesce=True,
        )
        validate_inner_join(
            df_joined=df_build_group_joined,
            df=df_build_group,
            on=BuildGroupTabColumnEnum.build.value,
            sheet=SpreadSheetTabEnum.build_group.value,
        )

        # convert to in-memory dict
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
            if sub_df["build"].n_unique() != sub_df.shape[0]:  # pragma: no cover
                df_not_unique = find_not_unique(sub_df, BuildTabColumnEnum.build.value)
                print(df_not_unique)
                raise ValueError(
                    f"Found duplicated build in build group '{build_group}'"
                )
            dct = {
                BuildGroupTabColumnEnum.build_group.value: build_group,
                "build_list": [
                    {"build": sub_dct["build"], "window": sub_dct["window"]}
                    for sub_dct in sub_df.to_dicts()
                ],
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
            nth_char=dct[CharacterTabColumnEnum.nth_char.value],
            talent=Talent[dct[BuildTabColumnEnum.spec.value]],
        )

    def get_build_group(self, build_group: str) -> OrderedSet[Character]:
        dct = self.build_groups[build_group]
        chars = list()
        for build_dct in dct["build_list"]:
            char = self.get_character(build_dct["build"])
            new_char = attrs.evolve(char, window=Window.new(build_dct["window"]))
            chars.append(new_char)
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
            Window.new(index).label: KeyMaker(key=keyboard)
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
            "except ImportError: # pragma: no cover\n"
            "    from gen_dataset import ds\n"
        ),
        import_mode: str = (
            "try:\n"
            "    from .mode import Mode\n"
            "except ImportError: # pragma: no cover\n"
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
