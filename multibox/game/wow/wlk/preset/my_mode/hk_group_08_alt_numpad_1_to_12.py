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


class HotkeyGroup08AltNumpad1To12Mixin:
    """
    todo: docstring.
    """

    def build_hk_alt_numpad_1_misdirect_and_mark(self: "Mode"):
        """
        **说明**

        在 Boss 战开怪时, 通常需要猎人给 Tank 误导, 然后前三下的毒蛇钉刺, 奇美拉射击,
        瞄准射击造成的大量仇恨会累计给 Tank, 使得开场就能建立足够的初始仇恨, 确保不会 OT.

        另外, 在开怪之前, 猎人应该给 Boss 上猎人标记增加受到的远程攻击伤害.

        这个按键就是用来完成这两个任务的.

        **使用方法**

        按 1 下就可以了.

        **动作条安排**

        - 动作条按钮上误导焦点宏.
        - 误导焦点宏按钮要绑定 ``Alt + Z`` 快捷键, 并确保跟 ``act.Hunter.Misdirection_Focus_Macro``
            中的定义一致. 猎人印记技能要绑定 ``Ctrl + G`` 快捷键, 并确保跟 ``act.Hunter.Hunter_s_Mark``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Numpad1 - 猎人误导坦克",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_1),
        ) as self.hk_alt_numpad_1_hunter_misdirect:
            with hk.SendLabel(
                id=f"Alt Numpad1 - 猎人误导坦克",
                to=self.get_lbs_by_tc(TC.hunter),
            ):
                # 一般上猎人印记时我们不能让猎人自动攻击, 开怪应该由 Tank 来开.
                # 先选择自己能确保之前右键点击 Boss 所产生的自动攻击被取消.
                act.Target.TARGET_SELF()
                act.Target.TARGET_FOCUS_TARGET()
                act.Hunter.Hunter_s_Mark()
                act.Hunter.Misdirection_Focus_Macro()

    def build_hk_alt_numpad_2_aspect_of_pact_or_hawk(self: "Mode"):
        """
        **说明**

        猎人在龙鹰守护和豹群守护 (全团提高移动速度) 之间切换.

        **使用方法**

        按 1 下就切换到下一个守护. 一直按就一直在两个守护之间切换

        **动作条安排**

        - 动作条按钮上是切换守护宏.
        - 动作条按钮要绑定 ``Shift + F`` 快捷键, 并确保跟 ``act.Hunter.Aspect_of_Pact_or_dragon_hawk``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Numpad2 - 猎人在雄鹰和豹群守护之间切换",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_2),
        ) as self.hk_alt_numpad_2_aspect_of_pact_or_hawk:
            with hk.SendLabel(
                id="Alt Numpad2 - 猎人在雄鹰和豹群守护之间切换",
                to=self.get_lbs_by_tc(TC.hunter),
            ):
                act.Hunter.Aspect_of_Pact_or_dragon_hawk()

    def build_hk_alt_numpad_3_aspect_of_viper_or_hawk(self: "Mode"):
        """
        **说明**

        猎人在龙鹰守护和蝮蛇守护 (回蓝) 之间切换.

        **使用方法**

        按 1 下就切换到下一个守护. 一直按就一直在两个守护之间切换

        **动作条安排**

        - 动作条按钮上是切换守护宏.
        - 动作条按钮要绑定 ``Shift + G`` 快捷键, 并确保跟 ``act.Hunter.Aspect_of_viper_or_dragon_hawk``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Numpad3 - 猎人在雄鹰和蝮蛇守护之间切换",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_3),
        ) as self.hk_alt_numpad_3_aspect_of_viper_or_hawk:
            with hk.SendLabel(
                id="Alt Numpad3 - 猎人在雄鹰和蝮蛇守护之间切换",
                to=self.get_lbs_by_tc(TC.hunter),
            ):
                act.Hunter.Aspect_of_viper_or_dragon_hawk()

    def build_hk_alt_numpad_4_all_boomkin_star_fall(self: "Mode"):
        """
        **说明**

        所有鸟德一起开星落.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上是星落技能.
        - 动作条按钮要绑定 ``Alt + F`` 快捷键, 并确保跟 ``act.DruidBalance.Starfall``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Numpad4 - 鸟德集体放星落",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_4),
        ) as self.hk_alt_numpad_4_all_boomkin_star_fall:
            with hk.SendLabel(
                id="Alt Numpad4 - 鸟德集体放星落",
                to=self.get_lbs_by_tc(TC.druid_balance),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.DruidBalance.Starfall()

    def build_hk_alt_numpad_5_all_dps_burst(self: "Mode"):
        """
        **说明**

        所有 DPS 一起开爆发性技能 (不包括萨满嗜血).

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上是一键开爆发技能宏.
        - 动作条按钮要绑定 ``Alt + D`` 快捷键, 并确保跟 ``act.General.DPS_BURST_MACRO_KEY_ALT_D``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Numpad5 - DPS 开爆发技能",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_5),
        ) as self.hk_alt_numpad_5_all_dps_burst:
            with hk.SendLabel(
                id="Alt Numpad5 - DPS 开爆发技能",
                to=self.get_lbs_by_tc(TC.dps),
            ):
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

    def build_hk_alt_numpad_6_all_dps_burst_and_hero(self: "Mode"):
        """
        **说明**

        所有 DPS 一起开爆发性技能, 并且包括萨满嗜血.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上是一键开爆发技能宏.
        - 动作条按钮要绑定 ``Alt + D`` 快捷键, 并确保跟 ``act.General.DPS_BURST_MACRO_KEY_ALT_D``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Numpad6 - 开嗜血, 同时所有 DPS 开爆发技能",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_6),
        ) as self.hk_alt_numpad_6_all_dps_burst_and_hero:
            with hk.SendLabel(
                id="Alt Numpad6 - 非萨满 DPS 开爆发技能",
                to=self.get_lbs_by_tc(TC.dps).difference(self.get_lbs_by_tc(TC.shaman)),
            ):
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

            with hk.SendLabel(
                id="Alt Numpad6 - 萨满 DPS 开爆发技能以及嗜血",
                to=self.get_lbs_by_tc(TC.shaman_elemental),
            ):
                act.Shaman.Bloodlust_or_Heroism()
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

            with hk.SendLabel(
                id="Alt Numpad6 - 萨满 治疗 开嗜血",
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
        **说明**

        所有萨满放净化图腾 (给小队驱 Debuff)

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上是净化图腾技能.
        - 动作条按钮要绑定 ``Alt + F2`` 快捷键, 并确保跟 ``act.Shaman.Cleansing_Totem``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Numpad10 - 萨满放清毒图腾",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_0),
        ) as self.hk_alt_numpad_10_cleansing_totem:
            with hk.SendLabel(
                id="Alt Numpad10 - 萨满放清毒图腾",
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.Cleansing_Totem()

    def build_hk_alt_numpad_11_tremor_totem(self: "Mode"):
        """
        **说明**

        所有萨满放战栗图腾 (给小队成员反恐惧)

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上是战栗图腾技能.
        - 动作条按钮要绑定 ``Alt + F1`` 快捷键, 并确保跟 ``act.Shaman.Tremor_Totem``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Numpad11 - 萨满放战栗图腾",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_11_DIVIDE),
        ) as self.hk_alt_numpad_11_tremor_totem:
            with hk.SendLabel(
                id="Alt Numpad11 - 萨满放战栗图腾",
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.Tremor_Totem()

    def build_hk_alt_numpad_12_earth_binding_totem(self: "Mode"):
        """
        **说明**

        所有萨满放地缚图腾 (范围减速)

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上是地缚图腾技能.
        - 动作条按钮要绑定 ``Shift + F`` 快捷键, 并确保跟 ``act.Shaman.Earthbind_Totem``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Numpad12 - 萨满放地缚图腾",
            key=KN.SCROLOCK_ON(KN.ALT_NUMPAD_12_MULTIPLY),
        ) as self.hk_alt_numpad_12_earth_binding_totem:
            with hk.SendLabel(
                id="Alt Numpad12 - 萨满放地缚图腾",
                to=self.get_lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.Earthbind_Totem()

    def build_hk_group_08_alt_numpad_1_to_12_mixin(self):
        self.build_hk_alt_numpad_1_misdirect_and_mark()
        self.build_hk_alt_numpad_2_aspect_of_pact_or_hawk()
        self.build_hk_alt_numpad_3_aspect_of_viper_or_hawk()
        self.build_hk_alt_numpad_4_all_boomkin_star_fall()
        self.build_hk_alt_numpad_5_all_dps_burst()
        self.build_hk_alt_numpad_6_all_dps_burst_and_hero()
        # self.build_hk_alt_numpad_7_8_9_first_raid_damage_reduction()
        self.build_hk_alt_numpad_10_cleansing_totem()
        self.build_hk_alt_numpad_11_tremor_totem()
        self.build_hk_alt_numpad_12_earth_binding_totem()
