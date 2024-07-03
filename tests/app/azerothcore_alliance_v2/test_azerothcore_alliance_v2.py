# -*- coding: utf-8 -*-

from multibox.app.azerothcore_alliance_v2.api import (
    dungeon_mode_fact,
    raid_mode_fact,
)


def test():
    for mode in [
        dungeon_mode_fact.x5p_alliance_r_abcde,
        # raid_mode_fact.x10p_alliance_r_abcdefghij,
    ]:
        mode.render(verbose=False)


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.app.azerothcore_alliance_v2", preview=False, is_folder=True)
