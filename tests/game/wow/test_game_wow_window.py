# -*- coding: utf-8 -*-

from multibox.game.wow.window import Window


class TestWindow:
    def test_make(self):
        window = Window.make(1)
        assert window.label == "w01"
        assert window.title == "WoW01"
        assert window.index == 1


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.window", preview=False)
