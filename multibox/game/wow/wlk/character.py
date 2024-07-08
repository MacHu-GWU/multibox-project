# -*- coding: utf-8 -*-

import typing as T

import attrs
from attrs_mate import AttrsClass
from ordered_set import OrderedSet

import multibox.game.wow.api as wow
from .talent import Talent as TL, TalentCategory as TC

Window = wow.Window


@attrs.define(eq=False, slots=False)
class Character(wow.Character):
    """
    这个类扩展了 :class:`multibox.game.wow.character.Character` 这个对所有版本通用的类.
    用于表示一个在 WOTLK 版本下的代表着一个正在进行的游戏角色. 有着具体的天赋. 比如一个圣骑士
    角色有两套天赋. 在天赋 1 下就算是一个 Character, 在天赋 2 下算是另一个 Character.

    除了 :class:`~multibox.game.wow.character.Character` 的属性外, 额外增加了以下属性:

    :param talent: 角色的天赋.
    :param is_tank_1: 自己是否是 1 号坦克.
    :param is_tank_2: 自己是否是 2 号坦克.
    :param tank_1: 从自己的视角看 1 号坦克是哪个.
    :param tank_2: 从自己的视角看 2 号坦克是哪个.
    :param is_dr_pala_1: 自己是否是 1 号减伤圣骑士.
    :param is_dr_pala_2: 自己是否是 2 号减伤圣骑士.

    **Why do I need these attribute?**

    早期时 Character 并没有这些属性,


    """

    # fmt: off
    talent: TL = AttrsClass.ib_generic(TL, nullable=True, default=None)
    is_tank_1: bool = AttrsClass.ib_bool(default=False)
    is_tank_2: bool = AttrsClass.ib_bool(default=False)
    tank_1: T.Optional["Character"] = attrs.field(default=None)
    tank_2: T.Optional["Character"] = attrs.field(default=None)
    is_dr_pala_1: bool = AttrsClass.ib_bool(default=False)
    is_dr_pala_2: bool = AttrsClass.ib_bool(default=False)
    # 下面的属性是鸟德专用的
    is_typhoon_druid_1: bool = AttrsClass.ib_bool(default=False)
    is_typhoon_druid_2: bool = AttrsClass.ib_bool(default=False)
    # 下面的属性是治疗职业专用的
    is_tank_1_healer: bool = AttrsClass.ib_bool(default=False)
    is_tank_2_healer: bool = AttrsClass.ib_bool(default=False)
    is_raid_healer: bool = AttrsClass.ib_bool(default=False)
    is_tank_1_beacon_paladin: bool = AttrsClass.ib_bool(default=False)
    is_tank_2_beacon_paladin: bool = AttrsClass.ib_bool(default=False)
    # fmt: on

    @classmethod
    def filter_by_talent(
        cls,
        chars: T.Iterable["Character"],
        tl: TL,
    ) -> OrderedSet["T_CHARACTER"]:
        """
        筛选出属于某个天赋的所有角色.

        例如你可以选出所有 PvE DK 血坦克 ``Talent.dk_pve_blood_tank`` 的角色.
        """
        return OrderedSet([char for char in chars if char.talent is tl])

    @classmethod
    def filter_by_talent_category(
        cls,
        chars: T.Iterable["Character"],
        tc: TC,
    ) -> OrderedSet["T_CHARACTER"]:
        """
        筛选出天赋属于某个天赋类别的所有角色.

        例如你可以选出所有 PvE Tank 类别的角色. 实际上是先根据类别找出所有对应的天赋的集合,
        然后一一判断这个角色的天赋在不在集合中.
        """
        talent_set = tc.talents
        return OrderedSet([char for char in chars if char.talent in talent_set])


T_CHARACTER = T.TypeVar("T_CHARACTER", bound=Character)
