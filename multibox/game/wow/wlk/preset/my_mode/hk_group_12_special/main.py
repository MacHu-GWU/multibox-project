# -*- coding: utf-8 -*-

import typing as T

from .icc_boss1 import IccBoss1Mixin

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class HotkeyGroup12SpecialMixin(IccBoss1Mixin):
    def build_hk_group_12_special_mixin(self: "Mode"):
        if "icc_boss1" in self.name:
            self.build_hk_icc_boss1()
