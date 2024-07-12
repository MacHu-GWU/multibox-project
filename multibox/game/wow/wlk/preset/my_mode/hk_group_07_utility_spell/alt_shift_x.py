# -*- coding: utf-8 -*-

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TL, TC
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class AltShiftXMixin:
    def build_hk_default_alt_shift_x(self: "Mode"):
        """
        **说明**

        所有的元素萨轮流放雷霆风暴击退. 适用团队中有 3 个元素萨打小队副本的情况, 可以保证每一波
        小怪都有雷霆风暴.

        **使用方法**

        按 1 下就有一个元素萨放星落, 再按一下就是另一个元素萨.

        **动作条安排**

        - 动作条按钮上就是雷霆风暴技能.
        - 动作条按钮要绑定 ``Alt + F`` 快捷键, 并确保跟 ``act.ShamanElementalCombat.Thunderstorm``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Shift X - 元素萨轮流放雷霆风暴",
            key=KN.SCROLOCK_ON(KN.ALT_SHIFT_X),
        ) as self.hk_alt_shift_f_take_turn_thunder_storm:
            for lb in self.get_lbs_by_tc(TC.shaman_elemental):
                with hk.Toggle():
                    with hk.SendLabel(to=[lb]):
                        act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                        act.ShamanElementalCombat.Thunderstorm()

    def build_alt_shift_x_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_alt_shift_x()
