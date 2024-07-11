# -*- coding: utf-8 -*-

import typing as T

from .ctrl_oem3 import CtrlOem3Mixin

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class HotkeyGroup07UtilitySpellMixin(
    CtrlOem3Mixin,
):
    def build_hk_group_07_mixin(self: "Mode"):
        self.build_ctrl_oem3_mixin()
