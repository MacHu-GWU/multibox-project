# -*- coding: utf-8 -*-

import typing as T
from itertools import cycle

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
import multibox.game.wow.wlk.api as wlk
import multibox.game.wow.wlk.preset.my_act.api as act


if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class Act1Mixin:
    def build_default_act1(self: "Mode"):
        with hk.Hotkey(
            id="Key1",
            key=KN.SCROLOCK_ON(KN.KEY_1),
        ) as self.hk_1:
            self.build_tank_default_action(key=KN.KEY_1)
            self.build_dps_default_action(key=KN.KEY_1)

            lbs_tank_healer = self.lbs_tank_healer

            # 确保有人奶 1 号坦克.
            if self.lb_tank1:
                if len(lbs_tank_healer):
                    lb = lbs_tank_healer.pop()
                    with hk.SendLabel(
                        id="SlowHealTank1",
                        to=[lb],
                    ):
                        self.target_tank_1_key_maker()
                        CAN.KEY_1()

            # 如果有 2 号坦克, 就尝试派人去奶
            if self.lb_tank2:
                if len(lbs_tank_healer):
                    lb = lbs_tank_healer.pop()
                    with hk.SendLabel(
                        id="SlowHealTank2",
                        to=[lb],
                    ):
                        self.target_tank_2_key_maker()
                        CAN.KEY_1()

            # 如果还有空闲的神牧, 则随机给团上恢复
            lbs_priest_holy = lbs_tank_healer.intersection(self.lbs_priest_holy)
            if len(lbs_priest_holy):
                lb = lbs_priest_holy.pop()
                with hk.SendLabel(
                    id="HolyPriestHealRaid",
                    to=[lb],
                ):
                    # 注: 这里是第一次出现这种模式, 以后也会有很多地方用到这种模式,
                    # 所以我在这里说明一下为什么这么实现
                    # 这里的业务逻辑其实是人类按 1 (在其他地方就是按其他键), 所有窗口
                    # 也跟着按 1. todo, 把这段话放在 act2 去说
                    act.PriestHoly.MB_HEAL_RAID()

            # 如果还有空闲的戒律牧, 则随机给团上盾
            lbs_priest_disco = lbs_tank_healer.intersection(self.lbs_priest_disco)
            if len(lbs_priest_disco):
                lb = lbs_priest_disco.pop()
                lbs_tank_healer.remove(lb)
                with hk.SendLabel(
                    id="DiscoPriestHealRaid",
                    to=[lb],
                ):
                    act.PriestDiscipline.MB_HEAL_RAID()

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
                tank_pairs: T.List[T.Tuple[str, hk.KeyMaker]] = list()
                if self.lb_tank1:
                    tank_pairs.append((self.lb_tank1, self.target_tank_1_key_maker))
                if self.lb_tank2:
                    tank_pairs.append((self.lb_tank2, self.target_tank_2_key_maker))
                tank_pairs_cycle = cycle(tank_pairs)
                for ind, lb in enumerate(lbs_tank_healer, start=1):
                    lb, key_maker = next(tank_pairs_cycle)
                    with hk.SendLabel(
                        id=f"ExtractHealer{ind}HealTank{lb}",
                        to=[lb],
                    ):
                        key_maker()
                        CAN.KEY_1()

            print(self.hk_1.blocks)

    def build_act1(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act1()
