# -*- coding: utf-8 -*-

"""
实现在多开模式下 小键盘 Numpad 1-12 的功能. 这些按键可以用专用 MMORPG 鼠标的侧面轻松按到.
"""

import typing as T

from hotkeynet import api as hk
from hotkeynet.api import KN, CAN

from multibox.game.wow.wlk.api import TalentCategory as TC
from ..my_act import api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


class HotkeyGroup05Numpad1To12Mixin:
    """
    todo: docstring.
    """

    def build_hk_numpad_4(self: "Mode"):
        """
        **说明**

        重置所有人的视角为从上往下 45 度俯视的视角. 只有在所有人的视角一致的情况下, 才能保证
        哪些用鼠标在窗口内同一个位置点击的操作是一致的.

        注: 默认视角的配置是在 ``WTF/Account/{account_name}/config-cache.wtf`` 文件中的
        cameraViewDistance, cameraPitchB, cameraYawB 的字段中定义的.

        **使用方法**

        按就行了.

        **动作条安排**

        无
        """
        with hk.Hotkey(
            id="ResetCamera",
            key=KN.SCROLOCK_ON(KN.NUMPAD_4),
        ) as self.hk_numpad_4_reset_camera:
            with hk.SendLabel(
                id="ResetCamera",
                to=self.get_lbs_all(),
            ):
                act.Camera.SET_FIRST_CAMERA_VIEW_2()

    def build_hk_numpad_5(self: "Mode"):
        """
        **说明**

        所有萨满批量放置图腾.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上就是先祖召唤技能.
        - 动作条按钮要绑定 ``Shift + ~`` 快捷键, 并确保跟 ``act.Shaman.Call_of_the_Ancestors``
            中的定义一致.
        """
        with hk.Hotkey(
            id="ShamanPutTotem",
            key=KN.SCROLOCK_ON(KN.NUMPAD_5),
        ) as self.hk_numpad_5_shaman_put_totem:
            with hk.SendLabel(
                id="ShamanPutTotem",
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.Shaman.Call_of_the_Ancestors()

    def build_hk_numpad_6(self: "Mode"):
        """
        **说明**

        所有萨满回收所有图腾.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上就是召回图腾技能.
        - 动作条按钮要绑定 ``Shift + Tab`` 快捷键, 并确保跟 ``act.Shaman.Totemic_Recall``
            中的定义一致.
        """
        with hk.Hotkey(
            id="ShamanRecallTotem",
            key=KN.SCROLOCK_ON(KN.NUMPAD_6),
        ) as self.hk_numpad_6_shaman_recall_totem:
            with hk.SendLabel(
                name="ShamanRecallTotem",
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.Shaman.Totemic_Recall()

    def build_hk_numpad_7(self: "Mode"):
        """
        **说明**

        所有人后退一步, 解除跟随状态.

        **使用方法**

        按就行了.

        **动作条安排**

        无.
        """
        with hk.Hotkey(
            id="StopFollowing",
            key=KN.SCROLOCK_ON(KN.NUMPAD_7),
        ) as self.hk_numpad_7_all_move_backward:
            with hk.SendLabel(
                id="StopFollowing",
                to=self.get_lbs_all(),
            ):
                act.Movement.MOVE_BACKWARD()

    def build_hk_numpad_8(self: "Mode"):
        """
        **说明**

        在所有窗口内的相对位置一样的地方点击左键. 常用的场景有:

        - 在人物选择界面进入游戏.
        - 所有人接受任务.
        - 打开关闭包裹.
        - 所有人在同一区域施放 AOE (例如暴风雪)
        - 等等 ...

        设置于 Numpad8 是因为左键用的频率较高, 使用 MMO 鼠标时大拇指自然的就在这个位置.
        有些应用场景, 例如在同一区域施放 AOE 技能, 需要所有人的视角一致才能保证你在司机上
        点击的位置同时也是你的跟随者点击的位置. 因此, 建议使用 :meth:`build_hk_numpad_4`
        中的按键让所有人的视角一致.

        **使用方法**

        按就行了.

        **动作条安排**

        无.
        """
        with hk.Hotkey(
            id="SyncLeftClick",
            key=KN.SCROLOCK_ON(KN.NUMPAD_8),
        ) as self.hk_numpad_8_sync_left_click:
            with hk.SendLabel(
                id="all",
                to=self.get_lbs_all(),
            ):
                CAN.LEFT_CLICK()

    def build_hk_numpad_9(self: "Mode"):
        """
        **说明**

        在所有窗口内的相对位置一样的地方点击右键. 常用的场景有:

        - 拾取任务物品 (那种一个鼠标移上去出现一个齿轮的互动方式)
        - 开门, 开箱子等.

        设置于 Numpad9 是因为想要放在 左键点击 Hotkey 的按键 Numpad8 旁边.
        有些应用场景, 需要所有人的视角一致才能保证你在司机上
        点击的位置同时也是你的跟随者点击的位置. 因此, 建议使用 :meth:`build_hk_numpad_4`
        中的按键让所有人的视角一致.

        **使用方法**

        按就行了.

        **动作条安排**

        无.
        """
        with hk.Hotkey(
            id="SyncRightClick",
            key=KN.SCROLOCK_ON(KN.NUMPAD_9),
        ) as self.hk_numpad_9_sync_right_click:
            with hk.SendLabel(
                id="all",
                to=self.get_lbs_all(),
            ):
                CAN.RIGHT_CLICK()

    def build_hk_numpad_10(self: "Mode"):
        """
        **说明**

        所有人跟随焦点角色.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上就是 ``/follow focus`` 跟随焦点宏.
            todo: 可能不需要宏, 只需要两个快捷键既可, 这是一个不需要一直按的低频操作,
            todo: 无需用宏绑定多个按键来节约 HotkeyNet 的按键来提高性能.
        - 动作条按钮要绑定 ``Numpad 12`` 快捷键, 并确保跟 ``act.Movement.FOLLOW_FOCUS``
            中的定义一致.
        """
        with hk.Hotkey(
            id="AllFollowFocus",
            key=KN.SCROLOCK_ON(KN.NUMPAD_0),
        ) as self.hk_numpad_0_all_follow_focus:
            with hk.SendLabel(
                id="all",
                to=self.get_lbs_all(),
            ):
                act.Movement.FOLLOW_FOCUS()

    def build_hk_numpad_11(self: "Mode"):
        """
        **说明**

        所有人上坐骑或是飞行形态.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上是上马宏, 具体宏命令请参考
            ``act.General.MOUNT_UP_MACRO_KEY_NUMPAD_11_DIVIDE`` 的文档.
        - 动作条按钮要绑定 ``Numpad 11`` 快捷键, 并确保跟
            ``act.General.MOUNT_UP_MACRO_KEY_NUMPAD_11_DIVIDE`` 中的定义一致.
        """
        with hk.Hotkey(
            id="AllMountUp",
            key=KN.SCROLOCK_ON(KN.NUMPAD_11_DIVIDE),
        ) as self.hk_numpad_11_mount_up:
            with hk.SendLabel(
                id="all",
                to=self.get_lbs_all(),
            ):
                act.General.MOUNT_UP_MACRO_KEY_NUMPAD_11_DIVIDE()

    def build_hk_numpad_12(self: "Mode"):
        """
        **说明**

        跟焦点的目标右键点击互动, 常用于接任务, 剥皮, 对话. 相当于先左键选中了焦点的目标
        (也就是司机所选定的目标), 然后右键点击与之互动.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上是 ``/assist focus`` 的宏
        - 动作条按钮要绑定 ``Numpad 3`` 快捷键, 并确保跟
            ``act.Target.TARGET_FOCUS_TARGET`` 中的定义一致. 而且跟目标互动的快捷键
            要设为 ``J``, 并确保跟  ``act.Target.INTERACT_WITH_TARGET`` 中的定义一致.
        """
        with hk.Hotkey(
            id="InteractFocusTarget",
            key=KN.SCROLOCK_ON(KN.NUMPAD_12_MULTIPLY),
        ) as self.hk_numpad_12_interact_with_focus_target:
            with hk.SendLabel(
                id="all",
                to=self.get_lbs_all(),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.Target.INTERACT_WITH_TARGET()

    def build_hk_group_05_numpad_1_to_12_mixin(self: "Mode"):
        self.build_hk_numpad_4()
        self.build_hk_numpad_5()
        self.build_hk_numpad_6()
        self.build_hk_numpad_7()
        self.build_hk_numpad_8()
        self.build_hk_numpad_9()
        self.build_hk_numpad_10()
        self.build_hk_numpad_11()
        self.build_hk_numpad_12()
