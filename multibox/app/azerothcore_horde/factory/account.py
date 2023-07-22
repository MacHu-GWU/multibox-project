# -*- coding: utf-8 -*-

"""
此模块用于枚举所有的在 azerothcore 的账号密码, 并安全地在 HotkeyNet 脚本中引用这些信息.
避免将敏感信息写入代码. 实现数据和运算分离的效果.
"""

from multibox.runtime import IS_CI
from multibox.game.wow.api import AccountLoader
from multibox.app.azerothcore_horde.paths import path_azerothcore_horde_accounts_json, path_azerothcore_horde_test_accounts_json

if IS_CI:
    path = path_azerothcore_horde_test_accounts_json
else:
    path = path_azerothcore_horde_accounts_json

_account_loader = AccountLoader(path=path)


class AccountFactory:
    """
    枚举出所有的用户名密码的数据对象, 以供之后引用.
    """
    rab01 = _account_loader.load("rab01")
    rab02 = _account_loader.load("rab02")
    rab03 = _account_loader.load("rab03")
    rab04 = _account_loader.load("rab04")
    rab05 = _account_loader.load("rab05")

acc_fact = AccountFactory
