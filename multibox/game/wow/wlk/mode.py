# -*- coding: utf-8 -*-

"""
Todo: doc string here
"""

import typing as T
from itertools import cycle
from functools import cached_property

import attrs
from attrs_mate import AttrsClass
from pathlib_mate import Path
from ordered_set import OrderedSet

import hotkeynet.api as hk

from ...wow.account import Account
from ...wow.window import Window

from .character import Character
from .talent import Talent as TL
from .talent import TalentCategory as TC
from .client import Client

from multibox.logger import logger
from multibox.utils.models import BaseSemiMutableModel


T_TARGET_KEY_MAPPING = T.Dict[str, hk.KeyMaker]


@attrs.define(eq=False, slots=False)
class Mode(BaseSemiMutableModel, AttrsClass):
    """
    Mode 是你最终选择要玩的游戏模式. 它相当于是一堆工厂类工厂函数的集合, 提供了一个 namespace
    来组织这些工厂函数. 一个 Mode 包括了:

    :param name: 给这个模式一个人类可读的名字.
    :param client: 客户端的相关设置.
    :param chars: 指定要使用哪些角色. :meth:`multibox.game.wow.wlk.dataset.Dataset.get_mode`
        方法能保证它们已经是根据 window label 排序好了的.
        这里面有的角色是 active char, 有的角色是 login char.
        请阅读 :ref:`wow-active-character` 了解什么是 active char.
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

    **Label Helper Methods**

    在多开的 HotkeyNet 定义中, 经常会出现根据天赋筛选出一部分角色的 window label
    然后让这些角色按下某技能按键的代码.

    下面凡是以 ``get_lbs_xyz`` 开头的方法都是一个工厂函数, 用于生成这种按照天赋筛选出的
    角色的 window label 集合. 调用时需要用 ``get_lbs_xyz()``. 因为这个集合是 mutable 的,
    每次调用这个方法都会生成一个新的集合, 以保证就算你对这个集合进行了修改, 也不会影响到其他集合,
    防止出现奇怪的 bug. 但这样做的的代价是牺牲一部分性能开销.

    下面凡是以 ``lbs_xyz`` 开头的都是一个 ``@cached_property``, 调用时不需要打括号.
    ``get_lbs_xyz`` 方法的返回值的一个内存中的缓存. 如果你确定 100% 你不会修改这个集合,
    那么你可以用这个方法以获得更好的性能.
    """

    name: T.Optional[str] = attrs.field(default=None)
    client: T.Optional[Client] = attrs.field(default=None)
    chars: OrderedSet[Character] = attrs.field(factory=OrderedSet)
    target_key_mapping: T_TARGET_KEY_MAPPING = attrs.field(factory=dict)
    script: hk.Script = attrs.field(factory=hk.Script)
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

    def _validate_dps(self):
        pass

    def _validate_healer(self):
        paladin_healer_talents = TC.paladin_healer.talents
        healer_talents = TC.healer.talents
        lb_tank1 = self.lb_tank1
        lb_tank2 = self.lb_tank2
        for char in self.active_chars:
            if char.talent in paladin_healer_talents:
                if char.is_raid_healer:  # pragma: no cover
                    raise ValueError(
                        f"在 {self.name!r} 模式下, 奶骑 {char.name!r} 不可以将 "
                        f"is_raid_healer 设为 True, 因为奶骑天生给 tank 道标, 随机刷团血, "
                        f"这个 flag 无需设置."
                    )
                err_msg = (
                    "在 {self.name!r} 模式下, 奶骑 {char.name!r} 不可以同时将 "
                    "is_tank_{i}_healer 和 is_tank_{i}_beacon_paladin 设为 True, "
                    "因为设定 is_tank_{i}_healer 表示它定点给 tank 刷血, 这和道标是冲突的."
                )
                if (
                    char.is_tank_1_healer and char.is_tank_1_beacon_paladin
                ):  # pragma: no cover
                    raise ValueError(err_msg.format(self=self, char=char, i=1))
                if (
                    char.is_tank_2_healer and char.is_tank_2_beacon_paladin
                ):  # pragma: no cover
                    raise ValueError(err_msg.format(self=self, char=char, i=2))
                if (
                    char.is_tank_1_beacon_paladin and char.is_tank_2_beacon_paladin
                ):  # pragma: no cover
                    raise ValueError(
                        f"在 {self.name!r} 模式下, 奶骑 {char.name!r} 不可以同时将 "
                        f"is_tank_1_beacon_paladin 和 is_tank_2_beacon_paladin 设为 True!"
                        f"这是矛盾的."
                    )

            if char.talent in healer_talents:
                if char.is_tank_1_healer and char.is_tank_2_healer:  # pragma: no cover
                    raise ValueError(
                        f"在 {self.name!r} 模式下, 治疗 {char.name!r} 不可以同时将 "
                        f"is_tank_1_healer 和 is_tank_2_healer 设为 True! 这是矛盾的."
                    )

                err_msg = (
                    "在 {self.name!r} 模式下, 治疗 {char.name!r} 不能是 {i} 号 "
                    "tank 的治疗或道标奶骑, 因为该模式下没有 tank {i}."
                    "请检查你的角色设定."
                )
                if (lb_tank1 is None) and (
                    char.is_tank_1_healer or char.is_tank_1_beacon_paladin
                ):
                    raise ValueError(err_msg.format(self=self, char=char, i=1))
                if (lb_tank2 is None) and (
                    char.is_tank_2_healer or char.is_tank_2_beacon_paladin
                ):
                    raise ValueError(err_msg.format(self=self, char=char, i=2))

    def _validate(self):
        self._validate_dps()
        self._validate_healer()

    def __attrs_post_init__(self):
        # 定位队伍中的关键人物
        # fmt: off
        self.leader1 = OrderedSet([char for char in self.active_chars if char.is_leader_1])
        self.leader2 = OrderedSet([char for char in self.active_chars if char.is_leader_2])
        self.tank1 = Character.find_xyz(chars=self.chars, field="is_tank_1", is_active=True)
        self.tank2 = Character.find_xyz(chars=self.chars, field="is_tank_2", is_active=True)
        self.dr_pala1 = Character.find_xyz(chars=self.chars, field="is_dr_pala_1", is_active=True)
        self.dr_pala2 = Character.find_xyz(chars=self.chars, field="is_dr_pala_2", is_active=True)
        # fmt: on

        self._validate()

        # 当创建 hotkeynet.api.Script 对象时, context 里是没有东西的, 我们需要用
        # 先调用 ``with Script()`` 的语法然后才能定义 Command, Hotkey, 这样很麻烦.
        # 所以我们手动将它设为 context 的顶层, 这样就可以直接定义 Command, Hotkey 了.
        hk.context.push(self.script)

    def get_active_chars(self) -> OrderedSet[Character]:
        """
        筛选出 active 的角色.
        """
        return OrderedSet([char for char in self.chars if char.is_active])

    @cached_property
    def active_chars(self) -> OrderedSet[Character]:
        """
        See :meth:`get_active_chars`.
        """
        return self.get_active_chars()

    def get_label_to_char_mapping(self) -> T.Dict[str, Character]:
        """
        生成一个 window label 到 Character 对象的映射. 方便之后根据 window label
        来查找 Character 对象.
        """
        return {char.window.label: char for char in self.chars}

    @cached_property
    def label_to_char_mapping(self) -> T.Dict[str, Character]:
        return self.get_label_to_char_mapping()

    def get_char_by_label(self, lb: str) -> Character:
        """
        根据 window label 查找 Character 对象.
        """
        return self.label_to_char_mapping[lb]

    def get_many_chars_by_labels(self, lbs: T.Iterable[str]) -> OrderedSet[Character]:
        """
        根据 window label 的集合查找 Character 对象的集合.
        """
        return OrderedSet([self.get_char_by_label(lb) for lb in lbs])

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

    @property
    def target_tank_1_key_maker(self) -> hk.KeyMaker:
        return self.target_key_mapping[self.lb_tank1]

    @property
    def target_tank_2_key_maker(self) -> hk.KeyMaker:
        return self.target_key_mapping[self.lb_tank2]

    # --------------------------------------------------------------------------
    # 在多开的 HotkeyNet 定义中, 经常会出现根据天赋筛选出一部分角色的 window label
    # 然后让这些角色按下某技能按键的代码. 下面凡是以 ``get_bs
    # --------------------------------------------------------------------------
    def get_lbs_all(self) -> OrderedSet[str]:
        """
        返回所有要进行游戏的人物角色所对应的游戏窗口的 label.

        在多开热键定义中, 常用于那些对所有角色生效的按键. 比如 1234, 前进后退等.
        """
        return OrderedSet([char.window.label for char in self.chars if char.is_active])

    @cached_property
    def lbs_all(self) -> OrderedSet[str]:
        """
        See :meth:`get_lbs_all`.
        """
        return self.get_lbs_all()

    def get_lbs_by_tl(self, tl: TL) -> OrderedSet[str]:
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

    def get_lbs_by_tc(self, tc: TC) -> OrderedSet[str]:
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

    def get_lbs_healer(self) -> OrderedSet[str]:
        return self.get_lbs_by_tc(TC.healer)

    @cached_property
    def lbs_healer(self) -> OrderedSet[str]:
        """
        See :meth:`get_lbs_healer`.
        """
        return self.get_lbs_healer()

    def get_lbs_druid_resto(self) -> OrderedSet[str]:
        return self.get_lbs_by_tc(TC.druid_resto)

    @cached_property
    def lbs_druid_resto(self) -> OrderedSet[str]:
        """
        See :meth:`get_lbs_druid_resto`.
        """
        return self.get_lbs_druid_resto()

    def get_lbs_shaman_resto(self) -> OrderedSet[str]:
        return self.get_lbs_by_tc(TC.shaman_resto)

    @cached_property
    def lbs_shaman_resto(self) -> OrderedSet[str]:
        """
        See :meth:`get_lbs_shaman_resto`.
        """
        return self.get_lbs_shaman_resto()

    def get_lbs_priest_holy(self) -> OrderedSet[str]:
        return self.get_lbs_by_tc(TC.priest_holy)

    @cached_property
    def lbs_priest_holy(self) -> OrderedSet[str]:
        """
        See :meth:`get_lbs_priest_holy`.
        """
        return self.get_lbs_priest_holy()

    def get_lbs_priest_disco(self) -> OrderedSet[str]:
        return self.get_lbs_by_tc(TC.priest_disco)

    @cached_property
    def lbs_priest_disco(self) -> OrderedSet[str]:
        """
        See :meth:`get_lbs_priest_disco`.
        """
        return self.get_lbs_priest_disco()

    def get_lbs_paladin_holy(self) -> OrderedSet[str]:
        return self.get_lbs_by_tc(TC.paladin_holy)

    @cached_property
    def lbs_paladin_holy(self) -> OrderedSet[str]:
        """
        See :meth:`get_lbs_paladin_holy`.
        """
        return self.get_lbs_paladin_holy()

    def get_lbs_paladin_holy_and_non_paladin_holy_healer(
        self,
    ) -> T.Tuple[OrderedSet[str], OrderedSet[str]]:
        """
        返回两个集合, 一个是所有的奶骑, 一个是所有的非奶骑治疗. 由于道标技能的存在, 奶骑治疗
        的逻辑往往跟其他治疗有很大不同.
        """
        lbs_healer = self.lbs_healer
        lbs_paladin_holy = self.lbs_paladin_holy
        lbs_non_paladin_holy_healer = lbs_healer.difference(lbs_paladin_holy)
        return lbs_paladin_holy, lbs_non_paladin_holy_healer

    @cached_property
    def lbs_paladin_holy_and_non_paladin_holy_healer(
        self,
    ) -> T.Tuple[OrderedSet[str], OrderedSet[str]]:
        """
        See :meth:`get_lbs_paladin_holy_and_non_paladin_holy_healer`.
        """
        return self.get_lbs_paladin_holy_and_non_paladin_holy_healer()

    def get_lbs_tank_healer(self) -> OrderedSet[str]:
        """
        返回所有的治疗的 label, 但是把更应该优先治疗 tank 的治疗职业放在集合末尾.
        这个集合常见于动态地给 tank 分配治疗. 这个集合里如果有人, 就优先把优先级最高的治疗
        用 set.pop() 的方式取出来分配给 tank.
        """
        lbs_healer = OrderedSet()
        lbs_healer.update(self.lbs_paladin_holy)
        lbs_healer.update(self.lbs_priest_disco)
        lbs_healer.update(self.lbs_priest_holy)
        lbs_healer.update(self.lbs_shaman_resto)
        lbs_healer.update(self.lbs_druid_resto)
        return lbs_healer

    @cached_property
    def lbs_tank_healer(self) -> OrderedSet[str]:
        """
        See :meth:`get_lbs_tank_healer`.
        """
        return self.get_lbs_tank_healer()

    def get_lbs_raid_healer(self) -> OrderedSet[str]:
        """
        返回所有的治疗的 label, 但是把更应该优先治疗 raid 的治疗职业放在集合末尾.
        这个集合常见于动态地给团队分配治疗. 这个集合里如果有人, 就优先把优先级最高的治疗
        用 set.pop() 的方式取出来刷团血.
        """
        lbs_healer = OrderedSet()
        lbs_healer.update(self.lbs_paladin_holy)
        lbs_healer.update(self.lbs_shaman_resto)
        lbs_healer.update(self.lbs_druid_resto)
        lbs_healer.update(self.lbs_priest_holy)
        lbs_healer.update(self.lbs_priest_disco)
        return lbs_healer

    @cached_property
    def lbs_raid_healer(self) -> OrderedSet[str]:
        """
        See :meth:`get_lbs_raid_healer`.
        """
        return self.get_lbs_raid_healer()

    def get_tank_pairs_cycle(self) -> T.Iterator[T.Tuple[str, hk.KeyMaker]]:
        """
        在给治疗分配任务时, 会遇到多出来的治疗平均分配给 tank 的情况. 这个方法返回一个
        在 tank 之间循环的迭代器, 并且返回 tank 的 label 以及对应的 KeyMaker 对象
        (用于点击选中这个 tank 角色的宏).

        Usage example::

            >>> mode = Mode(...)
            >>> tank_pairs_cycle = mode.get_tank_pairs_cycle()
            >>> lb_tank, key_maker = next(tank_pairs_cycle)
            >>> with hk.SendLabel(id="select_tank", to=[...]):
            ...    key_maker()
            ...    # put spell here
        """
        tank_pairs: T.List[T.Tuple[str, hk.KeyMaker]] = list()
        if self.lb_tank1:
            tank_pairs.append((self.lb_tank1, self.target_tank_1_key_maker))
        if self.lb_tank2:
            tank_pairs.append((self.lb_tank2, self.target_tank_2_key_maker))
        return cycle(tank_pairs)

    def build_send_label_by_tc(
        self,
        tc: TC,
        funcs: T.Iterable[T.Callable],
        id: str = "{talent}",
    ) -> T.Optional[hk.SendLabel]:
        """
        根据天赋组对角色进行筛选, 并生成 SendLabel 对象. 这个方法是为了简化代码而设计的.

        :param funcs: 一系列的函数, 用于构建在 send label 的 block 中的内容.
            比如连续按下多个按键.
        """
        lbs = self.get_lbs_by_tc(tc)
        if lbs:
            with hk.SendLabel(
                id=id.format(talent=tc.name),
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

    @logger.emoji_block(
        msg="Generate HotkeyNet Script",
        emoji="📝",
    )
    def dump(self, verbose: bool = False):  # pragma: no cover
        """
        Generate the hotkeynet script and write to file.
        """
        logger.info(f"mode: {self.name!r}")
        self.script_path.write_text(self.render(verbose=verbose))
