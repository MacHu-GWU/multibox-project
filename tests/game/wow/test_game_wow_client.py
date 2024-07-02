# -*- coding: utf-8 -*-

from multibox.game.wow.client import Client


class TestClient:
    def test_make(self):
        client = Client()
        _ = client


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.client", preview=False)
