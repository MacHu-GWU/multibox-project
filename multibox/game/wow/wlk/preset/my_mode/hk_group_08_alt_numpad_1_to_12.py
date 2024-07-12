# -*- coding: utf-8 -*-

"""
实现 Alt + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
"""

import typing as T

from hotkeynet import api as hk
from hotkeynet.api import KN
from hotkeynet.utils import difference_list

from multibox.game.wow.wlk.api import TalentCategory as TC
from ..my_act import api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


class HotkeyGroup08AltNumpad1To12:
    """
    todo: docstring.
    """

    def build_hk_alt_numpad_1_misdirect_and_tot_focus(self: "Mode"):
        """
        todo: docstring.
        """
        with hk.Hotkey(
            id="Alt Numpad1 - 猎人误导坦克",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_1),
        ) as self.hk_alt_numpad_1_hunter_misdirect:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.get_lbs_by_tc(TC.hunter),
            ):
                act.Hunter.Misdirection_Focus_Macro()

    def build_hk_alt_numpad_2_aspect_of_pact_or_hawk(self: "Mode"):
        """
        todo: docstring.
        """
        with hk.Hotkey(
            id="Alt Numpad2 - 猎人在雄鹰和豹群守护之间切换",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_2),
        ) as self.hk_alt_numpad_2_aspect_of_pact_or_hawk:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.get_lbs_by_tc(TC.hunter),
            ):
                act.Hunter.Aspect_of_Pact_or_dragon_hawk()

    def build_hk_alt_numpad_3_aspect_of_viper_or_hawk(self: "Mode"):
        """
        todo: docstring.
        """
        with hk.Hotkey(
            id="Alt Numpad3 - 猎人在雄鹰和蝮蛇守护之间切换",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_3),
        ) as self.hk_alt_numpad_3_aspect_of_viper_or_hawk:
            with hk.SendLabel(
                name=TC.hunter.name,
                to=self.get_lbs_by_tc(TC.hunter),
            ):
                act.Hunter.Aspect_of_viper_or_dragon_hawk()

    def build_hk_alt_numpad_4_all_boomkin_star_fall(self: "Mode"):
        """
        todo: docstring.
        """
        with hk.Hotkey(
            id="Alt Numpad4 - 鸟德集体放星落",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_4),
        ) as self.hk_alt_numpad_4_all_boomkin_star_fall:
            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.get_lbs_by_tc(TC.druid_balance),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.DruidBalance.Starfall()

    def build_hk_alt_numpad_5_all_dps_burst(self: "Mode"):
        """
        todo: docstring.
        """
        with hk.Hotkey(
            id="Alt Numpad5 - DPS 开爆发技能",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_5),
        ) as self.hk_alt_numpad_5_all_dps_burst:
            with hk.SendLabel(
                id=TC.dps.name,
                to=self.get_lbs_by_tc(TC.dps),
            ):
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

    def build_hk_alt_numpad_6_all_dps_burst_and_hero(self: "Mode"):
        """
        todo: docstring.
        """
        with hk.Hotkey(
            id="Alt Numpad6 - 开嗜血, 同时所有 DPS 开爆发技能",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_6),
        ) as self.hk_alt_numpad_6_all_dps_burst_and_hero:
            with hk.SendLabel(
                id="all_non_shaman_dps",
                to=difference_list(
                    self.get_lbs_by_tc(TC.dps),
                    self.get_lbs_by_tc(TC.shaman),
                ),
            ):
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

            with hk.SendLabel(
                id=TC.shaman_elemental.name,
                to=self.get_lbs_by_tc(TC.shaman_elemental),
            ):
                act.Shaman.Bloodlust_or_Heroism()
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

            with hk.SendLabel(
                id=TC.shaman_resto.name,
                to=self.get_lbs_by_tc(TC.shaman_resto),
            ):
                act.Shaman.Bloodlust_or_Heroism()

    def build_hk_alt_numpad_7_8_9_first_raid_damage_reduction(self: "Mode"):
        """
        todo: docstring.
        """
        with hk.Hotkey(
            id="Alt Numpad7 - 放第一个神圣牺牲团队减伤技能",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_7),
        ) as self.hk_alt_numpad_7_raid_damage_reduction:
            with hk.SendLabel(
                id=TC.paladin_protect.name,
                to=self.get_lbs_by_tc(TC.paladin_protect),
            ):
                # 要点两下, 启动神圣牺牲后自己取消
                act.PaladinProtection.Divine_Sacrifice()
                act.PaladinProtection.Divine_Sacrifice()

        with hk.Hotkey(
            id="Alt Numpad8 - 放第二个神圣牺牲团队减伤技能",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_8),
        ) as self.hk_alt_numpad_8_raid_damage_reduction:
            with hk.SendLabel(
                id=TC.paladin_holy.name,
                to=self.get_lbs_by_tc(TC.paladin_holy),
            ):
                # 要点两下, 启动神圣牺牲后自己取消
                act.PaladinProtection.Divine_Sacrifice()
                act.PaladinProtection.Divine_Sacrifice()

        with hk.Hotkey(
            id="Alt Numpad9 - 放第三个神圣牺牲团队减伤技能",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_9),
        ) as self.hk_alt_numpad_9_raid_damage_reduction:
            with hk.SendLabel(
                id=TC.paladin_holy.name,
                to=self.get_lbs_by_tc(TC.paladin_holy),
            ):
                act.PaladinHoly.Aura_Mastery()

    def build_hk_alt_numpad_10_cleansing_totem(self: "Mode"):
        """
        todo: docstring.
        """
        with hk.Hotkey(
            id="Alt Numpad10 - 萨满放清毒图腾",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_0),
        ) as self.hk_alt_numpad_10_cleansing_totem:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.Cleansing_Totem()

    def build_hk_alt_numpad_11_tremor_totem(self: "Mode"):
        """
        todo: docstring.
        """
        with hk.Hotkey(
            id="Alt Numpad11 - 萨满放战栗图腾",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_11_DIVIDE),
        ) as self.hk_alt_numpad_11_tremor_totem:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.Tremor_Totem()

    def build_hk_alt_numpad_12_earth_binding_totem(self: "Mode"):
        """
        todo: docstring.
        """
        with hk.Hotkey(
            id="Alt Numpad12 - 萨满放地缚图腾",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_12_MULTIPLY),
        ) as self.hk_alt_numpad_12_earth_binding_totem:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.Earthbind_Totem()

    def build_hk_group_08_alt_numpad_1_to_12_mixin(self):
        self.build_hk_alt_numpad_1_misdirect_and_tot_focus()
        self.build_hk_alt_numpad_2_aspect_of_pact_or_hawk()
        self.build_hk_alt_numpad_3_aspect_of_viper_or_hawk()
        self.build_hk_alt_numpad_4_all_boomkin_star_fall()
        self.build_hk_alt_numpad_5_all_dps_burst()
        self.build_hk_alt_numpad_6_all_dps_burst_and_hero()
        # self.build_hk_alt_numpad_7_8_9_first_raid_damage_reduction()
        self.build_hk_alt_numpad_10_cleansing_totem()
        self.build_hk_alt_numpad_11_tremor_totem()
        self.build_hk_alt_numpad_12_earth_binding_totem()
