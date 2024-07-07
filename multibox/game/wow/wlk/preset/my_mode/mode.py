# -*- coding: utf-8 -*-

import typing as T
import attrs

from ordered_set import OrderedSet
from multibox.game.wow.wlk.api import (
    Mode as _Mode,
    Character,
)

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
    tank1_direct_healer: T.Optional[Character] = attrs.field(default=None)
    tank2_direct_healer: T.Optional[Character] = attrs.field(default=None)
    extra_tank_healer: OrderedSet[Character] = attrs.field(factory=OrderedSet)
    is_tank1_has_beacon: bool = attrs.field(default=False)
    is_tank2_has_beacon: bool = attrs.field(default=False)
    tank1_beacon_paladin: T.Optional[Character] = attrs.field(default=None)
    tank2_beacon_paladin: T.Optional[Character] = attrs.field(default=None)
    extra_tank_beacon_paladin: OrderedSet[Character] = attrs.field(factory=OrderedSet)
    raid_healer: OrderedSet[Character] = attrs.field(factory=OrderedSet)

    def allocate_healer(self):
        """
        这个函数用来根据团队成员的天赋组成, 智能分配哪个治疗应该做什么工作. 我们要分配的工作有:

        1. 哪个治疗负责给主坦克直接刷血.
        2. 哪个治疗负责给副坦克直接刷血.
        3. 哪个奶骑给主坦克上圣光道标.
        4. 哪个奶骑给副坦克上圣光道标.
        5. 哪个治疗负责奶团.
        """
        # 将
        lbs_tank_healer = self.lbs_tank_healer
        lbs_paladin_holy = self.lbs_paladin_holy
        lbs_non_paladin_tank_healer = lbs_tank_healer.difference(lbs_paladin_holy)

        # # 确保有人奶 1 号坦克.
        # if self.lb_tank1:


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
