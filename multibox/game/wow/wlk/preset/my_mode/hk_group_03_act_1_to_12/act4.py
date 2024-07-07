# -*- coding: utf-8 -*-

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TL, TC
import multibox.game.wow.wlk.preset.my_act.api as act


if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class Act4Mixin:
    def build_default_act4(self: "Mode"):
        """
        Act 4 技能主要是周期性的补一些技能. 包括:

        1. 奶骑每 15 秒一次给焦点的目标 (boss) 补圣光审判.
        2. 奶萨每 30 秒一次给 tank 补大地之盾.
        3. 戒律牧和神牧每 15 秒一次给 tank 补愈合祷言.

        Tank 和 DPS 职业则自由正常拉怪打怪.

        See :ref:`wow-wlk-simulate-periodical-skill-casting`
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
                        id="HolyPaladinLightJudgementTank1Target",
                        to=[lb],
                    ):
                        self.target_tank_1_key_maker()
                        act.Target.ASSIST_TARGET()
                        act.PaladinHoly.MB_Periodical_Judgement_of_Light_on_Focus_Target_Macro()

            if len(lbs_paladin_holy):
                lb = lbs_paladin_holy.pop()
                if self.lb_tank2:
                    with hk.SendLabel(
                        id="HolyPaladinLightJudgementTank2Target",
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
                        id="RestoShamanPutEarthShieldOnTank1",
                        to=[lb],
                    ):
                        self.target_tank_1_key_maker()
                        act.ShamanRestoration.MB_Periodical_Refresh_Earth_Shield_on_Tank_Macro()

            if len(lbs_shaman_resto):
                lb = lbs_shaman_resto.pop()
                if self.lb_tank2:
                    with hk.SendLabel(
                        id="RestoShamanPutEarthShieldOnTank2",
                        to=[lb],
                    ):
                        self.target_tank_2_key_maker()
                        act.ShamanRestoration.MB_Periodical_Refresh_Earth_Shield_on_Tank_Macro()

            # 德鲁伊, 用位于 4 号键位上的一键治疗宏
            self._build_send_label_by_talent(
                talent=list(TC.druid_resto.talents),
                target=None,
                key=KN.KEY_4,
            )

            # 戒律牧 用位于 4 号键位上的按概率周期性给坦克上愈合祷言或苦修的宏
            label_list = self.lbs_by_tc(TC.priest_disco)
            if len(label_list) == 0:
                pass
            # 如果只有 1 个戒律牧, 则给焦点补愈合祷言
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id=TC.shaman_resto.name,
                    to=self.lbs_by_tc(TC.priest_disco),
                ):
                    act.Target.TARGET_FOCUS()
                    CAN.KEY_4()

            # 如果有 2 或 2 个以上的奶萨, 两个奶萨分别给两个 tank 的补大地之盾
            # 其他多余的奶萨什么也不做
            elif len(label_list) == 2:
                if self.lb_tank1:
                    with hk.SendLabel(
                        id="DiscoPriest1",
                        to=[label_list[0]],
                    ):
                        self.target_tank_1_key_maker()
                        CAN.KEY_4()
                if self.lb_tank2:
                    with hk.SendLabel(
                        id="DiscoPriest2",
                        to=[label_list[1]],
                    ):
                        self.target_tank_2_key_maker()
                        CAN.KEY_4()

    def build_act4(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act4()
