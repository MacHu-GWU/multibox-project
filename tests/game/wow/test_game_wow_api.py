# -*- coding: utf-8 -*-

from multibox.game.wow.api import (
    Account,
    AccountLoader,
    Character,
    CharacterHelper,
    Talent,
    TalentCategory,
    Window,
)


def test():
    pass


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.api", preview=False)
