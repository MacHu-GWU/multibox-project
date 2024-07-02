# -*- coding: utf-8 -*-

from multibox.game.wow.wlk.client import Client


class TestGameClient:
    def test(self):
        client = Client()
        _ = client


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.wlk.client", preview=False)
