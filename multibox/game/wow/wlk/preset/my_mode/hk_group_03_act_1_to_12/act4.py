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


class Act4Mixin:
    """
    todo: docstring
    """

    def build_default_act4(self: "Mode"):
        """
        Act 4 技能主要是周期性的补一些技能. 包括:

        1. 奶骑每 15 秒一次给焦点的目标 (boss) 补圣光审判.
        2. 奶萨每 30 秒一次给 tank 补大地之盾.
        3. 戒律牧和神牧每 15 秒一次给 tank 补愈合祷言.

        Tank 和 DPS 职业则自由正常拉怪打怪.

        Ref:

        - :ref:`wow-wlk-simulate-periodical-skill-casting`
        - :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="Key4",
            key=KN.SCROLOCK_ON(KN.KEY_4),
        ) as self.hk_4:
            self.build_tank_default_action(key=KN.KEY_4)
            self.build_dps_default_action(key=KN.KEY_4)

            # 奶骑给焦点的目标补圣光审判
            lbs_paladin_holy = self.lbs_paladin_holy

            if len(lbs_paladin_holy):
                lb = lbs_paladin_holy.pop()
                if self.lb_tank1:
                    with hk.SendLabel(
                        id="Key4-HolyPaladinLightJudgementTank1Target",
                        to=[lb],
                    ):
                        self.target_tank_1_key_maker()
                        act.Target.ASSIST_TARGET()
                        act.PaladinHoly.MB_Periodical_Judgement_of_Light_on_Focus_Target_Macro()

            if len(lbs_paladin_holy):
                lb = lbs_paladin_holy.pop()
                if self.lb_tank2:
                    with hk.SendLabel(
                        id="Key4-HolyPaladinLightJudgementTank2Target",
                        to=[lb],
                    ):
                        self.target_tank_2_key_maker()
                        act.Target.ASSIST_TARGET()
                        act.PaladinHoly.MB_Periodical_Judgement_of_Light_on_Focus_Target_Macro()

            # 奶萨 用位于 4 号键位上的按概率周期性给坦克上大地之盾的宏
            lbs_shaman_resto = self.lbs_shaman_resto

            if len(lbs_shaman_resto):
                lb = lbs_shaman_resto.pop()
                if self.lb_tank1:
                    with hk.SendLabel(
                        id="Key4-RestoShamanPutEarthShieldOnTank1",
                        to=[lb],
                    ):
                        self.target_tank_1_key_maker()
                        act.ShamanRestoration.MB_Periodical_Refresh_Earth_Shield_on_Tank_Macro()

            if len(lbs_shaman_resto):
                lb = lbs_shaman_resto.pop()
                if self.lb_tank2:
                    with hk.SendLabel(
                        id="Key4-RestoShamanPutEarthShieldOnTank2",
                        to=[lb],
                    ):
                        self.target_tank_2_key_maker()
                        act.ShamanRestoration.MB_Periodical_Refresh_Earth_Shield_on_Tank_Macro()

            # 德鲁伊, 用位于 4 号键位上的一键治疗宏
            lbs_druid_resto = self.lbs_druid_resto
            if len(lbs_druid_resto):
                with hk.SendLabel(
                    id="Key4-RestoDruidHealRaid",
                    to=lbs_druid_resto,
                ):
                    act.DruidRestoration.MB_HEAL_RAID_KEY_4()

            # 戒律牧和神牧, 用位于 4 号键位上的一键治疗宏
            lbs_priest_healer = self.get_lbs_by_tc(TC.priest_healer)
            if len(lbs_priest_healer):
                with hk.SendLabel(
                    id="Key4-PriestHealRaid",
                    to=lbs_priest_healer,
                ):
                    CAN.KEY_4()

            # tank_pairs_cycle = self.get_tank_pairs_cycle()
            # lbs_priest_healer = self.get_lbs_by_tc(TC.priest.healer)
            # for ith, lb_healer in enumerate(lbs_priest_healer, start=1):
            #     lb_tank, key_maker = next(tank_pairs_cycle)
            #     with hk.SendLabel(
            #         id=f"Key4-{ith}PriestHealerPutPrayerOfMendingOnTank{lb_tank}",
            #         to=[lb_healer],
            #     ):
            #         key_maker()
            #         act.Priest.MB_HEAL_RAID()
            #
            #
            # label_list = self.get_lbs_by_tc(TC.priest_disco)
            # if len(label_list) == 0:
            #     pass
            # # 如果只有 1 个戒律牧, 则给焦点补愈合祷言
            # elif len(label_list) == 1:
            #     with hk.SendLabel(
            #         id=TC.shaman_resto.name,
            #         to=self.get_lbs_by_tc(TC.priest_disco),
            #     ):
            #         act.Target.TARGET_FOCUS()
            #         CAN.KEY_4()
            #
            # # 如果有 2 或 2 个以上的奶萨, 两个奶萨分别给两个 tank 的补大地之盾
            # # 其他多余的奶萨什么也不做
            # elif len(label_list) == 2:
            #     if self.lb_tank1:
            #         with hk.SendLabel(
            #             id="DiscoPriest1",
            #             to=[label_list[0]],
            #         ):
            #             self.target_tank_1_key_maker()
            #             CAN.KEY_4()
            #     if self.lb_tank2:
            #         with hk.SendLabel(
            #             id="DiscoPriest2",
            #             to=[label_list[1]],
            #         ):
            #             self.target_tank_2_key_maker()
            #             CAN.KEY_4()

    def build_act4(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act4()
