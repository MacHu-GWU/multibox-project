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


class HotkeyGroup10ShiftNumpad1To12:
    """
    注意: Shift + Numpad 和 Ctrl / Alt + Numpad 的工作原理不同. 在传统键盘中,
    Shift + Numpad 的效果是将 Numpad 的按键映射为 Home, End, PgUp, PgDn, Insert, Delete,
    等案件 (你看小键盘数字键上面的字母就懂了).
    """

    def build_hk_shift_numpad_1(self: "Mode"):
        """
        todo: docstring
        """
        with hk.Hotkey(
            id="Shift Numpad1",
            key=KN.SCROLOCK_ON(KN.NUMPAD_SHIFT_1_END),
        ) as self.hk_shift_numpad_1:
            with hk.SendLabel(
                name=TC.shaman.name,
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.Call_of_the_Ancestors()

    def build_hk_shift_numpad_2(self: "Mode"):
        """
        todo: docstring
        """
        with hk.Hotkey(
            id="Shift Numpad2",
            key=KN.SCROLOCK_ON(KN.NUMPAD_SHIFT_2_DOWN),
        ) as self.hk_shift_numpad_2:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.Totemic_Recall()

    def build_hk_group_10_mixin(self):
        self.build_hk_shift_numpad_1()
        self.build_hk_shift_numpad_2()
