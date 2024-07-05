# -*- coding: utf-8 -*-

import attrs
from multibox.game.window import Window as BaseWindow


# World of Warcraft Window
@attrs.define(eq=False, slots=False)
class Window(BaseWindow):
    @classmethod
    def make_title(cls, index: int) -> str:
        return cls.index_to_text(index=index, prefix="WoW", zfill=2)

    @classmethod
    def make_label(cls, index: int) -> str:
        return cls.index_to_text(index=index, prefix="w", zfill=2)


class TestWindow:
    def test_make(self):
        window = Window.new(1)
        assert window.index == 1
        assert window.label == "w01"
        assert window.title == "WoW01"

    def test_to_labels(self):
        assert Window.to_labels(1) == ["w01"]
        assert Window.to_labels("w01") == ["w01"]
        assert Window.to_labels([1, "w02"]) == ["w01", "w02"]


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.window", preview=False)
