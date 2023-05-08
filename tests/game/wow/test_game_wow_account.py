# -*- coding: utf-8 -*-

from pathlib_mate import Path
from multibox.game.wow.account import (
    Account,
    AccountLoader,
)


class TestAccount:
    def test_make(self):
        loader = AccountLoader(path=Path.dir_here(__file__).joinpath("accounts.json"))

        acc1 = loader.load("acc1")
        assert isinstance(acc1, Account) is True
        assert acc1.username == "acc1"
        assert acc1.password == "pwd1"


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.account", preview=False)
