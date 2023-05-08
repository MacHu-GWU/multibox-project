# -*- coding: utf-8 -*-

from multibox.game.wow.wlk import act


def test():
    _ = act.PaladinHoly.Beacon_of_Light


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.wlk.act", preview=False)
