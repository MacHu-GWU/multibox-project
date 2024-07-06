# -*- coding: utf-8 -*-

"""
实现各种特殊 Boss 战时候的特定快捷键 S. 例如鸟德星落, 鸟德吹风, 法师打断, 等等.
"""

import typing as T
import itertools

from hotkeynet import api as hk
from hotkeynet.api import KN, CAN

from multibox.game.wow.wlk.api import TalentCategory as TC
from ..my_act import api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


class HotkeyGroup12SpecialMixin:
    def build_icc_boss1(self: "Mode"):
        with hk.Hotkey(
            id="Shift + Z",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.Z)),
        ) as self.hk_shift_z:
            lbs_shaman = self.lbs_by_tc(TC.shaman)
            with hk.SendLabel(
                to=list(lbs_shaman),
            ):
                act.Target.TARGET_RAID()
                act.Shaman.Chain_Heal()

            lbs_paladin_holy = self.lbs_by_tc(TC.paladin_holy)
            with hk.SendLabel(
                to=list(lbs_paladin_holy),
            ):
                act.Target.TARGET_RAID()
                act.PaladinHoly.Holy_Light()

            lbs_druid_resto = self.lbs_by_tc(TC.druid_resto)
            with hk.SendLabel(
                to=list(lbs_druid_resto),
            ):
                act.DruidRestoration.MB_HEAL_RAID()

            lbs_priest_healer = self.lbs_by_tc(TC.priest_healer)
            with hk.SendLabel(
                to=list(lbs_priest_healer),
            ):
                act.PriestHoly.Prayer_of_Healing()

            lbs_non_shaman_dps = self.lbs_by_tc(TC.dps).difference(lbs_shaman)
            with hk.SendLabel(
                to=list(lbs_non_shaman_dps),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                CAN.KEY_2()

            lbs_tank = self.lbs_by_tc(TC.tank)
            with hk.SendLabel(
                to=list(lbs_tank),
            ):
                CAN.KEY_2()

        # with hk.Hotkey(
        #     id="Shift + T",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.T)),
        # ) as self.hk_shift_t:
        #     with hk.SendLabel(
        #         to=self.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift + X",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.X)),
        # ) as self.hk_shift_x:
        #     with hk.SendLabel(
        #         to=self.lbs_all,
        #     ):
        #         hk.Key.trigger()

    def build_hk_group_12_mixin(self: "Mode"):
        if "icc_boss1" in self.name:
            self.build_icc_boss1()
