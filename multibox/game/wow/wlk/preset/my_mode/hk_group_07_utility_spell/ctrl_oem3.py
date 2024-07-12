# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class CtrlOem3Mixin:
    """
    todo: docstring
    """

    def build_hk_default_ctrl_oem3(self: "Mode"):
        """
        **说明**

        所有人从坐骑上下来. 无论现在是在地上还是在马上还是在飞行坐骑上.

        **使用方法**

        按就行了.

        - 全团下马: 先按一下这个键然后全团后退确保全团下马. 已经在马上的角色会下马, 而
        在地上的角色的上马技能会被后退键打断.
        - 全团上马: 先用 "全团下马" 的方法确保全团下马然后再按一次这个键, 1.5 秒后全团上马.

        **动作条安排**

        - 动作条按钮上是一个下马宏. 你把所有角色的坐骑的技能都放在这个宏里. 比如你的 5 个角色
            用到了 10 种不同的坐骑, 那你就都放在这里. 不然 5 个角色的宏都得不一样, 比较麻烦
            宏的内容如下::

            #showtooltip
            /cancelaura [mounted] {坐骑名称}
            /cancelaura [mounted] {坐骑名称}

        - 动作条按钮要绑定 ``Ctrl + ~`` 快捷键.
        """
        with hk.Hotkey(
            id="Ctrl + ` - 所有人下坐骑",
            key=KN.SCROLOCK_ON(KN.CTRL_OEM3_WAVE_OR_BACK_QUOTE),
        ) as self.hk_ctrl_oem3_wave_dismount:
            with hk.SendLabel(
                to=self.get_lbs_all(),
            ):
                act.General.MOUNT_DOWN_MACRO_CTRL_OEM3_WAVE()

    def build_ctrl_oem3_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_ctrl_oem3()
