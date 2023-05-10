# -*- coding: utf-8 -*-

"""
Todo: doc string here
"""

import typing as T
import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path

from .factory.game_client import GameClient
from .team import Team
from .hkn.script import HknScript
from .paths import path_azerothcore_hkn


@attr.s
class Mode(AttrsClass):
    """
    Mode 是你最终选择要玩的游戏模式. 它相当于是一堆工厂类工厂函数的集合, 提供了一个 namespace
    来组织这些工厂函数. 一个 Mode 包括了:

    :game_client: 客户端的相关设置.
    :team: 你要用哪些账号, 哪些角色, 哪些天赋, 分别在哪些窗口玩.
    :script: 你的多开脚本.

    Mode 也是用来最终生成 HotkeyNet 脚本的类.
    """

    game_client: T.Optional[GameClient] = attr.ib(default=None)
    team: T.Optional["Team"] = attr.ib(default=None)
    hkn_script: T.Optional["HknScript"] = attr.ib(default=None)
    path: T.Optional[Path] = attr.ib(default=path_azerothcore_hkn)

    def __attrs_post_init__(self):
        self.hkn_script = HknScript(mode=self)

    def render(self, verbose: bool = False) -> str:
        """
        Render the hotkeynet script as string.
        """
        return self.hkn_script.script.render(verbose=verbose)

    def dump(self, verbose: bool = False):
        """
        Write
        """
        self.path.write_text(self.render(verbose=verbose))
