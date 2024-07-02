# -*- coding: utf-8 -*-

from ..dataset import (
    acc_fact,
    char_fact,
    char_group_fact,
    client_fact,
)
import multibox.game.wow.wlk.preset.my_mode.api as my_mode

from ..act import target_leader_key_mapper_raid_tank
from ..paths import path_azerothcore_alliance_v2_hkn


class ModeFactory:
    @property
    def x5p_alliance_r_abcde(self):
        return my_mode.Mode(
            # client=client_fact.c_1920_1080,
            client=client_fact.c_1600_900,
            # client=client_fact.c_1176_664,
            active_chars=char_group_fact.r_1_to_5,
            login_chars=char_group_fact.r_1_to_5,
            target_leader_key_mapper=target_leader_key_mapper_raid_tank,
            script_path=path_azerothcore_alliance_v2_hkn,
            leader1=char_fact.ra_paladin_pve_protect,
            leader2=char_fact.ra_paladin_pve_protect,
            tank1=char_fact.ra_paladin_pve_protect,
            dr_pala1=char_fact.ra_paladin_pve_protect,
        )


dungeon_mode_fact = ModeFactory()
