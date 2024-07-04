# -*- coding: utf-8 -*-

from multibox.app.acore.dataset import mode_fact

# -----------------------------------------------------------------------------
# Azerothcore - Alliance - Dungeon
# -----------------------------------------------------------------------------
# mode = mode_fact.alliance_r_abcde_solo_dungeon

# -----------------------------------------------------------------------------
# Azerothcore - Alliance - Raid
# -----------------------------------------------------------------------------
# mode = mode_fact.alliance_r_abcdefghij_solo_raid
# mode = raid_mode_fact.x10p_core_team
# mode = raid_mode_fact.x10p_naxx_abomination_4th_boss
# mode = raid_mode_fact.x25p_core_team
# mode = raid_mode_fact.x25p_core_team_ICC_1

# -----------------------------------------------------------------------------
# Azerothcore - Horde - Dungeon
# -----------------------------------------------------------------------------
mode = mode_fact.horde_s_abcde_solo_dungeon

# -----------------------------------------------------------------------------
# Don't Touch
# -----------------------------------------------------------------------------
# mode.dump(verbose=True)
mode.dump(verbose=False)
