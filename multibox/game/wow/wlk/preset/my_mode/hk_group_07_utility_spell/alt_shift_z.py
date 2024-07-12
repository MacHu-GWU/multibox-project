# -*- coding: utf-8 -*-

import typing as T
import random

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TL, TC
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class AltShiftZMixin:
    def build_hk_default_alt_shift_z(self: "Mode"):
        """
        **说明**

        所有的牧师轮流放群体恐惧. 适用团队中有多个牧师打副本的情况, 可以保证小怪一靠近就被恐惧开了.

        **使用方法**

        按 1 下就有一个牧师放群体恐惧, 再按一下就是另一个牧师.

        **动作条安排**

        - 动作条按钮上就是恐惧技能.
        - 动作条按钮要绑定 ``Alt + E`` 快捷键, 并确保跟 ``act.Priest.Psychic_Scream``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Shift Z - 牧师轮流放群体恐惧",
            key=KN.SCROLOCK_ON(KN.ALT_SHIFT_Z),
        ) as self.hk_alt_shift_f_take_turn_fear:
            lbs_priest = self.get_lbs_by_tc(TC.priest)
            lbs_warlock = self.get_lbs_by_tc(TC.warlock)
            for lb in lbs_priest:
                with hk.Toggle():
                    with hk.SendLabel(to=[lb]):
                        act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                        act.Priest.Psychic_Scream()
                    # 随机选择一个术士放恐惧
                    if len(lbs_warlock):
                        lb = random.choice(lbs_warlock)
                        with hk.SendLabel(to=[lb]):
                            act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                            act.Target.TARGET_FOCUS_TARGET()
                            act.Warlock.Fear()

    def build_alt_shift_z_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_alt_shift_z()
