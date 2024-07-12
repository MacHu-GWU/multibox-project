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


class CtrlTMixin:
    """
    todo: docstring
    """

    def build_hk_default_ctrl_t(self: "Mode"):
        """
        **说明**

        所有人吃食物回血回蓝.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上是一个能同时回血回蓝的食物.
        - 动作条按钮要绑定 ``Ctrl + T`` 快捷键.
        """

        with hk.Hotkey(
            id="Ctrl + T - 所有人吃食物",
            key=KN.SCROLOCK_ON(KN.CTRL_T),
        ) as self.hk_ctrl_t_eat_and_drink_food:
            with hk.SendLabel(
                to=self.get_lbs_all(),
            ):
                act.General.EAT_FOOD_KEY_CTRL_T()

    def build_ctrl_t_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_ctrl_t()
