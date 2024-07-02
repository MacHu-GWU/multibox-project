# -*- coding: utf-8 -*-

from multibox.game.wow.account import Account


class TestAccount:
    def test_make(self):
        acc1_1 = Account("acc1", "pwd1")
        acc1_2 = Account("acc1", "pwd1")
        assert id(acc1_1) != id(acc1_2)


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.account", preview=False)
