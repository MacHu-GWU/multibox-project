# -*- coding: utf-8 -*-

from multibox.game.wow.wlk.game_client import GameClient


class TestGameClient:
    def test(self):
        game_client = GameClient()
        game_client.get_choose_char_x_y(1)


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.wlk.game_client", preview=False)
