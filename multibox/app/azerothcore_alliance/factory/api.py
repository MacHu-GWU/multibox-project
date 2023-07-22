# -*- coding: utf-8 -*-

"""
当你想要 import multibox.app.azerothcore.factory 里面的模块里的东西的时候, 不要直接 import,
而是通过这个 API 模块 import.
"""

from .account import acc_fact
from .character import (
    char_fact,
    char_group,login_char_fact,
    raid_active_char_fact,
    dungeon_active_char_fact,
)
from .game_client import game_client_fact
from .icons import Icons as icon_fact
from . import action as act
