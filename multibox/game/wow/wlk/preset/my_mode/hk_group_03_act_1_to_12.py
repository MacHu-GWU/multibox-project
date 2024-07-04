# -*- coding: utf-8 -*-

"""
实现按键 1-12 的功能.
"""

import typing as T

from ordered_set import OrderedSet
from hotkeynet import api as hk
from hotkeynet.api import KN, CAN

from multibox.game.wow.wlk.api import Talent as TL, TalentCategory as TC
from ..my_act import api as act


if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


class HotkeyGroup03Act1To12Mixin:
    def _get_send_label_by_id(
        self: "Mode",
        id_: str,
        blocks: T.Iterable[hk.SendLabel],
    ) -> T.Optional[hk.SendLabel]:
        for block in blocks:
            if isinstance(block, hk.SendLabel):
                if block.id == id_:
                    return block
        return None

    def build_actions_default(
        self: "Mode",
        key: str,
        healer_target_nothing: bool = False,
        healer_target_focus: bool = False,
        healer_target_focus_target: bool = False,
        healer_target_self: bool = False,
        healer_target_party: bool = False,
        healer_target_raid: bool = False,
    ) -> T.List[hk.SendLabel]:
        """
        通常情况下, 我们打怪的逻辑是: 坦克拉怪, DPS 输出, 治疗奶. 而我们有那么多键位. 为了
        避免为那么多键位写一大堆重复代码, 我们定义了一个工厂函数, 用于生成默认的设置.
        简单来说默认设置就是:

        1. 坦克对当前选择的怪施放技能
        2. DPS 对焦点的目标释放技能
        3. 治疗 对某个目标释放技能, 这里的 "某个" 取决于哪个模式. 请参考下面的参数定义:

        :param healer_target_nothing: 在施放治疗技能前不选择目标
        :param healer_target_focus: 治疗前 (下同), 先选定焦点, 通常是坦克司机
        :param healer_target_focus_target: 先选择焦点的目标, 通常是坦克选择队友然后治疗该队友
        :param healer_target_self: 先选择自己
        :param healer_target_party: 先用宏随机选定小队成员
        :param healer_target_raid: 先用宏随机选择团队成员

        以上 5 个模式中必须选择其中的一个.

        **注**

        这里我们需要为所有的 Active Characters 的每一个特定的天赋创建一个 SendLabel 对象.
        这和我们之前为一类 TalentCategory 创建一个 SendLabel, 然后在 SendLabel.to
        里面指定多个 label 的模式不同. 虽然后者从代码的角度讲更加紧凑, 但是却丧失了之后为
        每个特定的天赋在特殊场景下指定不同的行为的能力. 所以我们才用的这种不符合直觉的写法.
        """
        if (
            sum(
                [
                    healer_target_nothing,
                    healer_target_focus,
                    healer_target_focus_target,
                    healer_target_self,
                    healer_target_party,
                    healer_target_raid,
                ]
            )
            != 1
        ):
            raise ValueError()

        send_label_list = list()

        # Tank
        for talent in TC.tank.talents:
            with hk.SendLabel(
                id=talent.name,
                to=self.lbs_by_tl(talent),
            ) as send_label:
                hk.Key.make(key)
                send_label_list.append(send_label)

        # DPS
        for talent in TC.dps.talents:
            with hk.SendLabel(
                id=talent.name,
                to=self.lbs_by_tl(talent),
            ) as send_label:
                act.Target.TARGET_FOCUS_TARGET()
                hk.Key.make(key)
                send_label_list.append(send_label)

        # Healer
        for talent in TC.healer.talents:
            with hk.SendLabel(
                id=talent.name,
                to=self.lbs_by_tl(talent),
            ) as send_label:
                if healer_target_nothing:
                    hk.Key.make(key)
                elif healer_target_focus:
                    act.Target.TARGET_FOCUS()
                    hk.Key.make(key)
                elif healer_target_focus_target:
                    act.Target.TARGET_FOCUS_TARGET()
                    hk.Key.make(key)
                elif healer_target_self:
                    act.Target.TARGET_SELF()
                    hk.Key.make(key)
                elif healer_target_party:
                    act.Target.TARGET_PARTY()
                    hk.Key.make(key)
                elif healer_target_raid:
                    act.Target.TARGET_RAID()
                    hk.Key.make(key)
                else:  # pragma: no cover
                    raise NotImplementedError

                send_label_list.append(send_label)

        return send_label_list

    def _build_send_label_by_talent(
        self: "Mode",
        talent: T.Union[TL, T.List[TL]],
        target: T.Optional[T.Union[T.Callable, T.List[T.Callable]]],
        key: str,
    ) -> T.List[hk.SendLabel]:
        send_label_list: T.List[hk.SendLabel] = list()
        if isinstance(talent, TL):
            talent_list: T.List[TL] = [talent]
        else:
            talent_list: T.List[TL] = talent

        if target is None:
            target_list: T.List[T.Callable] = []
        elif isinstance(target, list):
            target_list: T.List[T.Callable] = target
        else:
            target_list: T.List[T.Callable] = [target]

        for talent in talent_list:
            with hk.SendLabel(
                id=talent.name,
                to=self.lbs_by_tl(talent),
            ) as send_label:
                for target in target_list:
                    target()
                hk.Key.make(key)
                send_label_list.append(send_label)

        return send_label_list

    def _build_default_tank_action(self: "Mode", key: str) -> T.List[hk.SendLabel]:
        return self._build_send_label_by_talent(
            talent=list(TC.tank.talents),
            target=list(),
            key=key,
        )

    def _build_default_dps_action(self: "Mode", key: str) -> T.List[hk.SendLabel]:
        return self._build_send_label_by_talent(
            talent=list(TC.dps.talents),
            target=act.Target.TARGET_FOCUS_TARGET,
            key=key,
        )

    def build_hk_1_heal_tank(self: "Mode"):
        with hk.Hotkey(
            id="Key1",
            key=KN.SCROLOCK_ON(KN.KEY_1),
        ) as self.hk_1:
            self._build_default_tank_action(key=KN.KEY_1)
            self._build_default_dps_action(key=KN.KEY_1)

            # 先获得所有可能在这个组里的治疗职业的 Label, 然后根据人数, 天赋给它们分配任务
            # 先分配任务的最高的最后 append, 放在队尾, 方便 pop
            lbs_healer = OrderedSet()
            lbs_healer.update(self.lbs_paladin_holy)
            lbs_healer.update(self.lbs_priest_disco)
            lbs_healer.update(self.lbs_priest_holy)
            lbs_healer.update(self.lbs_shaman_resto)
            lbs_healer.update(self.lbs_druid_resto)

            # 确保有人奶 1 号坦克.
            if len(lbs_healer):
                lb = lbs_healer.pop()
                with hk.SendLabel(
                    id="SlowHealLeader1",
                    to=[lb],
                ):
                    self.target_leader_1()
                    CAN.KEY_1()

            # 如果有 2 号坦克, 就尝试派人去奶
            if self.lb_leader2:
                if len(lbs_healer):
                    lb = lbs_healer.pop()
                    with hk.SendLabel(
                        id="SlowHealLeader2",
                        to=[lb],
                    ):
                        self.target_leader_2()
                        CAN.KEY_1()

            # 神牧, 随机给团上恢复
            lbs_priest_holy = lbs_healer.intersection(self.lbs_priest_holy)
            if len(lbs_priest_holy):
                lb = lbs_priest_holy.pop()
                with hk.SendLabel(
                    id="HolyPriestHealRaid",
                    to=[lb],
                ):
                    act.PriestHoly.MB_HEAL_RAID()

            # 戒律牧, 随机给团上盾
            lbs_priest_disco = lbs_healer.intersection(self.lbs_priest_disco)
            if len(lbs_priest_disco):
                lb = lbs_priest_disco.pop()
                lbs_healer.remove(lb)
                with hk.SendLabel(
                    id="DiscoPriestHealRaid",
                    to=[lb],
                ):
                    act.PriestDiscipline.MB_HEAL_RAID()

            # 奶骑, 随机奶团, 因为道标的存在, 它肯定也是在奶坦克的
            lbs_paladin_holy = lbs_healer.intersection(self.lbs_paladin_holy)
            if len(lbs_paladin_holy):
                lbs_healer.difference_update(lbs_paladin_holy)
                with hk.SendLabel(
                    id="HolyPaladinHealRaid",
                    to=lbs_paladin_holy,
                ):
                    act.Target.TARGET_RAID()
                    act.PaladinHoly.One_Minute_Heal_Rotation_Macro_copy_1()

            # 如果还有其他治疗没活干, 那么它们也帮着治疗焦点
            if len(lbs_healer):
                with hk.SendLabel(
                    id="RestOfHealerHealFocus",
                    to=lbs_healer,
                ):
                    act.Target.TARGET_FOCUS()
                    CAN.KEY_1()

    def build_hk_2_heal_nothing(self: "Mode"):
        with hk.Hotkey(
            id="Key2",
            key=KN.SCROLOCK_ON(KN.KEY_2),
        ) as self.hk_2:
            self._build_default_tank_action(key=KN.KEY_2)
            self._build_default_dps_action(key=KN.KEY_2)

            # 德鲁伊, 萨满, 戒律牧, 神圣牧师 用位于 2 号键位上的一键治疗宏
            self._build_send_label_by_talent(
                talent=list(
                    TC.druid_resto.talents
                    | TC.shaman_resto.talents
                    | TC.priest_disco.talents
                    | TC.priest_holy.talents
                ),
                target=None,
                key=KN.KEY_2,
            )
            # 奶骑, 随机奶团
            self._build_send_label_by_talent(
                talent=list(TC.paladin_holy.talents),
                target=act.Target.TARGET_RAID,
                key=KN.KEY_2,
            )

    def build_hk_3_heal_tank(self: "Mode"):
        with hk.Hotkey(
            id="Key3",
            key=KN.SCROLOCK_ON(KN.KEY_3),
        ) as self.hk_3:
            self._build_default_tank_action(key=KN.KEY_3)
            self._build_default_dps_action(key=KN.KEY_3)

            # 先获得所有可能在这个组里的治疗职业的 Label, 然后根据人数, 天赋给它们分配任务
            # 先分配任务的最高的最后 append, 放在队尾, 方便 pop
            lbs_healer = OrderedSet()
            lbs_healer.update(self.lbs_priest_disco)
            lbs_healer.update(self.lbs_priest_holy)
            lbs_healer.update(self.lbs_shaman_resto)
            lbs_healer.update(self.lbs_druid_resto)

            lbs_paladin_holy = self.lbs_paladin_holy

            # 确保有人奶 1 号坦克.
            if len(lbs_healer):
                lb = lbs_healer.pop()
                with hk.SendLabel(
                    id="FastHealLeader1",
                    to=[lb],
                ):
                    self.target_leader_1()
                    CAN.KEY_3()

            if len(lbs_paladin_holy):
                lb = lbs_paladin_holy.pop()
                with hk.SendLabel(
                    id="HolyPaladinBeaconOnLeader1",
                    to=[lb],
                ):
                    self.target_leader_1()
                    hk.Key.make(KN.KEY_3)

            # 如果有 2 号坦克, 就尝试派人去奶
            if self.lb_leader2:
                if len(lbs_healer):
                    lb = lbs_healer.pop()
                    with hk.SendLabel(
                        id="FastHealLeader2",
                        to=[lb],
                    ):
                        self.target_leader_2()
                        CAN.KEY_3()

                if len(lbs_paladin_holy):
                    lb = lbs_paladin_holy.pop()
                    with hk.SendLabel(
                        id="HolyPaladinBeaconOnLeader2",
                        to=[lb],
                    ):
                        self.target_leader_1()
                        hk.Key.make(KN.KEY_3)

            # 神牧, 随机给团上恢复
            lbs_priest_holy = lbs_healer.intersection(self.lbs_priest_holy)
            if len(lbs_priest_holy):
                lb = lbs_priest_holy.pop()
                with hk.SendLabel(
                    id="HolyPriestHealRaid",
                    to=[lb],
                ):
                    act.PriestHoly.MB_HEAL_RAID()

            # 戒律牧, 随机给团上盾
            lbs_priest_disco = lbs_healer.intersection(self.lbs_priest_disco)
            if len(lbs_priest_disco):
                lb = lbs_priest_disco.pop()
                lbs_healer.remove(lb)
                with hk.SendLabel(
                    id="DiscoPriestHealRaid",
                    to=[lb],
                ):
                    act.PriestDiscipline.MB_HEAL_RAID()

            # 奶骑, 随机奶团, 因为道标的存在, 它肯定也是在奶坦克的
            lbs_paladin_holy = lbs_healer.intersection(self.lbs_paladin_holy)
            if len(lbs_paladin_holy):
                lbs_healer.difference_update(lbs_paladin_holy)
                with hk.SendLabel(
                    id="HolyPaladinHealRaid",
                    to=lbs_paladin_holy,
                ):
                    act.Target.TARGET_RAID()
                    act.PaladinHoly.One_Minute_Heal_Rotation_Macro_copy_1()

            # 如果还有其他治疗没活干, 那么它们也帮着治疗焦点
            if len(lbs_healer):
                with hk.SendLabel(
                    id="RestOfHealerHealFocus",
                    to=lbs_healer,
                ):
                    act.Target.TARGET_FOCUS()
                    CAN.KEY_3()

    def build_hk_4_heal_nothing(self: "Mode"):
        with hk.Hotkey(
            id="Key4",
            key=KN.SCROLOCK_ON(KN.KEY_4),
        ) as self.hk_4:
            self._build_default_tank_action(key=KN.KEY_4)
            self._build_default_dps_action(key=KN.KEY_4)

            # 奶骑给焦点的目标补圣光审判
            label_list = self.lbs_by_tc(TC.paladin_healer)
            if len(label_list) == 0:
                pass
            # 如果只有 1 个奶骑, 则给焦点的目标补圣光审判
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id=TC.paladin_healer.name,
                    to=self.lbs_by_tc(TC.paladin_healer),
                ):
                    act.Target.TARGET_FOCUS_TARGET()
                    hk.Key.make(KN.KEY_4)
            # 如果有 2 或 2 个以上的奶骑, 两个奶骑分别给两个 leader 的目标补圣光审判
            elif len(label_list) == 2:
                with hk.SendLabel(
                    id="HolyPaladin1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.target_leader_1()
                    act.Target.ASSIST_TARGET()
                    hk.Key.make(KN.KEY_4)
                with hk.SendLabel(
                    id="HolyPaladin2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.target_leader_2()
                    act.Target.ASSIST_TARGET()
                    hk.Key.make(KN.KEY_4)
                with hk.SendLabel(
                    id="HolyPaladin3andAbove",
                    to=label_list[2:],
                ):
                    act.Target.TARGET_FOCUS_TARGET()
                    hk.Key.make(KN.KEY_4)

            # 奶萨 用位于 4 号键位上的按概率周期性给坦克上大地之盾的宏
            label_list = self.lbs_by_tc(TC.shaman_resto)
            if len(label_list) == 0:
                pass
            # 如果只有 1 个奶萨, 则给焦点补大地之盾
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id=TC.shaman_resto.name,
                    to=self.lbs_by_tc(TC.shaman_resto),
                ):
                    act.Target.TARGET_FOCUS()
                    hk.Key.make(KN.KEY_4)

            # 如果有 2 或 2 个以上的奶萨, 两个奶萨分别给两个坦克补大地之盾
            # 其他多余的奶萨什么也不做
            elif len(label_list) == 2:
                with hk.SendLabel(
                    id="RestoShaman1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.target_leader_1()
                    hk.Key.make(KN.KEY_4)
                with hk.SendLabel(
                    id="RestoShaman2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.target_leader_2()
                    hk.Key.make(KN.KEY_4)

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
                    hk.Key.make(KN.KEY_4)

            # 如果有 2 或 2 个以上的奶萨, 两个奶萨分别给两个 leader 的补大地之盾
            # 其他多余的奶萨什么也不做
            elif len(label_list) == 2:
                with hk.SendLabel(
                    id="DiscoPriest1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.target_leader_1()
                    hk.Key.make(KN.KEY_4)
                with hk.SendLabel(
                    id="DiscoPriest2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.target_leader_2()
                    hk.Key.make(KN.KEY_4)

    def build_hk_5_aoe_heal_self(self: "Mode"):
        with hk.Hotkey(
            id="Key5",
            key=KN.SCROLOCK_ON(KN.KEY_5),
        ) as self.hk_5:
            send_label_list = self.build_actions_default(
                key=KN.KEY_5,
                healer_target_focus_target=True,  # 选择 焦点的目标
            )

            # 奶骑对自己放圣光术
            send_label = self._get_send_label_by_id(
                id_=TL.paladin_pve_holy.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.Target.TARGET_SELF(),
                    act.PaladinHoly.Holy_Light(),
                ]

            # 奶萨对自己放治疗链
            send_label = self._get_send_label_by_id(
                id_=TL.shaman_pve_resto.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.Target.TARGET_SELF(),
                    act.Shaman.Chain_Heal(),
                ]

            # 奶德对自己放野性生长
            send_label = self._get_send_label_by_id(
                id_=TL.druid_pve_resto.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.Target.TARGET_SELF(),
                    act.DruidRestoration.Wild_Growth(),
                ]

            # 戒律牧放治疗祷言
            send_label = self._get_send_label_by_id(
                id_=TL.priest_pve_disco.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.PriestDiscipline.Prayer_of_Healing(),
                ]

            # 神圣牧放治疗祷言
            send_label = self._get_send_label_by_id(
                id_=TL.priest_pve_holy.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.PriestHoly.Prayer_of_Healing(),
                ]

    def build_hk_6_one_time_debuff(self: "Mode"):
        with hk.Hotkey(
            id="Key6",
            key=KN.SCROLOCK_ON(KN.KEY_6),
        ) as self.hk_6:
            send_label_list = self.build_actions_default(
                key=KN.KEY_6,
                healer_target_focus_target=True,  # 选择 焦点
            )

    def build_hk_7(self: "Mode"):
        with hk.Hotkey(
            id="Key7",
            key=KN.SCROLOCK_ON(KN.KEY_7),
        ) as self.hk_7:
            send_label_list = self.build_actions_default(
                key=KN.KEY_7,
                healer_target_focus_target=True,  # 选择 焦点
            )

    def build_hk_8_buff_self(self: "Mode"):
        with hk.Hotkey(
            id="Key8",
            key=KN.SCROLOCK_ON(KN.KEY_8),
        ) as self.hk_8:
            with hk.SendLabel(
                id="all",
                to=self.lbs_all,
            ):
                hk.Key(key=KN.KEY_8)

    def build_hk_9_buff_raid(self: "Mode"):
        with hk.Hotkey(
            id="Key9",
            key=KN.SCROLOCK_ON(KN.KEY_9),
        ) as self.hk_9:
            with hk.SendLabel(
                id="all",
                to=self.lbs_all,
            ):
                hk.Key(key=KN.KEY_9)

    def build_hk_0_short_term_buff(self: "Mode"):
        """
        补刷持续时间短的 Buff.
        """
        with hk.Hotkey(
            id="Key0",
            key=KN.SCROLOCK_ON(KN.KEY_0),
        ) as self.hk_0_short_term_buff:
            # DK 吹号角
            with hk.SendLabel(
                id=TC.dk.name,
                to=self.lbs_by_tc(TC.dk),
            ):
                act.DK.Horn_of_Winter()

            # 奶骑 上道标, 这里稍微有点复杂
            label_list = self.lbs_by_tc(TC.paladin_healer)
            if len(label_list) == 0:
                pass
            # 如果只有 1 个奶骑, 则给焦点加圣光道标
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id=TC.paladin_healer.name,
                    to=self.lbs_by_tc(TC.paladin_healer),
                ):
                    act.Target.TARGET_FOCUS()
                    act.PaladinHoly.Beacon_of_Light()
            # 如果有 2 或 2 个以上的奶骑, 两个奶骑分别给两个 leader 加圣光道标
            # 其他的奶骑给焦点加圣光道标
            elif len(label_list) == 2:
                with hk.SendLabel(
                    id="HolyPaladin1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.target_leader_1()
                    act.PaladinHoly.Beacon_of_Light()
                with hk.SendLabel(
                    id="HolyPaladin2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.target_leader_2()
                    act.PaladinHoly.Beacon_of_Light()
                with hk.SendLabel(
                    id="HolyPaladin3andAbove",
                    to=label_list[2:],
                ):
                    act.Target.TARGET_FOCUS()
                    act.PaladinHoly.Beacon_of_Light()

            # 恢复萨上水盾
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.lbs_by_tc(TC.shaman),
            ):
                act.ShamanRestoration.Water_Shield()

            # 术士上邪甲
            with hk.SendLabel(
                id=TC.warlock.name,
                to=self.lbs_by_tc(TC.warlock),
            ):
                act.Warlock.Fel_Armor()

            # 牧师上心灵之火
            with hk.SendLabel(
                id=TC.priest.name,
                to=self.lbs_by_tc(TC.priest),
            ):
                act.Priest.Inner_Fire()

    def build_hk_11_focus_mode_1(self: "Mode"):
        """
        所有人的焦点设置为它们的 1 号司机 (除了司机本人)
        """
        with hk.Hotkey(
            id="SetFocusMode1",
            key=KN.SCROLOCK_ON(KN.KEY_11_MINUS),
        ) as self.hk_11_focus_mode_1:
            for char in self.active_chars:
                if char.is_leader_1:  # 司机本人清除焦点
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[char.window.label],
                    ):
                        act.General.CLEAR_FOCUS_NUMPAD_7()
                else:  # 其他人设置焦点
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[char.window.label],
                    ):
                        self.target_leader_key_mapper[char.leader_1_window.label]()
                        act.General.SET_FOCUS_KEY_NUMPAD_6()

    def build_hk_12_focus_mode_2(self: "Mode"):
        """
        所有人的焦点设置为它们的 2 号司机 (除了司机本人)
        """
        with hk.Hotkey(
            id="SetFocusMode2",
            key=KN.SCROLOCK_ON(KN.KEY_12_PLUS),
        ) as self.hk_12_focus_mode_2:
            for char in self.active_chars:
                if char.is_leader_2:  # 司机本人清除焦点
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[char.window.label],
                    ):
                        act.General.CLEAR_FOCUS_NUMPAD_7()
                else:  # 其他人设置焦点
                    with hk.SendLabel(
                        name=char.account.username,
                        to=[char.window.label],
                    ):
                        self.target_leader_key_mapper[char.leader_2_window.label]()
                        act.General.SET_FOCUS_KEY_NUMPAD_6()

    # # --- alt 1,2,3,4,5
    def build_hk_alt_5(self: "Mode"):
        """
        对自己放大型群刷技能.
        """
        with hk.Hotkey(
            id="Alt 5",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.KEY_5)),
        ) as self.hk_alt_5:
            with hk.SendLabel(
                id=TC.priest_holy.name,
                to=self.lbs_by_tc(tc=TC.priest_holy),
            ):
                act.Target.TARGET_SELF()
                act.Priest.Circle_of_Healing()

            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.lbs_by_tc(tc=TC.shaman),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.Shaman.Chain_Heal()

    def build_hk_group_03_act_1_to_12_mixin(self):
        self.build_hk_1_heal_tank()
        self.build_hk_2_heal_nothing()
        self.build_hk_3_heal_tank()
        self.build_hk_4_heal_nothing()
        self.build_hk_5_aoe_heal_self()
        self.build_hk_6_one_time_debuff()
        self.build_hk_7()
        self.build_hk_8_buff_self()
        self.build_hk_9_buff_raid()
        self.build_hk_0_short_term_buff()
        self.build_hk_11_focus_mode_1()
        self.build_hk_12_focus_mode_2()

        self.build_hk_alt_5()
