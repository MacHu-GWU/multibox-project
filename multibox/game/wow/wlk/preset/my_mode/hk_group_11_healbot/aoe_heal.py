# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TC
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class HealBotAoeHealMixin:
    """
    todo: docstring
    """

    def build_hk_default_healbot_aoe_heal(self: "Mode"):
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

    def build_healbot_aoe_heal(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_healbot_aoe_heal()
