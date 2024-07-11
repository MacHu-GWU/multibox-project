# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TL, TC
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

            # 奶骑
            for lb in self.get_lbs_paladin_holy():
                with hk.SendLabel(to=[lb]):
                    act.Target.TARGET_RAID()
                    CAN.KEY_2()

            # 奶萨, 奶德, 牧师
            for lb in (
                self.get_lbs_shaman_resto()
                | self.get_lbs_druid_resto()
                | self.get_lbs_priest_disco()
                | self.get_lbs_priest_holy()
            ):
                char = self.get_char_by_label(lb)
                if char.is_raid_healer:
                    with hk.SendLabel(to=[lb]):
                        CAN.KEY_2()

    def build_act2(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act2()
