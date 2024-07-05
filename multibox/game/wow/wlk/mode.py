# -*- coding: utf-8 -*-

"""
Todo: doc string here
"""

import typing as T
from functools import cached_property

import attrs
from attrs_mate import AttrsClass
from pathlib_mate import Path
from ordered_set import OrderedSet

import hotkeynet.api as hkn

from ...wow.account import Account
from ...wow.window import Window

from .character import Character
from .talent import Talent as TL
from .talent import TalentCategory as TC
from .client import Client

from multibox.utils.models import BaseSemiMutableModel


T_TARGET_KEY_MAPPING = T.Dict[str, hkn.KeyMaker]


@attrs.define(eq=False, slots=False)
class Mode(BaseSemiMutableModel, AttrsClass):
    """
    Mode 是你最终选择要玩的游戏模式. 它相当于是一堆工厂类工厂函数的集合, 提供了一个 namespace
    来组织这些工厂函数. 一个 Mode 包括了:

    :param name: 给这个模式一个人类可读的名字.
    :param client: 客户端的相关设置.
    :param active_chars: 指定要使用哪些角色进行游戏. 跟人物移动, 战斗相关的按键将会对这些角色生效.
        See :class:`~multibox.game.wow.character.Character` for more details.
    :param login_chars: 指定要登录哪些角色. 跟人物移动, 战斗相关的按键将 **不会** 对这些角色生效.
        只有跟登录账号相关的按键有效. 这些账号通常是用来蹲拍卖行, 倒东西, 聊天.
        最终要被登录的角色是 active_chars 和 login_chars 的合集. 如果一个 ``Character``
        对象同时出现在 ``active_chars`` 和 ``login_chars``, 那么 ``login_chars`` 中的
        ``Character`` 对象将会被忽略.
        See :class:`~multibox.game.wow.character.Character` for more details.
    :param target_key_mapping: 一个字典, key 是队长角色的 label,
        value 是对应的 KeyMaker 对象 (也就是 hotkeynet 的快捷键). 默认情况下非司机角色
        点击选择 leader 的宏时都是选择 1 号司机, 但是对于司机本人, 特别是多个司机的情况下,
        不同的情况下你的司机选择的目标可能会不同. 例如有的时候是 1, 2 号司机各自行动, 有的时候
        是 2 号司机跟随 1 号司机. 这个字典就是用来定义这种特殊情况的.
    :param script: 你的多开脚本对象.
    :param script_path: 最终的多开脚本文件路径.

    注, ``active_chars`` 和 ``login_chars`` 角色集合必须满足两个条件,
    character name 没有重复, window 没有重复, 且是按照 window 排序好的.
    :meth:`multibox.game.wow.wlk.dataset.Dataset.from_excel`
    """

    name: T.Optional[str] = attrs.field(default=None)
    client: T.Optional[Client] = attrs.field(default=None)
    chars: OrderedSet[Character] = attrs.field(factory=OrderedSet)
    target_key_mapping: T_TARGET_KEY_MAPPING = attrs.field(factory=dict)
    script: hkn.Script = attrs.field(factory=hkn.Script)
    script_path: T.Optional[Path] = attrs.field(default=None)
    leader1: OrderedSet[Character] = attrs.field(default=None)
    leader2: OrderedSet[Character] = attrs.field(default=None)
    tank1: T.Optional[Character] = attrs.field(default=None)
    tank2: T.Optional[Character] = attrs.field(default=None)
    dr_pala1: T.Optional[Character] = attrs.field(default=None)
    dr_pala2: T.Optional[Character] = attrs.field(default=None)

    @cached_property
    def hash_key(self) -> str:  # pragma: no cover
        return self.name

    @cached_property
    def sort_key(self) -> str:  # pragma: no cover
        return self.name

    def __attrs_post_init__(self):
        # 定位队伍中的关键人物
        # fmt: off
        active_chars = self.active_chars
        self.leader1 = OrderedSet([char for char in active_chars if char.is_leader_1])
        self.leader2 = OrderedSet([char for char in active_chars if char.is_leader_2])
        self.tank1 = Character.find_xyz(chars=self.chars, field="is_tank_1", is_active=True)
        self.tank2 = Character.find_xyz(chars=self.chars, field="is_tank_2", is_active=True)
        self.dr_pala1 = Character.find_xyz(chars=self.chars, field="is_dr_pala_1", is_active=True)
        self.dr_pala2 = Character.find_xyz(chars=self.chars, field="is_dr_pala_2", is_active=True)
        # fmt: on

        # 当创建 hotkeynet.api.Script 对象时, context 里是没有东西的, 我们需要用
        # 先调用 ``with Script()`` 的语法然后才能定义 Command, Hotkey, 这样很麻烦.
        # 所以我们手动将它设为 context 的顶层, 这样就可以直接定义 Command, Hotkey 了.
        hkn.context.push(self.script)

    @property
    def active_chars(self) -> OrderedSet[Character]:
        """
        筛选出 active 的角色.
        """
        return OrderedSet([char for char in self.chars if char.is_active])

    @property
    def login_window_and_account_pairs(self) -> T.List[T.Tuple[Window, Account]]:
        """
        根据 active_chars 和 login_chars 中的定义, 弄清楚每个游戏窗口 (1, 2, 3, ...)
        对应的是哪个游戏账号. 这样我们的自动登录脚本才能正常工作.

        这里有个特殊情况, 如果 active_chars 中有个 char 占用了 1 号窗口, login_chars 也有
        个 char 占用了 1 号窗口, 那么 active_chars 中的角色将会占用 1 号窗口 (优先级高)
        """
        window_and_account_pairs: T.List[T.Tuple[Window, Account]] = [
            (char.window, char.account) for char in self.chars
        ]
        return window_and_account_pairs

    # @property
    # def target_leader_1_key_maker(self) -> hkn.KeyMaker:
    #     return self.target_key_mapping[self.leader1.window.label]
    #
    # @property
    # def target_leader_2_key_maker(self) -> hkn.KeyMaker:
    #     return self.target_key_mapping[self.leader2.window.label]

    @property
    def target_tank_1_key_maker(self) -> hkn.KeyMaker:
        return self.target_key_mapping[self.lb_tank1]

    @property
    def target_tank_2_key_maker(self) -> hkn.KeyMaker:
        return self.target_key_mapping[self.lb_tank2]

    @property
    def lbs_all(self) -> OrderedSet[str]:
        """
        返回所有要进行游戏的人物角色所对应的游戏窗口的 label.

        在多开热键定义中, 常用于那些对所有角色生效的按键. 比如 1234, 前进后退等.
        """
        return OrderedSet([char.window.label for char in self.chars if char.is_active])

    def lbs_by_tl(self, tl: TL) -> OrderedSet[str]:
        """
        返回所有要进行游戏的人物角色中, 匹配某个 **具体天赋** 的角色所对应的游戏窗口的 label.
        例如防护骑士.

        在多开热键定义中, 常用于根据天赋筛选部分角色.
        """
        return OrderedSet(
            [
                char.window.label
                for char in Character.filter_by_talent(
                    chars=self.active_chars,
                    tl=tl,
                )
            ]
        )

    def lbs_by_tc(self, tc: TC) -> OrderedSet[str]:
        """
        返回所有要进行游戏的人物角色中, 匹配某个 **天赋分组** 的角色所对应的游戏窗口的 label.
        例如全部的近战物理 DPS.

        在多开热键定义中, 常用于根据天赋筛选部分角色.
        """
        return OrderedSet(
            [
                char.window.label
                for char in Character.filter_by_talent_category(
                    chars=self.active_chars,
                    tc=tc,
                )
            ]
        )

    # @property
    # def lb_leader1(self) -> T.Optional[str]:
    #     """
    #     获得 1 号 Leader 的 label, 可能有一个人或者没有 (如果只是登录不玩游戏的化就没有 leader).
    #     """
    #     if self.leader1 is not None:
    #         return self.leader1.window.label
    #     return None
    #
    # @property
    # def lb_leader2(self) -> T.Optional[str]:
    #     """
    #     获得 2 号 Leader 的 label, 可能有一个人或者没有.
    #     """
    #     if self.leader2 is not None:
    #         return self.leader2.window.label
    #     return None

    @property
    def lb_tank1(self) -> T.Optional[str]:
        """
        获得 1 号坦克的 label, 可能有一个人或者没有.
        """
        if self.tank1 is not None:
            return self.tank1.window.label
        return None

    @property
    def lb_tank2(self) -> T.Optional[str]:
        """
        获得 2 号坦克的 label, 可能有一个人或者没有.
        """
        if self.tank2 is not None:
            return self.tank2.window.label
        return None

    @property
    def lb_dr_pala1(self) -> T.Optional[str]:
        """
        获得 1 号开团队减伤骑士的 label, 可能有一个人或者没有.
        """
        if self.dr_pala1 is not None:
            return self.dr_pala1.window.label
        return None

    @property
    def lb_dr_pala2(self) -> T.Optional[str]:
        """
        获得 2 号开团队减伤骑士的 label, 可能有一个人或者没有.
        """
        if self.dr_pala2 is not None:
            return self.dr_pala2.window.label
        return None

    @property
    def lbs_leader1(self) -> OrderedSet[str]:
        """
        获得所有 leader1 角色的 Label 集合.
        """
        return OrderedSet([char.window.label for char in self.leader1])

    @property
    def lbs_leader2(self) -> OrderedSet[str]:
        """
        获得所有 leader1 角色的 Label 集合.
        """
        return OrderedSet([char.window.label for char in self.leader2])

    @property
    def lbs_leader(self) -> OrderedSet[str]:
        """
        获得所有 leader 角色的 Label 集合.
        """
        return self.lbs_leader1.union(self.lbs_leader2)

    @property
    def lbs_non_leader(self) -> OrderedSet[str]:
        return self.lbs_all.difference(self.lbs_leader)

    @property
    def lbs_tank(self) -> OrderedSet[str]:
        """
        获得所有 tank 角色的 Label 集合.
        """
        return OrderedSet(
            [lb for lb in [self.lb_tank1, self.lb_tank2] if lb is not None]
        )

    @property
    def lbs_non_tank(self) -> OrderedSet[str]:
        return OrderedSet(
            [
                char.window.label
                for char in self.active_chars
                if (char.is_tank_1 is False) and (char.is_tank_2 is False)
            ]
        )

    @property
    def lbs_healer(self) -> OrderedSet[str]:
        return self.lbs_by_tc(TC.healer)

    @property
    def lbs_druid_resto(self) -> OrderedSet[str]:
        return self.lbs_by_tc(TC.druid_resto)

    @property
    def lbs_shaman_resto(self) -> OrderedSet[str]:
        return self.lbs_by_tc(TC.shaman_resto)

    @property
    def lbs_priest_holy(self) -> OrderedSet[str]:
        return self.lbs_by_tc(TC.priest_holy)

    @property
    def lbs_priest_disco(self) -> OrderedSet[str]:
        return self.lbs_by_tc(TC.priest_disco)

    @property
    def lbs_paladin_holy(self) -> OrderedSet[str]:
        return self.lbs_by_tc(TC.paladin_holy)

    def build_send_label_by_tc(
        self,
        tc: TC,
        funcs: T.Iterable[T.Callable],
    ) -> T.Optional[hkn.SendLabel]:
        """
        根据天赋组对角色进行筛选, 并生成 SendLabel 对象. 这个方法是为了简化代码而设计的.

        :param funcs: 一系列的函数, 用于构建在 send label 的 block 中的内容.
            比如连续按下多个按键.
        """
        lbs = self.lbs_by_tc(tc)
        if lbs:
            with hkn.SendLabel(
                id=tc.name,
                to=list(lbs),
            ) as send_label:
                for func in funcs:
                    func()
                return send_label
        return None

    # --------------------------------------------------------------------------
    # 把 Mode 对象转换成 hotkey 脚本
    # --------------------------------------------------------------------------
    def render(self, verbose: bool = False) -> str:  # pragma: no cover
        """
        Render the hotkeynet script as string.
        """
        return self.script.render(verbose=verbose)

    def dump(self, verbose: bool = False):  # pragma: no cover
        """
        Generate the hotkeynet script and write to file.
        """
        self.script_path.write_text(self.render(verbose=verbose))
