# -*- coding: utf-8 -*-

import attrs

from ...mode import Mode as _Mode

from .hk_label import HotkeyLabelMixin
from .hk_cmd import HotkeyCommandMixin

from .hk_group_01_window_and_login import HotkeyGroup01WindowAndLoginMixin
from .hk_group_02_movement import HotkeyGroup02MovementMixin
from .hk_group_03_act_1_to_12_old import HotkeyGroup03Act1To12MixinOld
from .hk_group_03_act_1_to_12.main import HotkeyGroup03Act1To12Mixin
from .hk_group_04_pet_control.main import HotkeyGroup04PetControlMixin
from .hk_group_05_numpad_1_to_12 import HotkeyGroup05Numpad1To12Mixin
from .hk_group_06_party_and_system import HotkeyGroup06PartyAndSystemMixin
from .hk_group_07_utility_spell import HotkeyGroup07UtilitySpellMixin
from .hk_group_08_alt_numpad_1_to_12 import HotkeyGroup08AltNumpad1To12
from .hk_group_09_ctrl_numpad_1_to_12 import HotkeyGroup09CtrlNumpad1To12
from .hk_group_10_shift_numpad_1_to_12 import HotkeyGroup10ShiftNumpad1To12
from .hk_group_11_healbot import HotkeyGroup11Healbot
from .hk_group_12_special.main import HotkeyGroup12SpecialMixin

from .hk_control_panel import HotkeyControlPanelMixin


@attrs.define(eq=False, slots=False)
class Mode(
    _Mode,
    # --- Label and Command
    HotkeyLabelMixin,
    HotkeyCommandMixin,
    # --- Group 1 to 12
    HotkeyGroup01WindowAndLoginMixin,
    HotkeyGroup02MovementMixin,
    HotkeyGroup03Act1To12Mixin,
    HotkeyGroup03Act1To12MixinOld,
    HotkeyGroup04PetControlMixin,
    HotkeyGroup05Numpad1To12Mixin,
    HotkeyGroup06PartyAndSystemMixin,
    HotkeyGroup07UtilitySpellMixin,
    HotkeyGroup08AltNumpad1To12,
    HotkeyGroup09CtrlNumpad1To12,
    HotkeyGroup10ShiftNumpad1To12,
    HotkeyGroup11Healbot,
    HotkeyGroup12SpecialMixin,
    # --- Control Panel
    HotkeyControlPanelMixin,
):
    is_tank1_has_healer: bool = attrs.field(default=False)
    is_tank2_has_healer: bool = attrs.field(default=False)
    is_tank1_has_beacon: bool = attrs.field(default=False)
    is_tank2_has_beacon: bool = attrs.field(default=False)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()

        self.build_label_mixin()
        self.build_command_mixin()

        self.build_hk_group_01_window_and_login_mixin()
        self.build_hk_group_02_movement_mixin()
        self.build_hk_group_03_act_1_to_12_mixin()
        self.build_hk_group_03_act_1_to_12_mixin_old()
        self.build_hk_group_04_pet_control_mixin()
        self.build_hk_group_05_numpad_1_to_12_mixin()
        self.build_hk_group_06_party_and_system_mixin()
        self.build_hk_group_07_mixin()
        self.build_hk_group_08_alt_numpad_1_to_12_mixin()
        self.build_hk_group_09_ctrl_numpad_1_to_12_mixin()
        self.build_hk_group_10_mixin()
        self.build_hk_group_11_healbot_mixin()
        self.build_hk_group_12_special_mixin()

        self.build_control_panel_mixin()
