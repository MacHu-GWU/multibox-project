# -*- coding: utf-8 -*-

import typing as T

import attr
from attrs_mate import AttrsClass

from hotkeynet import api as hk

from .label import LabelMixin
from .cmd import CommandMixin

from .hk_group_01_window_and_login import HotkeyGroup01WindowAndLoginMixin
from .hk_group_02_movement import HotkeyGroup02MovementMixin
from .hk_group_03_act_1_to_12 import HotkeyGroup03Act1To12Mixin
from .hk_group_04_pet_control import HotkeyGroup04PetControlMixin
from .hk_group_05_numpad_1_to_12 import HotkeyGroup05Numpad1To12Mixin
from .hk_group_06_party_and_system import HotkeyGroup06PartyAndSystemMixin
from .hk_group_07_utility_spell import HotkeyGroup07UtilitySpellMixin
from .hk_group_08_alt_numpad_1_to_12 import HotkeyGroup08AltNumpad1To12
from .hk_group_09_ctrl_numpad_1_to_12 import HotkeyGroup09CtrlNumpad1To12
from .hk_group_10_shift_numpad_1_to_12 import HotkeyGroup10ShiftNumpad1To12
from .hk_group_11_healbot import HotkeyGroup11Healbot

from .control_panel import ControlPanelMixin

if T.TYPE_CHECKING:
    from ..mode import Mode


@attr.s
class HknScript(
    AttrsClass,
    #--- Label adn Command
    LabelMixin,
    CommandMixin,
    #--- Group 1 to 12
    HotkeyGroup01WindowAndLoginMixin,
    HotkeyGroup02MovementMixin,
    HotkeyGroup03Act1To12Mixin,
    HotkeyGroup04PetControlMixin,
    HotkeyGroup05Numpad1To12Mixin,
    HotkeyGroup06PartyAndSystemMixin,
    HotkeyGroup07UtilitySpellMixin,
    HotkeyGroup08AltNumpad1To12,
    HotkeyGroup09CtrlNumpad1To12,
    HotkeyGroup10ShiftNumpad1To12,
    HotkeyGroup11Healbot,
    #--- Control Panel
    ControlPanelMixin,
):
    script: hk.Script = attr.ib(factory=hk.Script)
    mode: T.Optional["Mode"] = attr.ib(default=None)

    def __attrs_post_init__(self):
        # 当创建 hotkeynet.api.Script 对象时, context 里是没有东西的, 我们需要用
        # 先调用 ``with Script()`` 的语法然后才能定义 Command, Hotkey, 这样很麻烦.
        # 所以我们手动将它设为 context 的顶层, 这样就可以直接定义 Command, Hotkey 了.
        hk.context.push(self.script)

        self.build_label_mixin()
        self.build_command_mixin()

        self.build_hk_group_01_window_and_login_mixin()
        self.build_hk_group_02_movement_mixin()
        self.build_hk_group_03_act_1_to_12_mixin()
        self.build_hk_group_04_pet_control_mixin()
        self.build_hk_group_05_numpad_1_to_12_mixin()
        self.build_hk_group_06_party_and_system_mixin()
        self.build_hk_group_07_mixin()
        self.build_hk_group_08_alt_numpad_1_to_12_mixin()
        self.build_hk_group_09_ctrl_numpad_1_to_12_mixin()
        self.build_hk_group_10_mixin()
        self.build_hk_group_11_healbot_mixin()

        self.build_control_panel_mixin()
