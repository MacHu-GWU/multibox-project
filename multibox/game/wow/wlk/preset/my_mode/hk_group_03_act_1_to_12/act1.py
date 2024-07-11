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


class Act1Mixin:
    """
    todo: docstring
    """

    def build_hk_default_act1(self: "Mode"):
        """
        See :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="Key1",
            key=KN.SCROLOCK_ON(KN.KEY_1),
        ) as self.hk_1:
            self.build_tank_default_action(key=KN.KEY_1)
            self.build_dps_default_action(key=KN.KEY_1)

            # 奶骑
            for lb in self.get_lbs_paladin_holy():
                char = self.get_char_by_label(lb)
                if char.is_tank_1_healer:
                    with hk.SendLabel(to=[lb]):
                        self.target_tank_1_key_maker()
                        CAN.KEY_1()
                elif char.is_tank_2_healer:
                    with hk.SendLabel(to=[lb]):
                        self.target_tank_2_key_maker()
                        CAN.KEY_1()
                else:
                    with hk.SendLabel(to=[lb]):
                        act.Target.TARGET_RAID()
                        CAN.KEY_1()

            # 奶萨, 奶德, 牧师
            shaman_resto_talents = TC.shaman_resto.talents
            druid_resto_talents = TC.druid_resto.talents
            priest_disco_talents = TC.priest_disco.talents
            priest_holy_talents = TC.priest_holy.talents
            for lb in (
                self.get_lbs_shaman_resto()
                | self.get_lbs_druid_resto()
                | self.get_lbs_priest_disco()
                | self.get_lbs_priest_holy()
            ):
                char = self.get_char_by_label(lb)
                if char.is_tank_1_healer:
                    with hk.SendLabel(to=[lb]):
                        self.target_tank_1_key_maker()
                        CAN.KEY_1()
                elif char.is_tank_2_healer:
                    with hk.SendLabel(to=[lb]):
                        self.target_tank_2_key_maker()
                        CAN.KEY_1()
                else:
                    # 如果你装备够好, 你可以让多余的人无脑刷团
                    if char.talent in (
                        shaman_resto_talents
                        | druid_resto_talents
                        | priest_disco_talents
                        | priest_holy_talents
                    ):
                        CAN.KEY_2()  # 无脑刷团

    def build_act1(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_act1()
