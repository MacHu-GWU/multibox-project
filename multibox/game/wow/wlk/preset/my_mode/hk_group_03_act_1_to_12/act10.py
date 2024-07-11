# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TL, TC
import multibox.game.wow.wlk.preset.my_act.api as act
from multibox.game.wow.wlk.preset.my_mode.utils import TargetEnum

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class Act10Mixin:
    """
    todo: docstring
    """

    def build_default_act10(self: "Mode"):
        """
        See :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="Key0",
            key=KN.SCROLOCK_ON(KN.KEY_0),
        ) as self.hk_0_short_term_buff:
            # DK 吹号角
            with hk.SendLabel(
                id=TC.dk.name,
                to=self.get_lbs_by_tc(TC.dk),
            ):
                act.DK.Horn_of_Winter()

            # 奶骑补道标
            for lb in self.get_lbs_paladin_holy():
                char = self.get_char_by_label(lb)
                if char.is_tank_1_beacon_paladin:
                    with hk.SendLabel(to=[lb]):
                        self.target_tank_1_key_maker()
                        act.PaladinHoly.Beacon_of_Light()
                if char.is_tank_2_beacon_paladin:
                    with hk.SendLabel(to=[lb]):
                        self.target_tank_2_key_maker()
                        act.PaladinHoly.Beacon_of_Light()

            # 恢复萨上水盾
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.ShamanRestoration.Water_Shield()

            # 牧师上心灵之火
            with hk.SendLabel(
                id=TC.priest.name,
                to=self.get_lbs_by_tc(TC.priest),
            ):
                act.Priest.Inner_Fire()

    def build_act10(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act10()
