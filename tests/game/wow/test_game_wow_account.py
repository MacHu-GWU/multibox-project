# -*- coding: utf-8 -*-

"""
注: 这个模块没有什么特定功能, 它的方法都在 ``BaseSemiMutableModel`` 基类的单元测试中测过了.
"""

from multibox.game.wow.account import Account


class TestAccount:
    def test(self):
        _ = Account(username="acc1", password="pass1")


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.account", preview=False)
