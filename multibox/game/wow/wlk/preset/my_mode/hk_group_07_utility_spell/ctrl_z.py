# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
import multibox.game.wow.wlk.api as wlk
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class CtrlZMixin:
    """
    todo: docstring
    """

    def build_hk_default_ctrl_z(self: "Mode"):
        """
        **说明**

        所有人使用陆地坐骑. 可以是上马也可以是下马. 这个按键主要是在战场等无法使用飞行坐骑
        的地方替代平时用的一键上 陆地/飞行 坐骑的宏, 例如冬拥湖. 因为在战场中如果按平时的宏,
        它会认为是可以飞的而不断尝试用飞行坐骑导致卡住.

        **使用方法**

        - 全团下马: 先按一下这个键然后全团后退确保全团下马. 已经在马上的角色会下马, 而
        在地上的角色的上马技能会被后退键打断.
        - 全团上马: 先用 "全团下马" 的方法确保全团下马然后再按一次这个键, 1.5 秒后全团上马.

        **动作条安排**

        - 动作条按钮上是一个坐骑技能.
        - 动作条按钮要绑定 ``Ctrl + Z`` 快捷键.
        """
        with hk.Hotkey(
            id="Ctrl + Z - 所有人使用陆地坐骑",
            key=KN.SCROLOCK_ON(KN.CTRL_Z),
        ) as self.hk_ctrl_z_use_land_mount:
            with hk.SendLabel(
                to=self.get_lbs_all(),
            ):
                act.General.LAND_MOUNT_SPELL_KEY_CTRL_Z()

    def build_ctrl_z_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_ctrl_z()
