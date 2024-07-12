# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TC
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class AltShiftFMixin:
    """
    todo: docstring
    """

    def build_hk_default_alt_shift_f(self: "Mode"):
        """
        **说明**

        所有的鸟德轮流放星落. 适用团队中有 3 个鸟德打小队副本的情况, 可以保证每一波小怪
        都有星落技能.

        **使用方法**

        按 1 下就有一个鸟德放星落, 再按一下就是另一个鸟德. 如果要想所有
        鸟德一齐放星落, 可以使用 :meth:`...`.

        **动作条安排**

        - 动作条按钮上就是星落技能.
        - 动作条按钮要绑定 ``Alt + F`` 快捷键, 并确保跟 ``act.DruidBalance.Starfall``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Shift F - 鸟德轮流放星落",
            key=KN.SCROLOCK_ON(KN.ALT_SHIFT_F),
        ) as self.hk_alt_shift_f_take_turn_star_fall:
            for lb in self.get_lbs_by_tc(TC.druid_balance):
                with hk.Toggle():
                    with hk.SendLabel(to=[lb]):
                        act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                        act.DruidBalance.Starfall()

    def build_alt_shift_f_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_alt_shift_f()
