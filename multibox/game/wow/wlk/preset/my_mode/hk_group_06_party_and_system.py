# -*- coding: utf-8 -*-

"""
实现组队以及系统功能性的按键.
"""

import typing as T

from hotkeynet import api as hk
from hotkeynet.api import KN

from ..my_act import api as act

if T.TYPE_CHECKING: # pragma: no cover
    from .mode import Mode


class HotkeyGroup06PartyAndSystemMixin:
    """
    todo: docstring.
    """
    def build_hk_confirm(self: "Mode"):
        """
        所有人点击弹出窗口中的确认按钮. 这个点确认的动作是通过宏命令来实现的.
        """
        with hk.Hotkey(
            id="Confirm",
            key=KN.SCROLOCK_ON(KN.CTRL_Y),
        ) as self.hk_confirm:
            with hk.SendLabel(
                id="all",
                to=self.get_lbs_all(),
            ):
                act.General.CONFIRM_MACRO_KEY_NUMPAD_5()

    def build_hk_leave_party(self: "Mode"):
        """
        所有人点击弹出窗口中的确认按钮. 这个点确认的动作是通过宏命令来实现的.
        """
        with hk.Hotkey(
            id="LeaveParty",
            key=KN.SCROLOCK_ON(KN.CTRL_L),
        ) as self.hk_leave_party:
            with hk.SendLabel(
                name="all",
                to=self.get_lbs_all(),
            ):
                act.General.LEAVE_PARTY_MACRO_KEY_ALT_END()

    def build_hk_all_pass_item(self: "Mode"):
        """
        所有的角色放弃拾取物品. 这个要配合 Domino 动作条插件使用. 拾取物品的按钮必须在特定的位置.
        """
        with hk.Hotkey(
            id="All Pass Item",
            key=KN.SCROLOCK_ON(KN.CTRL_ALT_Q),
        ) as self.hk_all_pass_item:
            with hk.SendLabel(
                id="pass_item_button",
                to=self.get_lbs_all(),
            ):
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.client.pass_item_button_x,
                    y=self.client.pass_item_button_1_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.client.pass_item_button_x,
                    y=self.client.pass_item_button_2_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.client.pass_item_button_x,
                    y=self.client.pass_item_button_3_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.client.pass_item_button_x,
                    y=self.client.pass_item_button_4_y,
                )

    def build_hk_volume_down(self: "Mode"):
        """
        所有的窗口的音量减小.
        """
        with hk.Hotkey(
            id="Volume Down",
            key=KN.SCROLOCK_ON(KN.CTRL_SHIFT_ALT_M),
        ) as self.hk_volumn_down:
            with hk.SendLabel(
                id="all",
                to=self.get_lbs_all(),
            ):
                act.System.MASTER_VOLUME_DOWN()

    def build_hk_rdf_confirm_role_and_enter_dungeon(self: "Mode"):
        """
        在排随机地下城时, 所有人点击确认角色和进入地下城的按钮.
        """
        with hk.Hotkey(
            id="RDFConfirmRoleAndEnterDungeon",
            key=KN.SCROLOCK_ON(KN.CTRL_SHIFT_ALT_Y),
        ) as self.hk_rdf_confirm_role_and_enter_dungeon:
            with hk.SendLabel(
                id="all",
                to=self.get_lbs_all(),
            ):
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.client.rdf_confirm_role_accept_button_x,
                    y=self.client.rdf_confirm_role_accept_button_y,
                )
                hk.ClickMouse(button=KN.MOUSE_LButton).set_mode_as_x_y(
                    x=self.client.rdf_enter_dungeon_button_x,
                    y=self.client.rdf_enter_dungeon_button_y,
                )

    def build_hk_group_06_party_and_system_mixin(self: "Mode"):
        self.build_hk_confirm()
        self.build_hk_leave_party()
        self.build_hk_all_pass_item()
        self.build_hk_volume_down()
        self.build_hk_rdf_confirm_role_and_enter_dungeon()
