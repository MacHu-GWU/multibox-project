# -*- coding: utf-8 -*-

"""
实现组队以及系统功能性的按键.
"""

import typing as T

from hotkeynet import api as hk
from hotkeynet.api import KN

from ..my_act import api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


class HotkeyGroup06PartyAndSystemMixin:
    """
    todo: docstring.
    """

    def build_hk_confirm(self: "Mode"):
        """
        **说明**

        魔兽世界客户端 UI 中有一个通用的弹出窗口. 例如邀请组队, 是否一起开始护送任务, 进入战场,
        拍卖行买货时的确认按钮等. 这个按键可以让所有人点击弹出窗口中的确认按钮 (主要用于组队).

        这个点确认的动作是通过 ``/click StaticPopup1Button1`` 宏命令来实现的.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上就是确认宏.
        - 动作条按钮要绑定 ``Numpad 5`` 快捷键, 并确保跟
            ``act.General.CONFIRM_MACRO_KEY_NUMPAD_5`` 中的定义一致.
        """
        with hk.Hotkey(
            id="Click Confirm Button",
            key=KN.SCROLOCK_ON(KN.CTRL_Y),
        ) as self.hk_confirm:
            with hk.SendLabel(
                id="Click Confirm Button",
                to=self.get_lbs_all(),
            ):
                act.General.CONFIRM_MACRO_KEY_NUMPAD_5()

    def build_hk_leave_party(self: "Mode"):
        """
        **说明**

        有时你会需要所有人退队重新组队.

        这个退队的动作是通过 ``/script LeavePart()`` 宏命令来实现的.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上就是退队宏.
        - 动作条按钮要绑定 ``Alt End`` 快捷键, 并确保跟
            ``act.General.LEAVE_PARTY_MACRO_KEY_ALT_END`` 中的定义一致.
        """
        with hk.Hotkey(
            id="LeaveParty",
            key=KN.SCROLOCK_ON(KN.CTRL_L),
        ) as self.hk_leave_party:
            with hk.SendLabel(
                name="LeaveParty",
                to=self.get_lbs_all(),
            ):
                act.General.LEAVE_PARTY_MACRO_KEY_ALT_END()

    def build_hk_all_pass_item(self: "Mode"):
        """
        **说明**

        在多开时, 你一般只需要一个人拾取物品, 其他角色都放弃拾取, 不然物品会分散到不同角色的
        背包中导致很乱. 这个按键可以让所有人都点击放弃物品 (点击 roll 点界面右上角的红叉)
        这个要配合 Domino 动作条插件使用. 拾取物品的按钮必须在特定的位置, 并且在脚本中定义好
        这个特定坐标.

        **使用方法**

        按就行了.

        **动作条安排**

        无需动作条.
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
        **说明**

        有时候你不注意的化让所有游戏窗口哪怕不是在前台都播放声音的化, 你可能会听到乱糟糟的声音.
        这时这个按键就可以让所有窗口声音变小直至静音, 然后再手动将需要的窗口的声音打开既可.
        不然你就得一个一个窗口调整, 或者干脆所有窗口退出重新登录, 这样会太麻烦了.

        虽然我们大多数情况都会只让当前窗口播放声音, 但也有特殊情况下比如你需要让后台挂机的那个
        窗口也能听到有人回复你的声音时, 还是会有让多个窗口有声音的需求的.

        **使用方法**

        按就行了.

        **动作条安排**

        - 系统音量减小要绑定 ``Ctrl Minus (减号)`` 快捷键. 并确保跟
            ``act.General.MASTER_VOLUME_DOWN`` 中的定义一致.
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
        **说明**

        在排随机地下城时, 当已经排好的时候会弹出一个确认窗口. 这个窗口的确认按钮是无法通过
        :meth:`build_hk_confirm` 中的宏确认的, 必须要用鼠标点击. 这个按键可以让所有人点击
        确认按钮.

        **使用方法**

        按就行了.

        **动作条安排**

        无, 只需要在多开脚本定义按钮的坐标既可.
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
