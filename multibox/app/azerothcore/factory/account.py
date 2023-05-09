# -*- coding: utf-8 -*-

"""
此模块用于枚举所有的在 azerothcore 的账号密码, 并安全地在 HotkeyNet 脚本中引用这些信息.
避免将敏感信息写入代码. 实现数据和运算分离的效果.
"""

from multibox.runtime import IS_CI
from multibox.game.wow.api import AccountLoader
from multibox.app.azerothcore.paths import path_azerothcore_accounts_json, path_azerothcore_test_accounts_json

if IS_CI:
    path = path_azerothcore_test_accounts_json
else:
    path = path_azerothcore_accounts_json

_account_loader = AccountLoader(path=path)


class AccountFactory:
    """
    枚举出所有的用户名密码的数据对象, 以供之后引用.
    """

    fat01 = _account_loader.load("fat01")
    fat02 = _account_loader.load("fat02")
    fat03 = _account_loader.load("fat03")
    fat04 = _account_loader.load("fat04")
    fat05 = _account_loader.load("fat05")
    fat06 = _account_loader.load("fat06")
    fat07 = _account_loader.load("fat07")
    fat08 = _account_loader.load("fat08")
    fat09 = _account_loader.load("fat09")
    fat10 = _account_loader.load("fat10")
    fat11 = _account_loader.load("fat11")
    fat12 = _account_loader.load("fat12")
    fat13 = _account_loader.load("fat13")
    fat14 = _account_loader.load("fat14")
    fat15 = _account_loader.load("fat15")
    fat16 = _account_loader.load("fat16")
    fat17 = _account_loader.load("fat17")
    fat18 = _account_loader.load("fat18")
    fat19 = _account_loader.load("fat19")
    fat20 = _account_loader.load("fat20")
    fat21 = _account_loader.load("fat21")
    fat22 = _account_loader.load("fat22")
    fat23 = _account_loader.load("fat23")
    fat24 = _account_loader.load("fat24")
    fat25 = _account_loader.load("fat25")

    rab01 = _account_loader.load("rab01")
    rab02 = _account_loader.load("rab02")
    rab03 = _account_loader.load("rab03")
    rab04 = _account_loader.load("rab04")
    rab05 = _account_loader.load("rab05")
