# -*- coding: utf-8 -*-

import typing as T
from multibox.game.wow.wlk.api import (
    Character,
)

from .character_factory import char_fact


class LoginCharactersFactory:
    # horde
    @property
    def s_abcde(self) -> T.List[Character]:
        return [
            char_fact.sa_pve_protect_paladin.set_inactive(),
            char_fact.sb_pve_elemental_shaman.set_inactive(),
            char_fact.sc_pve_elemental_shaman.set_inactive(),
            char_fact.sd_pve_elemental_shaman.set_inactive(),
            char_fact.se_pve_resto_shaman.set_inactive(),
        ]


login_char_fact = LoginCharactersFactory()
