# -*- coding: utf-8 -*-

import typing as T

from .ctrl_1_to_6 import Ctrl1To6Mixin

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode

class HotkeyGroup04PetControlMixin(
    Ctrl1To6Mixin
):
    def build_hk_group_04_pet_control_mixin(self: "Mode"):
        self.build_ctrl_1_to_6_mixin()