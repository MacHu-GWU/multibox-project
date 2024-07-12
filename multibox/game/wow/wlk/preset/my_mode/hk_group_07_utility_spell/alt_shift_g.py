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


class AltShiftGMixin:
    """
    todo: docstring
    """

    def build_hk_default_alt_shift_g(self: "Mode"):
        """
        **说明**

        所有的鸟德轮流放台风. 适用于需要确保怪物一直无法近身的场景.

        **使用方法**

        按 1 下就有一个鸟德放台风, 再按一下就是另一个鸟德.

        **动作条安排**

        - 动作条按钮上就是台风技能.
        - 动作条按钮要绑定 ``G`` 快捷键, 并确保跟 ``act.DruidBalance.Typhoon``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Shift G - 鸟德轮流放台风",
            key=KN.SCROLOCK_ON(KN.ALT_SHIFT_G),
        ) as self.hk_alt_shift_g_take_turn_typhoon:
            for label in self.get_lbs_by_tc(TC.druid_balance):
                with hk.Toggle():
                    with hk.SendLabel(to=[label]):
                        act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                        act.DruidBalance.Typhoon()

    def build_alt_shift_g_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_alt_shift_g()
