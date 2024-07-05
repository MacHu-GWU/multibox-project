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
    target_key_mapping = "target_key_mapping"
    mode = "mode"


class AccountTabColumnEnum(str, enum.Enum):
    account = "account"
    password = "password"


account_schema = {
    AccountTabColumnEnum.account.value: pl.String,
    AccountTabColumnEnum.password.value: pl.String,
}


class CharacterTabColumnEnum(str, enum.Enum):
    character = "character"
    account = "account"
    nth_char = "nth_char"


class BuildTabColumnEnum(str, enum.Enum):
    build = "build"
    suffix = "suffix"
    character = "character"
    spec = "spec"
    spec_simulator = "spec_simulator"


class BuildGroupTabColumnEnum(str, enum.Enum):
    build_group = "build_group"
    build = "build"
    window = "window"
    is_active = "is_active"
    is_leader_1 = "is_leader_1"
    leader_1_win = "leader_1_win"
    is_leader_2 = "is_leader_2"
    leader_2_win = "leader_2_win"
    is_tank_1 = "is_tank_1"
    is_tank_2 = "is_tank_2"
    is_dr_pala_1 = "is_dr_pala_1"
    is_dr_pala_2 = "is_dr_pala_2"


build_group_schema = {
    BuildGroupTabColumnEnum.build_group.value: pl.String,
    BuildGroupTabColumnEnum.build.value: pl.String,
    BuildGroupTabColumnEnum.window.value: pl.Int8,
    BuildGroupTabColumnEnum.is_active.value: pl.Int8,
    BuildGroupTabColumnEnum.is_leader_1.value: pl.Int8,
    BuildGroupTabColumnEnum.leader_1_win.value: pl.Int8,
    BuildGroupTabColumnEnum.is_leader_2.value: pl.Int8,
    BuildGroupTabColumnEnum.leader_2_win.value: pl.Int8,
    BuildGroupTabColumnEnum.is_tank_1.value: pl.Int8,
    BuildGroupTabColumnEnum.is_tank_2.value: pl.Int8,
    BuildGroupTabColumnEnum.is_dr_pala_1.value: pl.Int8,
    BuildGroupTabColumnEnum.is_dr_pala_2.value: pl.Int8,
}


class ClientTabColumnEnum(str, enum.Enum):
    client = "client"


class TargetKeyMappingTabColumnEnum(str, enum.Enum):
    mapping = "mapping"
    window = "window"
    keyboard = "keyboard"


class ModeTabColumnEnum(str, enum.Enum):
    mode = "mode"
    chars = "chars"
    target_key_mapping = "target_key_mapping"


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


def int_to_bool(
    df: pl.DataFrame,
    col: T.Union[str, T.List[str]],
) -> pl.DataFrame:
    """
    把表格中的某些列的整数转换成布尔值. 因为我们在 Google Sheet 中输入的时候,
    用 1 表示 True, 0 或者 BLANK 表示 False. 但在数据层面它们其实是 boolean 类型.
    """
    if isinstance(col, str):  # pragma: no cover
        cols = [col]
    else:
        cols = col
    return df.with_columns([pl.col(col).cast(pl.Boolean) for col in cols])


def find_not_unique(df: pl.DataFrame, col: str) -> pl.DataFrame:  # pragma: no cover
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
    target_key_mappings: T.Dict[str, T.Dict[int, str]] = dataclasses.field(default_factory=dict)
    modes: T.Dict[str, T.Dict[str, T.Any]] = dataclasses.field(default_factory=dict)
    # fmt: on

    @classmethod
    def from_excel(cls, path_excel: T.Union[str, Path]):
        """
        从 Excel 文件中读取数据, 并转换成内存中的数据.

        Sample excel: https://docs.google.com/spreadsheets/d/1gMWItF6I6e6iYZ7wBdqaN_ENjJu8XSc1-7RFmSmGnSc/edit?gid=132622854#gid=132622854
        """
        path_excel = Path(path_excel)
        # fmt: off
        df_account = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.account.value, schema_overrides=account_schema)
        df_character = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.character.value)
        df_build = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.build.value)
        df_build_group = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.build_group.value, schema_overrides=build_group_schema)
        df_target_leader = pl.read_excel(f"{path_excel}", sheet_name=SpreadSheetTabEnum.target_key_mapping.value)
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
        df_build_group = int_to_bool(
            df=df_build_group,
            col=[
                BuildGroupTabColumnEnum.is_active.value,
                BuildGroupTabColumnEnum.is_leader_1.value,
                BuildGroupTabColumnEnum.is_leader_2.value,
                BuildGroupTabColumnEnum.is_tank_1.value,
                BuildGroupTabColumnEnum.is_tank_2.value,
                BuildGroupTabColumnEnum.is_dr_pala_1.value,
                BuildGroupTabColumnEnum.is_dr_pala_2.value,
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

        def validate_uniqueness_in_sub_df(
            sub_df: pl.DataFrame,
            col: str,
            build_group: str,
        ):
            if sub_df[col].n_unique() != sub_df.shape[0]:  # pragma: no cover
                df_not_unique = find_not_unique(sub_df, col)
                print(df_not_unique)
                raise ValueError(
                    f"Found duplicated {col!r} in build group '{build_group}'"
                )

        def validate_at_most_one(
            sub_df: pl.DataFrame,
            col: str,
            build_group: str,
        ):
            if sub_df[col].is_not_null().sum() > 1:  # pragma: no cover
                raise ValueError(
                    f"Found multiple {col!r} in build group '{build_group}'"
                )

        build_group: str
        for (build_group,), sub_df in df_build_group_joined.group_by(
            BuildGroupTabColumnEnum.build_group.value, maintain_order=True
        ):
            validate_uniqueness_in_sub_df(
                sub_df=sub_df,
                col=BuildTabColumnEnum.build.value,
                build_group=build_group,
            )
            validate_uniqueness_in_sub_df(
                sub_df=sub_df,
                col=BuildGroupTabColumnEnum.window.value,
                build_group=build_group,
            )
            for col in [
                BuildGroupTabColumnEnum.is_tank_1.value,
                BuildGroupTabColumnEnum.is_tank_2.value,
                BuildGroupTabColumnEnum.is_dr_pala_1.value,
                BuildGroupTabColumnEnum.is_dr_pala_2.value,
            ]:
                validate_at_most_one(
                    sub_df=sub_df,
                    col=col,
                    build_group=build_group,
                )
            dct = {
                BuildGroupTabColumnEnum.build_group.value: build_group,
                "build_list": sub_df.sort(by="window").to_dicts(),
            }
            build_groups[build_group] = dct

        clients = {
            dct[ClientTabColumnEnum.client.value]: dct for dct in df_client.to_dicts()
        }

        target_key_mappings = {}
        setup: str
        for (setup,), sub_df in df_target_leader.group_by(
            TargetKeyMappingTabColumnEnum.mapping.value, maintain_order=True
        ):
            mapping = {
                dct[TargetKeyMappingTabColumnEnum.window.value]: dct[
                    TargetKeyMappingTabColumnEnum.keyboard.value
                ]
                for dct in sub_df.to_dicts()
            }
            target_key_mappings[setup] = mapping

        modes = {dct[ModeTabColumnEnum.mode.value]: dct for dct in df_mode.to_dicts()}

        return cls(
            accounts=accounts,
            builds=builds,
            build_groups=build_groups,
            clients=clients,
            target_key_mappings=target_key_mappings,
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
        # 从 build 表中拿核心数据, 从 build_group 中拿根具体玩法有关的数据
        chars = list()
        for build_dct in dct["build_list"]:
            old_char = self.get_character(
                build_dct[BuildGroupTabColumnEnum.build.value]
            )
            new_char = attrs.evolve(
                old_char,
                # fmt: off
                window=Window.new(build_dct[BuildGroupTabColumnEnum.window.value]),
                is_active=bool(build_dct[BuildGroupTabColumnEnum.is_active.value]),
                is_leader_1=bool(build_dct[BuildGroupTabColumnEnum.is_leader_1.value]),
                is_leader_2=bool(build_dct[BuildGroupTabColumnEnum.is_leader_2.value]),
                is_tank_1=bool(build_dct[BuildGroupTabColumnEnum.is_tank_1.value]),
                is_tank_2=bool(build_dct[BuildGroupTabColumnEnum.is_tank_2.value]),
                is_dr_pala_1=bool(build_dct[BuildGroupTabColumnEnum.is_dr_pala_1.value]),
                is_dr_pala_2=bool(build_dct[BuildGroupTabColumnEnum.is_dr_pala_2.value]),
                # fmt: on
            )
            chars.append(new_char)
        window_to_char_mapping: T.Dict[int, Character] = {
            char.window.index: char for char in chars
        }
        for build_dct in dct["build_list"]:
            char = window_to_char_mapping[
                build_dct[BuildGroupTabColumnEnum.window.value]
            ]

            leader_1_win = build_dct[BuildGroupTabColumnEnum.leader_1_win.value]
            if leader_1_win:
                char.leader_1 = window_to_char_mapping[leader_1_win]

            leader_2_win = build_dct[BuildGroupTabColumnEnum.leader_2_win.value]
            if leader_2_win:
                char.leader_2 = window_to_char_mapping[leader_2_win]

            is_tank_1 = build_dct[BuildGroupTabColumnEnum.is_tank_1.value]
            if is_tank_1:
                for other_char in chars:
                    if other_char.hash_key != char.hash_key:
                        other_char.tank1 = char

            is_tank_2 = build_dct[BuildGroupTabColumnEnum.is_tank_2.value]
            if is_tank_2:
                for other_char in chars:
                    if other_char.hash_key != char.hash_key:
                        other_char.tank2 = char

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
        chars = self.get_build_group(build_group=dct["chars"])
        setup = dct[ModeTabColumnEnum.target_key_mapping.value]
        mapping = self.target_key_mappings[setup]
        target_key_mapping = {
            Window.new(index).label: KeyMaker(key=keyboard)
            for index, keyboard in mapping.items()
        }
        mode = mode_class(
            name=dct[ModeTabColumnEnum.mode.value],
            client=self.get_client(dct["client"]),
            chars=chars,
            target_key_mapping=target_key_mapping,
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
        verbose: bool = False,
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
            if overwrite is False:  # pragma: no cover
                raise FileExistsError(f"{path_character_py} already exists.")
        path_character_py.write_text(content)
        if test:
            if verbose:  # pragma: no cover
                print("Test the generated script ...")
            with path_character_py.parent.temp_cwd():
                if verbose:  # pragma: no cover
                    subprocess.run(
                        [sys.executable, f"{path_character_py}"],
                        check=True,
                    )
                else:
                    subprocess.run(
                        [sys.executable, f"{path_character_py}"],
                        capture_output=True,
                        check=True,
                    )
            if verbose:  # pragma: no cover
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


def get_property_methods(factory) -> T.List[str]:
    """
    Find all the property methods in a factory class.

    .. code-block:: python

        class AccountFactory:
            @property
            def acc1(self):
                return Account(...)

            @property
            def acc2(self):
                return Account(...)

        acc_fact = AccountFactory()

        get_property_methods(acc_fact) # will return ["acc1", "acc2"]
    """
    return [key for key in factory.__class__.__dict__ if not key.startswith("_")]
