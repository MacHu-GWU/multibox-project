# -*- coding: utf-8 -*-

from multibox.app.azerothcore.play import (
    dungeon_mode_fact,
    raid_mode_fact,
)


def test():
    for mode in [
        raid_mode_fact.x10p_core_team,
        raid_mode_fact.x10p_naxx_abomination_4th_boss,
        raid_mode_fact.x25p_core_team,
        raid_mode_fact.x25p_core_team_ICC_1,
        dungeon_mode_fact.x5p_horde_s_abcde,
    ]:
        mode.render(verbose=False)


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.app.azerothcore", preview=False, is_folder=True)
