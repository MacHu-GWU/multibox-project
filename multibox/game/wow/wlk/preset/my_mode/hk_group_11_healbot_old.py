# -*- coding: utf-8 -*-

"""
实现由在主控角色界面下, 用鼠标在团队框架上进行单机来实现治疗的快捷键.
需要配合团队框架 Healbot 插件使用.
"""

import typing as T

from ordered_set import OrderedSet
from hotkeynet import api as hk
from hotkeynet.api import KN, CAN
from hotkeynet import utils

from multibox.game.wow.wlk.api import TalentCategory as TC
from ..my_act import api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


class HotkeyGroup11HealbotOld:
    """
    todo: docstring.
    """

    def build_hk_healbot_small_heal(self: "Mode"):
        """
        **说明**

        在 Leader 角色的窗口内用鼠标选择团队框架上的角色, 然后按住 Ctrl + 左键点击, 可以让
        跟随者中的治疗职业对其施放治疗量较低的技能, 并且让其他 Tank 和 DPS 继续正常打怪.
        这样可以实现在 Leader 的窗口内对指定目标进行治疗.

        **使用方法**

        按就行了.

        **动作条安排**

        todo
        """
        with hk.Hotkey(
            id="Healbot Small Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.MOUSE_LButton)),
        ) as self.hk_healbot_small_heal:
            id = "Healbot Small Heal {talent}"
            # healer
            self.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.PaladinHoly.HB_Flash_of_Light,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.ShamanRestoration.HB_Riptide,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.DruidRestoration.HB_Rejuvenation,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    # 套盾救命, 给其他治疗争取时间
                    act.PriestDiscipline.HB_Power_Word_Shield,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.PriestHoly.HB_Flash_Heal,
                ],
                id=id,
            )
            # other
            self.build_send_label_by_tc(
                tc=TC.tank,
                funcs=[
                    CAN.KEY_2,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.dps,
                funcs=[
                    act.Target.TARGET_FOCUS_TARGET,
                    CAN.KEY_2,
                ],
                id=id,
            )

    def build_hk_healbot_big_heal(self: "Mode"):
        """
        **说明**

        在 Leader 角色的窗口内用鼠标选择团队框架上的角色, 然后按住 Ctrl + 右键点击, 可以让
        跟随者中的治疗职业对其施放治疗量较高的技能, 并且让其他 Tank 和 DPS 继续正常打怪.
        这样可以实现在 Leader 的窗口内对指定目标进行治疗.

        **使用方法**

        按就行了.

        **动作条安排**

        todo
        """
        with hk.Hotkey(
            id="Healbot Big Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.MOUSE_RButton)),
        ) as self.hk_healbot_big_heal:
            id = "Healbot Big Heal {talent}"
            # healer
            self.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.PaladinHoly.HB_Holy_Light,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.ShamanRestoration.HB_Healing_Wave,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.DruidRestoration.HB_Nourish,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    # 套盾救命, 给其他治疗争取时间
                    act.PriestDiscipline.HB_Power_Word_Shield,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.PriestHoly.HB_Flash_Heal,
                ],
                id=id,
            )
            # other
            self.build_send_label_by_tc(
                tc=TC.tank,
                funcs=[
                    CAN.KEY_2,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.dps,
                funcs=[
                    act.Target.TARGET_FOCUS_TARGET,
                    CAN.KEY_2,
                ],
                id=id,
            )

    def build_hk_healbot_aoe_heal(self: "Mode"):
        """
        **说明**

        在 Leader 角色的窗口内用鼠标选择团队框架上的角色, 然后按住 Ctrl Alt + 左键点击, 可以让
        跟随者中的治疗职业对其施放需要指定目标的群体治疗技能, 并且让其他 Tank 和 DPS 继续正常打怪.
        这样可以实现在 Leader 的窗口内对指定目标进行治疗.

        **使用方法**

        按就行了.

        **动作条安排**

        todo
        """
        with hk.Hotkey(
            id="Healbot Aoe Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_ALT_(KN.MOUSE_LButton)),
        ) as self.hk_healbot_aoe_heal:
            id = "Healbot Aoe Heal {talent}"
            # healer
            self.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.PaladinHoly.HB_Holy_Light,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.ShamanRestoration.HB_Chain_Heal_for_mbox,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.DruidRestoration.HB_Wild_Growth,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    # 套盾救命, 给其他治疗争取时间
                    act.PriestDiscipline.HB_Power_Word_Shield,
                ],
                id=id,
            )
            self.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.PriestHoly.HB_Circle_of_Healing,
                ],
                id=id,
            )
            # other
            self.build_send_label_by_tc(
                tc=TC.tank,
                funcs=[
                    CAN.KEY_2,
                ],
                id=id,
            )

            lbs_dps = self.get_lbs_by_tc(TC.dps)
            lbs_shaman = self.get_lbs_by_tc(TC.shaman)
            lbs_non_shaman_dps = lbs_dps.difference(lbs_shaman)
            with hk.SendLabel(
                id="Healbot Aoe Heal non shaman dps",
                to=lbs_non_shaman_dps,
            ):
                act.Target.TARGET_FOCUS_TARGET()
                CAN.KEY_2()

    def build_hk_healbot_dispel(self: "Mode"):
        """
        **说明**

        在 Leader 角色的窗口内用鼠标选择团队框架上的角色, 然后按住 Ctrl Alt + 右键点击, 可以让
        跟随者中有驱散技能的职业对其施放驱散, 并且让其他 Tank 和 DPS 继续正常打怪.
        这样可以实现在 Leader 的窗口内对指定目标进行驱散.

        分配任务的逻辑是:

        1. DPS 优先于 Healer 优先于 Tank.
        2. 先让 魔法, 诅咒, 中毒, 疾病 每一种都至少有一个人驱散. 其他多余的人可以继续 DPS,
            也可以随机选择团队成员驱散.

        **使用方法**

        按就行了.

        **动作条安排**

        todo
        """
        with hk.Hotkey(
            id="Healbot Dispel",
            key=KN.SCROLOCK_ON(KN.CTRL_ALT_(KN.MOUSE_RButton)),
        ) as self.hk_healbot_dispel:
            id = "Healbot Dispel {talent}"
            lbs_paladin_dps = self.get_lbs_by_tc(TC.paladin_dps)
            lbs_paladin_healer = self.get_lbs_by_tc(TC.paladin_healer)
            lbs_paladin_tank = self.get_lbs_by_tc(TC.paladin_tank)
            lbs_shaman_dps = self.get_lbs_by_tc(TC.shaman_dps)
            lbs_shaman_resto = self.get_lbs_by_tc(TC.shaman_resto)
            lbs_druid_balance = self.get_lbs_by_tc(TC.druid_balance)
            lbs_druid_resto = self.get_lbs_by_tc(TC.druid_resto)
            lbs_mage = self.get_lbs_by_tc(TC.mage)
            lbs_priest_shadow = self.get_lbs_by_tc(TC.priest_shadow)
            lbs_priest_healer = self.get_lbs_by_tc(TC.priest_healer)

            lbs_all = OrderedSet.union(
                lbs_paladin_dps,
                lbs_paladin_healer,
                # lbs_paladin_tank, # tank 尽量不要负责驱散, 除非迫不得已
                lbs_shaman_dps,
                lbs_shaman_resto,
                lbs_druid_balance,
                lbs_druid_resto,
                lbs_mage,
                lbs_priest_shadow,
                lbs_priest_healer,
            )
            # 下面的优先级都是经过精心设计过的
            lbs_dispel_magic = OrderedSet.union(
                lbs_paladin_tank,
                lbs_paladin_healer,
                lbs_priest_healer,
                lbs_priest_shadow,
                lbs_paladin_dps,
            )
            lb_to_dispel_magic_spell_mapping = dict()
            for lb in lbs_paladin_dps | lbs_paladin_healer | lbs_paladin_tank:
                lb_to_dispel_magic_spell_mapping[lb] = act.Paladin.HB_Cleanse
            for lb in lbs_priest_healer | lbs_priest_shadow:
                lb_to_dispel_magic_spell_mapping[lb] = act.Priest.HB_Dispel_Magic

            lbs_dispel_curse = OrderedSet.union(
                lbs_shaman_resto,
                lbs_druid_resto,
                lbs_druid_balance,
                lbs_mage,
            )
            lb_to_dispel_curse_spell_mapping = dict()
            for lb in lbs_shaman_resto:
                lb_to_dispel_curse_spell_mapping[lb] = act.Shaman.HB_Cleanse_Spirit
            for lb in lbs_druid_resto | lbs_druid_balance:
                lb_to_dispel_curse_spell_mapping[lb] = act.Druid.HB_Remove_Curse
            for lb in lbs_mage:
                lb_to_dispel_curse_spell_mapping[lb] = act.Mage.HB_Remove_Curse

            lbs_dispel_poison = OrderedSet.union(
                lbs_paladin_tank,
                lbs_paladin_healer,
                lbs_shaman_resto,
                lbs_druid_resto,
                lbs_druid_balance,
                lbs_shaman_dps,
                lbs_paladin_dps,
            )
            lb_to_dispel_poison_spell_mapping = dict()
            for lb in lbs_paladin_tank | lbs_paladin_healer | lbs_paladin_dps:
                lb_to_dispel_poison_spell_mapping[lb] = act.Paladin.HB_Cleanse
            for lb in lbs_shaman_resto:
                lb_to_dispel_poison_spell_mapping[lb] = act.Shaman.HB_Cleanse_Spirit
            for lb in lbs_druid_resto | lbs_druid_balance:
                lb_to_dispel_poison_spell_mapping[lb] = act.Druid.HB_Abolish_Poison
            for lb in lbs_shaman_dps:
                lb_to_dispel_poison_spell_mapping[lb] = act.Shaman.HB_Cure_Toxins

            lbs_dispel_disease = OrderedSet.union(
                lbs_paladin_tank,
                lbs_paladin_healer,
                lbs_shaman_resto,
                lbs_priest_healer,
                lbs_priest_shadow,
                lbs_shaman_dps,
                lbs_paladin_dps,
            )
            lbs_assigned = OrderedSet()
            lb_to_dispel_disease_spell_mapping = dict()
            for lb in lbs_paladin_tank | lbs_paladin_healer | lbs_paladin_dps:
                lb_to_dispel_disease_spell_mapping[lb] = act.Paladin.HB_Cleanse
            for lb in lbs_shaman_resto:
                lb_to_dispel_disease_spell_mapping[lb] = act.Shaman.HB_Cleanse_Spirit
            for lb in lbs_priest_healer | lbs_priest_shadow:
                lb_to_dispel_disease_spell_mapping[lb] = act.Priest.HB_Abolish_Disease
            for lb in lbs_shaman_dps:
                lb_to_dispel_disease_spell_mapping[lb] = act.Shaman.HB_Cure_Toxins

            # 魔法
            lbs_dispel_magic = lbs_dispel_magic.difference(lbs_assigned)
            if len(lbs_dispel_magic):
                lb = lbs_dispel_magic.pop()
                lbs_assigned.add(lb)
                with hk.SendLabel(
                    id="Healbot Dispel Magic",
                    to=[lb],
                ):
                    lb_to_dispel_magic_spell_mapping[lb]()

            # 诅咒
            lbs_dispel_curse = lbs_dispel_curse.difference(lbs_assigned)
            if len(lbs_dispel_curse):
                lb = lbs_dispel_curse.pop()
                lbs_assigned.add(lb)
                with hk.SendLabel(
                    id="Healbot Dispel Curse",
                    to=[lb],
                ):
                    lb_to_dispel_curse_spell_mapping[lb]()

            # 中毒
            lbs_dispel_poison = lbs_dispel_poison.difference(lbs_assigned)
            if len(lbs_dispel_poison):
                lb = lbs_dispel_poison.pop()
                lbs_assigned.add(lb)
                with hk.SendLabel(
                    id="Healbot Dispel Poison",
                    to=[lb],
                ):
                    lb_to_dispel_poison_spell_mapping[lb]()

            # 疾病
            lbs_dispel_disease = lbs_dispel_disease.difference(lbs_assigned)
            if len(lbs_dispel_disease):
                lb = lbs_dispel_disease.pop()
                lbs_assigned.add(lb)
                with hk.SendLabel(
                    id="Healbot Dispel Disease",
                    to=[lb],
                ):
                    lb_to_dispel_disease_spell_mapping[lb]()

            # 这个看你的团队, 如果 DPS 不吃紧, 可以让剩下的团队成员有驱散的尽量驱散
            lbs_all = lbs_all.difference(lbs_assigned)
            if len(lbs_all):
                with hk.SendLabel(
                    id="Healbot Random Dispel",
                    to=lbs_all,
                ):
                    act.Target.TARGET_RAID()
                    CAN.T()
            lbs_assigned.update(lbs_all)

            # other
            self._build_other_guy_do_your_job(
                lbs_assigned=lbs_assigned,
                id="Healbot non Dispel {role}",
            )

    def build_hk_healbot_innervate(self: "Mode"):
        """
        **说明**

        在 Leader 角色的窗口内用鼠标选择团队框架上的角色, 然后按住 Ctrl + 1 / 2 / 3,
        可以分别让 1, 2, 3 号德鲁伊给目标施放激活, 并且让其他 Tank 和 DPS 继续正常打怪.

        分配任务的逻辑是:

        鸟德优先于奶德优先于猫德. 熊德是 Tank, 不能变成人形态丢激活.

        **使用方法**

        按就行了.

        **动作条安排**

        todo
        """
        lbs_druid_balance = self.get_lbs_by_tc(TC.druid_balance)
        lbs_druid_resto = self.get_lbs_by_tc(TC.druid_resto)
        lbs_druid_cat = self.get_lbs_by_tc(TC.druid_cat)
        lbs_druid = OrderedSet.union(
            lbs_druid_cat,
            lbs_druid_resto,
            lbs_druid_balance,
        )

        lbs_assigned = OrderedSet()
        for i, key in [
            (1, KN.CTRL_NUMPAD_1),
            (2, KN.CTRL_NUMPAD_2),
            (3, KN.CTRL_NUMPAD_3),
        ]:
            if len(lbs_druid):
                lb = lbs_druid.pop()
                lbs_assigned.add(lb)
                with hk.Hotkey(
                    id=f"Healbot Innervate {i}",
                    key=KN.SCROLOCK_ON(key),
                ) as self.hk_healbot_innervate:
                    with hk.SendLabel(
                        id=f"Healbot Druid {i} cast innervate",
                        to=[lb],
                    ):
                        act.Druid.HB_Innervate()

        # other
        self._build_other_guy_do_your_job(
            lbs_assigned=lbs_assigned,
            id="Healbot Innervate {role}",
        )

    def build_hk_group_11_healbot_mixin_old(self: "Mode"):
        self.build_hk_healbot_small_heal()
        self.build_hk_healbot_big_heal()
        self.build_hk_healbot_aoe_heal()
        self.build_hk_healbot_dispel()
        self.build_hk_healbot_innervate()
