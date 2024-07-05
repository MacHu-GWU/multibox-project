# -*- coding: utf-8 -*-

"""
实现各种特殊 Boss 战时候的特定快捷键 S. 例如鸟德星落, 鸟德吹风, 法师打断, 等等.
"""

import typing as T
import itertools

from hotkeynet import api as hk
from hotkeynet.api import KN

from multibox.game.wow.wlk.api import TalentCategory as TC
from ..my_act import api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


class HotkeyGroup12SpecialMixin:
    def build_icc_boss1(self: "Mode"):
        with hk.Hotkey(
            id="Shift + Z",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.Z)),
        ) as self.hk_shift_z:
            with hk.SendLabel(
                to=self.lbs_all,
            ):
                hk.Key.trigger()

        with hk.Hotkey(
            id="Shift + T",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.T)),
        ) as self.hk_shift_t:
            with hk.SendLabel(
                to=self.lbs_all,
            ):
                hk.Key.trigger()

        with hk.Hotkey(
            id="Shift + X",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.X)),
        ) as self.hk_shift_x:
            with hk.SendLabel(
                to=self.lbs_all,
            ):
                hk.Key.trigger()

    def build_hk_group_12_mixin(self: "Mode"):
        if "icc_boss1" in self.name:
            self.build_icc_boss1()
