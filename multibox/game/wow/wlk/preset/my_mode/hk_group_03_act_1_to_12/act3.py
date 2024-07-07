# -*- coding: utf-8 -*-

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
import multibox.game.wow.wlk.api as wlk
import multibox.game.wow.wlk.preset.my_act.api as act


if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class Act3Mixin:
    def build_default_act3(self: "Mode"):
        with hk.Hotkey(
            id="Key3",
            key=KN.SCROLOCK_ON(KN.KEY_3),
        ) as self.hk_3:
            self.build_tank_default_action(key=KN.KEY_3)
            self.build_dps_default_action(key=KN.KEY_3)

            # 先获得所有可能在这个组里的治疗职业的 Label, 然后根据人数, 天赋给它们分配任务
            # 先分配任务的最高的最后 append, 放在队尾, 方便 pop
            lbs_tank_healer = self.lbs_tank_healer
            lbs_paladin_holy = self.lbs_paladin_holy
            lbs_non_paladin_tank_healer = lbs_tank_healer.difference(lbs_paladin_holy)

            # 确保有人奶 1 号坦克.
            if self.lb_tank1:
                if len(lbs_non_paladin_tank_healer):
                    self.is_tank1_has_healer = True
                    lb = lbs_non_paladin_tank_healer.pop()
                    with hk.SendLabel(
                        id="FastHealTank1",
                        to=[lb],
                    ):
                        self.target_tank_1_key_maker()
                        CAN.KEY_3()
                else:
                    # 如果没有人奶 1 号坦克, 团队中又还有空闲的奶骑,
                    # 那么第一个空闲的奶骑负责给 1 号坦克道标
                    if len(lbs_paladin_holy):
                        self.is_tank1_has_beacon = True
                        lb = lbs_paladin_holy.pop()
                        with hk.SendLabel(
                            id="HolyPaladinPeriodicalBeaconOnTank1",
                            to=[lb],
                        ):
                            self.target_tank_1_key_maker()
                            CAN.KEY_3()

            # 如果有 2 号坦克, 就尝试派人去奶
            if self.lb_tank2:
                if len(lbs_non_paladin_tank_healer):
                    self.is_tank2_has_healer = True
                    lb = lbs_non_paladin_tank_healer.pop()
                    with hk.SendLabel(
                        id="FastHealTank2",
                        to=[lb],
                    ):
                        self.target_tank_2_key_maker()
                        CAN.KEY_3()
                else:
                    # 如果没有人奶 2 号坦克, 团队中又还有空闲的奶骑,
                    # 那么第一个空闲的奶骑负责给 2 号坦克道标
                    if len(lbs_paladin_holy):
                        self.is_tank2_has_beacon = True
                        lb = lbs_paladin_holy.pop()
                        with hk.SendLabel(
                            id="HolyPaladinPeriodicalBeaconOnTank2",
                            to=[lb],
                        ):
                            self.target_tank_1_key_maker()
                            CAN.KEY_3()

            # 此时如果团队中有坦克, 或者有奶骑, 那么那么坦克身上的道标肯定是已经分配好了,
            # 之后如果还有奶骑 (概率不大, 团队中大概率不会有超过 2 个奶骑), 那么就平均分配
            # 给 tank 上道标
            tank_pairs_cycle = self.get_tank_pairs_cycle()
            for ind, lb in enumerate(lbs_paladin_holy, start=1):
                lb, key_maker = next(tank_pairs_cycle)
                with hk.SendLabel(
                    id=f"ExtractHolyPaladin{ind}BeaconOnTank{lb}",
                    to=[lb],
                ):
                    key_maker()
                    CAN.KEY_3()

            # 神牧, 随机给团上恢复
            lbs_priest_holy = lbs_non_paladin_tank_healer.intersection(
                self.lbs_priest_holy
            )
            if len(lbs_priest_holy):
                lb = lbs_priest_holy.pop()
                with hk.SendLabel(
                    id="HolyPriestHealRaid",
                    to=[lb],
                ):
                    act.PriestHoly.MB_HEAL_RAID()

            # 戒律牧, 随机给团上盾
            lbs_priest_disco = lbs_non_paladin_tank_healer.intersection(
                self.lbs_priest_disco
            )
            if len(lbs_priest_disco):
                lb = lbs_priest_disco.pop()
                lbs_non_paladin_tank_healer.remove(lb)
                with hk.SendLabel(
                    id="DiscoPriestHealRaid",
                    to=[lb],
                ):
                    act.PriestDiscipline.MB_HEAL_RAID()

            # 如果还有其他治疗没活干, 那么它们也帮着治疗焦点
            if len(lbs_non_paladin_tank_healer):
                with hk.SendLabel(
                    id="RestOfHealerHealFocus",
                    to=lbs_non_paladin_tank_healer,
                ):
                    act.Target.TARGET_FOCUS()
                    CAN.KEY_3()

    def build_act3(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act3()
