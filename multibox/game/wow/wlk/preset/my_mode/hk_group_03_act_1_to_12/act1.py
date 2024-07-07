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


class Act1Mixin:
    """
    todo: docstring
    """
    def build_default_act1(self: "Mode"):
        """
        See :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="Key1",
            key=KN.SCROLOCK_ON(KN.KEY_1),
        ) as self.hk_1:
            self.build_tank_default_action(key=KN.KEY_1)
            self.build_dps_default_action(key=KN.KEY_1)

            lbs_tank_healer = self.lbs_tank_healer
            lbs_paladin_holy = self.lbs_paladin_holy
            lbs_non_paladin_tank_healer = lbs_tank_healer.difference(lbs_paladin_holy)
            lbs_other_healer = lbs_non_paladin_tank_healer  # make var name shorter

            # 确保有人奶 1 号坦克.
            if self.lb_tank1:
                if len(lbs_other_healer):
                    lb = lbs_other_healer.pop()
                    with hk.SendLabel(
                        id="SlowHealTank1",
                        to=[lb],
                    ):
                        self.target_tank_1_key_maker()
                        CAN.KEY_1()

            # 如果有 2 号坦克, 就尝试派人去奶
            if self.lb_tank2:
                if len(lbs_other_healer):
                    lb = lbs_other_healer.pop()
                    with hk.SendLabel(
                        id="SlowHealTank2",
                        to=[lb],
                    ):
                        self.target_tank_2_key_maker()
                        CAN.KEY_1()

            # 如果还有空闲的戒律牧, 则随机给团上盾
            # 如果团队中没有奶德奶萨, 则在前面的逻辑里, 戒律牧会被分配去奶 tank 了
            lbs_priest_disco = lbs_tank_healer.intersection(self.lbs_priest_disco)
            if len(lbs_priest_disco):
                lb = lbs_priest_disco.pop()
                lbs_tank_healer.remove(lb)
                with hk.SendLabel(
                    id="DiscoPriestHealRaid",
                    to=[lb],
                ):
                    act.PriestDiscipline.MB_HEAL_RAID()

            # 如果还有空闲的神牧, 则随机给团上恢复
            # 如果团队中没有奶德奶萨, 则在前面的逻辑里, 神牧会被分配去奶 tank 了
            lbs_priest_holy = lbs_other_healer.intersection(self.lbs_priest_holy)
            if len(lbs_priest_holy):
                lb = lbs_priest_holy.pop()
                with hk.SendLabel(
                    id="HolyPriestHealRaid",
                    to=[lb],
                ):
                    act.PriestHoly.MB_HEAL_RAID()

            # 奶骑, 随机奶团, 因为道标一般已经打给坦克了, 所以奶团的同时肯定也是在奶坦克的
            lbs_paladin_holy = lbs_tank_healer.intersection(self.lbs_paladin_holy)
            if len(lbs_paladin_holy):
                lbs_tank_healer.difference_update(lbs_paladin_holy)
                with hk.SendLabel(
                    id="HolyPaladinHealRaid",
                    to=lbs_paladin_holy,
                ):
                    act.Target.TARGET_RAID()
                    act.PaladinHoly.MB_One_Minute_Heal_Rotation_Macro_copy_1()

            # 如果还有其他治疗没活干, 那么它们也帮着治疗 Tank
            if len(lbs_tank_healer):
                tank_pairs_cycle = self.get_tank_pairs_cycle()
                for ind, lb in enumerate(lbs_tank_healer, start=1):
                    lb, key_maker = next(tank_pairs_cycle)
                    with hk.SendLabel(
                        id=f"ExtractHealer{ind}HealTank{lb}",
                        to=[lb],
                    ):
                        key_maker()
                        CAN.KEY_1()

    def build_act1(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act1()
