# -*- coding: utf-8 -*-

from multibox.app.azerothcore_alliance_v2.api import (
    dungeon_mode_fact,
    # raid_mode_fact,
)

# -----------------------------------------------------------------------------
# Azerothcore - Alliance - Dungeon
# -----------------------------------------------------------------------------
mode = dungeon_mode_fact.x5p_alliance_r_abcde

# -----------------------------------------------------------------------------
# Azerothcore - Alliance - Raid
# -----------------------------------------------------------------------------
# mode = raid_mode_fact.x10p_core_team
# mode = raid_mode_fact.x10p_naxx_abomination_4th_boss
# mode = raid_mode_fact.x25p_core_team
# mode = raid_mode_fact.x25p_core_team_ICC_1


# -----------------------------------------------------------------------------
# Don't Touch
# -----------------------------------------------------------------------------
# mode.dump(verbose=True)
mode.dump(verbose=False)
