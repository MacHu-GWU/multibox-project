# -*- coding: utf-8 -*-

from multibox.app.acore.dataset import mode_fact


def test():
    for mode in [
        mode_fact.alliance_r_abcde_solo_dungeon,
        mode_fact.alliance_r_abcdefghij_solo_raid,
        mode_fact.horde_s_abcde_solo_dungeon,
    ]:
        mode.render(verbose=False)


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.app.acore", preview=False, is_folder=True)
