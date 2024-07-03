# -*- coding: utf-8 -*-

from multibox.game.wow.window import Window


class TestWindow:

    def test_make_label(self):
        assert Window.make_label(1) == "w01"
        assert Window.make_label(2) == "w02"

    def test_make(self):
        window = Window.make(1)
        assert window.label == "w01"
        assert window.title == "WoW01"
        assert window.index == 1

    def test_to_labels(self):
        assert Window.to_labels(1) == ["w01"]
        assert Window.to_labels("w01") == ["w01"]
        assert Window.to_labels([1, "w02"]) == ["w01", "w02"]


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.window", preview=False)
