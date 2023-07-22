# -*- coding: utf-8 -*-

import typing as T
from multibox.game.wow.wlk.api import Character, CharacterHelper

from ..character_factory import char_fact, char_group


class ActiveCharactersFactory:
    @property
    def x5p_s_abcde(self) -> T.List[Character]:
        return CharacterHelper.set_team_leader_and_tank(
            chars=[
                char_fact.sa_pve_protect_paladin.set_leader_12_and_tank_12().set_dr_pala_12(),
                char_fact.sb_pve_elemental_shaman,
                char_fact.sc_pve_elemental_shaman,
                char_fact.sd_pve_elemental_shaman,
                char_fact.se_pve_resto_shaman,
            ]
        )


dungeon_active_char_fact = ActiveCharactersFactory()
