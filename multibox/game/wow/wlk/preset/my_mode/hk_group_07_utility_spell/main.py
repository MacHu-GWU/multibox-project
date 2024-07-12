# -*- coding: utf-8 -*-

import typing as T

from .ctrl_oem3 import CtrlOem3Mixin
from .ctrl_z import CtrlZMixin
from .ctrl_t import CtrlTMixin
from .alt_x import AltXMixin
from .r import RMixin
from .t import TMixin
from .alt_shift_r import AltShiftRMixin
from .alt_shift_t import AltShiftTMixin
from .alt_shift_f import AltShiftFMixin
from .alt_shift_g import AltShiftGMixin
from .alt_shift_z import AltShiftZMixin
from .alt_shift_x import AltShiftXMixin
from .alt_shift_c import AltShiftCMixin

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class HotkeyGroup07UtilitySpellMixin(
    CtrlOem3Mixin,
    CtrlZMixin,
    CtrlTMixin,
    AltXMixin,
    RMixin,
    TMixin,
    AltShiftRMixin,
    AltShiftTMixin,
    AltShiftFMixin,
    AltShiftGMixin,
    AltShiftZMixin,
    AltShiftXMixin,
    AltShiftCMixin,
):
    def build_hk_group_07_utility_spell_mixin(self: "Mode"):
        self.build_ctrl_oem3_mixin()
        self.build_ctrl_z_mixin()
        self.build_ctrl_t_mixin()
        self.build_alt_x_mixin()
        self.build_r_mixin()
        self.build_t_mixin()
        self.build_alt_shift_r_mixin()
        self.build_alt_shift_t_mixin()
        self.build_alt_shift_f_mixin()
        self.build_alt_shift_g_mixin()
        self.build_alt_shift_z_mixin()
        self.build_alt_shift_x_mixin()
        self.build_alt_shift_c_mixin()
