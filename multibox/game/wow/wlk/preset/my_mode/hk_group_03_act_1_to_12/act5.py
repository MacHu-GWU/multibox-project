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


class Act5Mixin:
    """
    todo: docstring
    """

    def build_default_act5(self: "Mode"):
        """
        See :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="Key5",
            key=KN.SCROLOCK_ON(KN.KEY_5),
        ) as self.hk_5:
            # 奶骑对自己放圣光术
            lbs_paladin_non_tank = self.get_lbs_by_tc(TC.paladin_non_tank)
            if len(lbs_paladin_non_tank):
                with hk.SendLabel(to=lbs_paladin_non_tank):
                    act.Target.TARGET_SELF()
                    act.PaladinHoly.Holy_Light()

            # 萨满对自己放治疗链
            lbs_shaman = self.get_lbs_by_tc(TC.shaman)
            if len(lbs_shaman):
                with hk.SendLabel(to=lbs_shaman):
                    act.Target.TARGET_SELF()
                    act.Shaman.Chain_Heal()

            # 奶德对自己放野性生长
            lbs_druid_resto = self.get_lbs_by_tc(TC.druid_resto)
            if len(lbs_druid_resto):
                with hk.SendLabel(to=lbs_druid_resto):
                    act.Target.TARGET_SELF()
                    act.DruidRestoration.Wild_Growth()

            # 戒律牧放治疗祷言
            lbs_priest_healer = self.get_lbs_by_tc(TC.priest_healer)
            if len(lbs_priest_healer):
                with hk.SendLabel(to=lbs_priest_healer):
                    act.Target.TARGET_SELF()
                    act.Priest.Prayer_of_Healing()

            # 坦克正常打怪
            lbs_tank = self.get_lbs_by_tc(TC.tank)
            if len(lbs_tank):
                with hk.SendLabel(to=lbs_tank):
                    CAN.KEY_5()

            # 剩余没有被安排到的 DPS 跟着焦点打怪
            lbs_dps = self.get_lbs_by_tc(TC.dps)
            lbs_dps = lbs_dps.difference(
                lbs_paladin_non_tank,
                lbs_shaman,
                lbs_druid_resto,
                lbs_priest_healer,
                lbs_tank,
            )
            if len(lbs_dps):
                with hk.SendLabel(to=lbs_dps):
                    act.Target.TARGET_FOCUS_TARGET()
                    CAN.KEY_5()

    def build_act5(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act5()
