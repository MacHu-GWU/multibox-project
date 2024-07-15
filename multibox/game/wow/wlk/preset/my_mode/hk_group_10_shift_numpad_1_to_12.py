# -*- coding: utf-8 -*-

"""
实现 Shift + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
"""

import typing as T

from hotkeynet import api as hk
from hotkeynet.api import KN

from multibox.game.wow.wlk.api import TalentCategory as TC
from ..my_act import api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


class HotkeyGroup10ShiftNumpad1To12Mixin:
    """
    注意: Shift + Numpad 和 Ctrl / Alt + Numpad 的工作原理不同. 在传统键盘中,
    Shift + Numpad 的效果是将 Numpad 的按键映射为 Home, End, PgUp, PgDn, Insert, Delete,
    等按键 (你看小键盘数字键上面的字母就懂了). 所以不建议使用 Shift + Numpad 作为快捷键.
    """
