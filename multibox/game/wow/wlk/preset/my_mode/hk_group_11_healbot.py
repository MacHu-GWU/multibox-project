# -*- coding: utf-8 -*-

"""
实现由在主控角色界面下, 用鼠标在团队框架上进行单机来实现治疗的快捷键.
需要配合团队框架 Healbot 插件使用.
"""

import typing as T

from hotkeynet import api as hk
from hotkeynet.api import KN, CAN
from hotkeynet import utils

from multibox.game.wow.wlk.api import TalentCategory as TC
from ..my_act import api as act

if T.TYPE_CHECKING: # pragma: no cover
    from .mode import Mode


class HotkeyGroup11Healbot:
    def _build_send_label_non_shaman_dps(self: "Mode"):
        """
        点击 Healbot 的时候, 所有 DPS 继续攻击焦点的目标. 唯独 增强萨满 和 元素萨满 例外.
        虽然它们是 DPS 职业, 但是依然要跟其他治疗一样, 对团队框架目标使用治疗链.
        """
        lbs_dps = self.lbs_by_tc(TC.dps)
        lbs_shaman_non_resto = self.lbs_by_tc(TC.shaman_non_resto)
        to = utils.difference_list(lbs_dps, lbs_shaman_non_resto)
        with hk.SendLabel(
            id="non_shaman_dps",
            to=to,
        ) as send_label:
            act.Target.TARGET_FOCUS_TARGET()
            hk.Key(key=KN.KEY_2)
            return send_label

    def build_hk_healbot_small_heal(self: "Mode"):
        with hk.Hotkey(
            id="Healbot Small Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.MOUSE_LButton)),
        ) as self.hk_healbot_small_heal:
            self.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.PaladinHoly.HB_Flash_of_Light,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.ShamanRestoration.HB_Riptide,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.DruidRestoration.HB_Rejuvenation,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    act.PriestDiscipline.HB_Power_Word_Shield,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.PriestHoly.HB_Flash_Heal,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.tank,
                funcs=[
                    CAN.KEY_2,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.dps,
                funcs=[
                    act.Target.TARGET_FOCUS_TARGET,
                    CAN.KEY_2,
                ],
            )

    def build_hk_healbot_big_heal(self: "Mode"):
        with hk.Hotkey(
            id="Healbot Big Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.MOUSE_RButton)),
        ) as self.hk_healbot_big_heal:
            self.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.PaladinHoly.HB_Holy_Light,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.ShamanRestoration.HB_Healing_Wave,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.DruidRestoration.HB_Nourish,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    act.PriestDiscipline.HB_Power_Word_Shield,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.PriestHoly.HB_Flash_Heal,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.tank,
                funcs=[
                    CAN.KEY_2,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.dps,
                funcs=[
                    act.Target.TARGET_FOCUS_TARGET,
                    CAN.KEY_2,
                ],
            )

    def build_hk_healbot_aoe_heal(self: "Mode"):
        with hk.Hotkey(
            id="Healbot Aoe Heal",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.MOUSE_LButton)),
        ) as self.hk_healbot_aoe_heal:
            self.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.PaladinHoly.HB_Holy_Light,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.ShamanRestoration.HB_Chain_Heal_for_mbox,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.DruidRestoration.HB_Wild_Growth,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    act.PriestDiscipline.HB_Power_Word_Shield,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.PriestHoly.HB_Circle_of_Healing,
                ],
            )
            # 不要发送 key 到 坦克 和 DPS. 因为这个时候如果主窗口是 坦克 或 DPS,
            # 那么此时按着 SHIFT, 然后 HotkeyNEt 又发了个 1 或者 2, 就会切换动作条了
            # self.build_send_label_by_tc(
            #     tc=TC.tank,
            #     funcs=[
            #         CAN.KEY_2,
            #     ],
            # )
            self._build_send_label_non_shaman_dps(),

    def build_hk_healbot_dispel(self: "Mode"):
        with hk.Hotkey(
            id="Healbot Dispel",
            key=KN.SCROLOCK_ON(KN.MOUSE_MButton),
        ) as self.hk_healbot_dispel:
            self.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.PaladinHoly.HB_Cleanse,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.ShamanRestoration.HB_Cleanse_Spirit,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.DruidRestoration.HB_Remove_Curse,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    act.PriestDiscipline.Dispel_Magic,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.PriestHoly.Dispel_Magic,
                ],
            )
            self.build_send_label_by_tc(
                tc=TC.tank,
                funcs=[
                    CAN.KEY_2,
                ],
            )
            self._build_send_label_non_shaman_dps(),

    def build_hk_group_11_healbot_mixin(self: "Mode"):
        self.build_hk_healbot_small_heal()
        self.build_hk_healbot_big_heal()
        self.build_hk_healbot_aoe_heal()
        self.build_hk_healbot_dispel()
