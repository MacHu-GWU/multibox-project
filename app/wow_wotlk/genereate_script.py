# -*- coding: utf-8 -*-

from multibox.app.wow_wotlk.gen_dataset import make_module
# make_module()

from multibox.app.wow_wotlk.dataset import mode_fact
from multibox.app.wow_wotlk.paths import dir_app_wow_wotlk, path_wow_wotlk_hkn

# ==============================================================================
# Azerothcore
# ==============================================================================
# -----------------------------------------------------------------------------
# Azerothcore - Alliance - Dungeon
# -----------------------------------------------------------------------------
# mode = mode_fact.acore_alliance_r_abcde_solo_dungeon

# -----------------------------------------------------------------------------
# Azerothcore - Alliance - Raid
# -----------------------------------------------------------------------------
# mode = mode_fact.acore_alliance_r_abcdefghij_solo_raid
mode = mode_fact.acore_alliance_r_a_to_y_solo_25raid

# -----------------------------------------------------------------------------
# Azerothcore - Horde - Dungeon
# -----------------------------------------------------------------------------
# mode = mode_fact.acore_horde_s_abcde_solo_dungeon

# -----------------------------------------------------------------------------
# Azerothcore - Horde - Raid
# -----------------------------------------------------------------------------

# ==============================================================================
# Warmane Icecrown
# ==============================================================================
# mode = mode_fact.warmane_quarterly_login_team1
# mode = mode_fact.warmane_quarterly_login_team2

# -----------------------------------------------------------------------------
# Don't Touch
# -----------------------------------------------------------------------------
# --- Dump one mode to hotkeynet.js
mode.script_path = path_wow_wotlk_hkn

# mode.dump(verbose=True)
mode.dump(verbose=False)

# --- Dump all mode
# for property_name in mode_fact.__class__.__dict__:
#     if not property_name.startswith("_"):
#         mode = getattr(mode_fact, property_name)
#         script_path = dir_app_wow_wotlk.joinpath(f"hotkeynet-{property_name}.js")
#         mode.script_path = script_path
#         # mode.dump(verbose=True)
#         mode.dump(verbose=False)
