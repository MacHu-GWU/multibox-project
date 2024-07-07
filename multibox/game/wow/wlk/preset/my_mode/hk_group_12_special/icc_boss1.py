# -*- coding: utf-8 -*-

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TL, TC
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class IccBoss1Mixin:
    def build_icc_boss1(self: "Mode"):
        # 所有 DPS 点杀骸骨尖刺
        # Shift + V 按钮上必须放点杀 /target 骸骨尖刺 的宏
        with hk.Hotkey(
            id="V",
            key=KN.SCROLOCK_ON(KN.V),
        ) as self.hk_v:
            lbs_shaman_resto = self.lbs_by_tc(TC.shaman_resto)
            with hk.SendLabel(
                to=list(lbs_shaman_resto),
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

            lbs_dps = self.lbs_by_tc(TC.dps)
            with hk.SendLabel(
                to=list(lbs_dps),
            ):
                CAN.SHIFT_Z()
                CAN.KEY_2()

            lbs_tank = self.lbs_by_tc(TC.tank)
            with hk.SendLabel(
                to=list(lbs_tank),
            ):
                CAN.KEY_2()


        with hk.Hotkey(
            id="Shift + X",
            key=KN.SCROLOCK_ON(KN.SHIFT_X),
        ) as self.hk_shift_x:
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
