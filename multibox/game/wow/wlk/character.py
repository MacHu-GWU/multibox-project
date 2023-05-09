# -*- coding: utf-8 -*-

import typing as T

import attr
from attrs_mate import AttrsClass

from .. import api
from ..api import Window
from .talent import Talent as TL, TalentCategory as TC


@attr.s
class Character(api.Character):
    """
    在 WOTLK 版本下的代表着一个正在进行的游戏角色. 有着具体的天赋. 比如一个圣骑士角色有两套天赋.
    在天赋 1 下就算是一个 Character, 在天赋 2 下算是另一个 Character.

    除了 :class:`~multibox.game.wow.api.Character` 的属性外, 额外增加了以下属性:

    :param talent: 角色天赋.
    :param is_tank_1: 自己是否是 1 号坦克.
    :param is_tank_2: 自己是否是 2 号坦克.
    :param tank_1_window: 从自己的视角看 1 号坦克的窗口是哪个.
    :param tank_2_window: 从自己的视角看 2 号坦克的窗口是哪个.
    :param is_dr_pala_1: 自己是否是 1 号减伤圣骑士.
    :param is_dr_pala_2: 自己是否是 2 号减伤圣骑士.
    """

    talent: TL = AttrsClass.ib_generic(TL, nullable=True, default=None)
    is_tank_1: bool = AttrsClass.ib_bool(default=False)
    is_tank_2: bool = AttrsClass.ib_bool(default=False)
    tank_1_window: api.Window = AttrsClass.ib_generic(Window, nullable=True, default=None)
    tank_2_window: api.Window = AttrsClass.ib_generic(Window, nullable=True, default=None)
    is_dr_pala_1: bool = AttrsClass.ib_bool(default=False)
    is_dr_pala_2: bool = AttrsClass.ib_bool(default=False)

    def set_tank_1(self) -> "Character":
        self.is_tank_1 = True
        return self

    def set_not_tank_1(self) -> "Character":
        self.is_tank_1 = False
        return self

    def set_tank_2(self) -> "Character":
        self.is_tank_2 = True
        return self

    def set_not_tank_2(self) -> "Character":
        self.is_tank_2 = False
        return self

    def set_tank_1_window(self, window: api.Window) -> "Character":
        self.tank_1_window: Window = window
        return self

    def set_tank_2_window(self, window: api.Window) -> "Character":
        self.tank_2_window: Window = window
        return self

    def set_dr_pala_1(self) -> "Character":
        self.is_dr_pala_1 = True
        return self

    def set_dr_pala_2(self) -> "Character":
        self.is_dr_pala_2 = True
        return self

    def set_leader_1_tank_1(self) -> "Character":
        self.set_is_leader_1()
        self.set_tank_1()
        return self

    def set_leader_2_tank_2(self) -> "Character":
        self.set_is_leader_2()
        self.set_tank_2()
        return self

    def set_leader_12_and_tank_12(self) -> "Character":
        self.set_is_leader_1()
        self.set_tank_1()
        self.set_is_leader_2()
        self.set_tank_2()
        return self


class CharacterHelper(api.CharacterHelper):
    @classmethod
    def find_tank_1(cls, chars: T.Iterable["Character"]) -> T.Optional[Window]:
        return cls._find_key_char_window(chars, attribute="is_tank_1")

    @classmethod
    def find_tank_2(cls, chars: T.Iterable["Character"]) -> T.Optional[Window]:
        return cls._find_key_char_window(chars, attribute="is_tank_2")

    @classmethod
    def set_tank_1_window(
        cls,
        chars: T.Iterable["Character"],
        window: Window,
    ):
        """
        将所有角色的 1 号坦克窗口设为指定窗口.
        """
        cls._set_key_char_window(chars, "tank_1_window", window)

    @classmethod
    def set_tank_2_window(
        cls,
        chars: T.Iterable["Character"],
        window: Window,
    ):
        """
        将所有角色的 2 号坦克窗口设为指定窗口.
        """
        cls._set_key_char_window(chars, "tank_2_window", window)

    @classmethod
    def set_team_leader_and_tank(cls, chars: T.Iterable["Character"]):
        """
        在定义队伍时, 我们希望能简化操作. 只要在一堆角色中指定了谁是 1 号司机, 谁是 2 号司机,
        那么其他人就自动将他们的 leader_1_window, leader_2_window,
        tank_1_window, tank_2_window 设置好.
        """
        # find leader char window
        leader_1_window: T.Optional[Window] = cls.find_leader_1(chars)
        leader_2_window: T.Optional[Window] = cls.find_leader_2(chars)
        tank_1_window: T.Optional[Window] = cls.find_tank_1(chars)
        tank_2_window: T.Optional[Window] = cls.find_tank_2(chars)

        if leader_1_window is not None:
            cls.set_leader_1_window(chars, leader_1_window)
        else:
            raise ValueError("At least one char has to be the leader 1")

        if leader_2_window is not None:
            cls.set_leader_2_window(chars, leader_2_window)
        else:
            raise ValueError("At least one char has to be the leader 2")

        if tank_1_window is not None:
            cls.set_tank_1_window(chars, tank_1_window)

        if tank_2_window is not None:
            cls.set_tank_2_window(chars, tank_2_window)

        return chars

    @classmethod
    def filter_by_talent(
        cls,
        chars: T.Iterable["Character"],
        tl: TL,
    ) -> T.OrderedDict[str, "Character"]:
        """
        筛选出属于某个天赋的所有角色.

        例如你可以选出所有 PvE DK 血坦克 ``Talent.dk_pve_blood_tank`` 的角色.
        """
        return cls.deduplicate([char for char in chars if char.talent is tl])

    @classmethod
    def filter_by_talent_category(
        cls,
        chars: T.Iterable["Character"],
        tc: TC,
    ) -> T.OrderedDict[str, "Character"]:
        """
        筛选出天赋属于某个天赋类别的所有角色.

        例如你可以选出所有 PvE Tank 类别的角色. 实际上是先根据类别找出所有对应的天赋的集合,
        然后一一判断这个角色的天赋在不在集合中.
        """
        talent_set = tc.talents
        return cls.deduplicate([char for char in chars if char.talent in talent_set])
