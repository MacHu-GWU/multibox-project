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


class Act2Mixin:
    """
    todo: docstring
    """
    def build_default_act2(self: "Mode"):
        """
        See :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="Key2",
            key=KN.SCROLOCK_ON(KN.KEY_2),
        ) as self.hk_2:
            self.build_tank_default_action(key=KN.KEY_2)
            self.build_dps_default_action(key=KN.KEY_2)

            # 德鲁伊, 萨满, 戒律牧, 神圣牧师 用位于 2 号键位上的一键治疗宏奶团
            lbs_paladin_holy, lbs_non_paladin_holy_healer = (
                self.lbs_paladin_holy_and_non_paladin_holy_healer
            )
            with hk.SendLabel(
                id="NonPaladinHealerHitKey2HealRaid",
                to=lbs_non_paladin_holy_healer,
            ) as send_label:
                CAN.KEY_2()

            # 奶骑, 用位于 2 号键位上的一键治疗宏奶团
            with hk.SendLabel(
                id="PaladinHealerHitKey2HealRaid",
                to=lbs_non_paladin_holy_healer,
            ) as send_label:
                act.Target.TARGET_RAID()
                CAN.KEY_2()

    def build_act2(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act2()
