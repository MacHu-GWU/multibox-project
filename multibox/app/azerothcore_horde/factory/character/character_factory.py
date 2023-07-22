# -*- coding: utf-8 -*-

import typing as T
from multibox.game.wow.wlk.api import (
    Talent as TL,
    Window,
    Character,
)
from multibox.app.azerothcore_horde.factory.account import acc_fact


class CharacterFactory:
    """
    枚举出所有账号下的所有角色的所有天赋. 每一个 @property 都代表: 一个账号下的一个角色的
    具体天赋配装. 同一个角色的双天赋需要创建两个 @property 函数.

    这样我们可以通过调用这些 可以被搜索定位, 名字人类可理解 的函数方便的创建游戏角色的实例.
    """

    @property
    def sa_pve_protect_paladin(self) -> Character:
        return Character(
            account=acc_fact.rab01,
            name="sa",
            talent=TL.paladin_pve_protect,
            window=Window.make(1),
            nth_char=1,
        )

    @property
    def sb_pve_elemental_shaman(self) -> Character:
        return Character(
            account=acc_fact.rab02,
            name="sb",
            talent=TL.shaman_pve_elemental,
            window=Window.make(2),
            nth_char=1,
        )

    @property
    def sc_pve_elemental_shaman(self) -> Character:
        return Character(
            account=acc_fact.rab03,
            name="sc",
            talent=TL.shaman_pve_elemental,
            window=Window.make(3),
            nth_char=1,
        )

    @property
    def sd_pve_elemental_shaman(self) -> Character:
        return Character(
            account=acc_fact.rab04,
            name="sd",
            talent=TL.shaman_pve_elemental,
            window=Window.make(4),
            nth_char=1,
        )

    @property
    def se_pve_resto_shaman(self) -> Character:
        return Character(
            account=acc_fact.rab05,
            name="se",
            talent=TL.shaman_pve_resto,
            window=Window.make(5),
            nth_char=1,
        )


char_fact = CharacterFactory()


class CharacterGroup:
    # horde
    @property
    def s_abcde(self) -> T.List[Character]:
        return [
            char_fact.sa_pve_protect_paladin,
            char_fact.sb_pve_elemental_shaman,
            char_fact.sc_pve_elemental_shaman,
            char_fact.sd_pve_elemental_shaman,
            char_fact.se_pve_resto_shaman,
        ]


char_group = CharacterGroup()
