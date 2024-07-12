# -*- coding: utf-8 -*-

"""
实现 Ctrl + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
"""

import typing as T

from hotkeynet import api as hk
from hotkeynet.api import KN

from multibox.game.wow.wlk.api import TalentCategory as TC
from ..my_act import api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


class HotkeyGroup09CtrlNumpad1To12:
    """
    todo: docstring.
    """

    # def build_hk_ctrl_numpad_1_silence_shot_focus_target(self: "Mode"):
    #     """
    #     todo: docstring
    #     """
    #     with hk.Hotkey(
    #         id="Ctrl Numpad1 - 射击猎人对焦点的目标释放沉默射击",
    #         key=KN.SCROLOCK_ON(KN.CTRL_NUMPAD_1),
    #     ) as self.hk_ctrl_numpad_1:
    #         with hk.SendLabel(
    #             id=TC.hunter.name,
    #             to=self.get_lbs_by_tc(TC.hunter),
    #         ):
    #             act.Target.TARGET_FOCUS_TARGET()
    #             act.Hunter.Silencing_Shot()
    #
    # def build_hk_ctrl_numpad_2_counter_spell_focus_target(self: "Mode"):
    #     """
    #     todo: docstring
    #     """
    #     with hk.Hotkey(
    #         id="Ctrl Numpad2 - 法师对焦点的目标释放法术反制",
    #         key=KN.SCROLOCK_ON(KN.CTRL_NUMPAD_2),
    #     ) as self.hk_ctrl_numpad_2:
    #         with hk.SendLabel(
    #             id=TC.mage.name,
    #             to=self.get_lbs_by_tc(TC.mage),
    #         ):
    #             act.Target.TARGET_FOCUS_TARGET()
    #             act.Mage.Counterspell()
    #
    # def build_hk_ctrl_numpad_3_aggressive_dispel(self: "Mode"):
    #     """
    #     todo: docstring
    #     """
    #     with hk.Hotkey(
    #         id="Ctrl Numpad3 - 进攻驱散",
    #         key=KN.SCROLOCK_ON(KN.CTRL_NUMPAD_3),
    #     ) as self.hk_ctrl_numpad_3:
    #         with hk.SendLabel(
    #             id=TC.shaman.name,
    #             to=self.get_lbs_by_tc(TC.shaman),
    #         ):
    #             act.Target.TARGET_FOCUS_TARGET()
    #             act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
    #             act.Shaman.Purge()
    #
    #         with hk.SendLabel(
    #             id=TC.priest.name,
    #             to=self.get_lbs_by_tc(TC.priest),
    #         ):
    #             act.Target.TARGET_FOCUS_TARGET()
    #             act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
    #             act.Priest.Dispel_Magic()
    #
    # def build_hk_ctrl_numpad_4_aoe_fear(self: "Mode"):
    #     """
    #     todo: docstring
    #     """
    #     with hk.Hotkey(
    #         id="Ctrl Numpad4",
    #         key=KN.SCROLOCK_ON(KN.CTRL_NUMPAD_4),
    #     ) as self.hk_ctrl_numpad_4:
    #         with hk.SendLabel(
    #             id=TC.priest_shadow.name,
    #             to=self.get_lbs_by_tc(TC.priest_shadow),
    #         ):
    #             act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
    #             act.PriestShadow.Psychic_Horror()
    #
    # def build_hk_ctrl_numpad_5_typhoon(self: "Mode"):
    #     """
    #     todo: docstring
    #     """
    #     with hk.Hotkey(
    #         id="Ctrl Numpad5",
    #         key=KN.SCROLOCK_ON(KN.CTRL_NUMPAD_5),
    #     ) as self.hk_ctrl_numpad_5:
    #         with hk.SendLabel(
    #             id=TC.druid_balance.name,
    #             to=self.get_lbs_by_tc(TC.druid_balance),
    #         ):
    #             act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
    #             act.DruidBalance.Typhoon()
    #
    # def build_hk_ctrl_numpad_6_thunder_storm(self: "Mode"):
    #     """
    #     todo: docstring
    #     """
    #     with hk.Hotkey(
    #         id="Ctrl Numpad6",
    #         key=KN.SCROLOCK_ON(KN.CTRL_NUMPAD_6),
    #     ) as self.hk_ctrl_numpad_6:
    #         with hk.SendLabel(
    #             id="all_elemental_shaman",
    #             to=self.get_lbs_by_tc(TC.shaman_elemental),
    #         ):
    #             act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
    #             act.ShamanElementalCombat.Thunderstorm()
    #
    # def build_hk_ctrl_numpad_7_hymn_of_life(self: "Mode"):
    #     """
    #     todo: docstring
    #     """
    #     with hk.Hotkey(
    #         id="Ctrl Numpad7",
    #         key=KN.SCROLOCK_ON(KN.CTRL_NUMPAD_7),
    #     ) as self.hk_ctrl_numpad_7:
    #         with hk.SendLabel(
    #             id=TC.priest.name,
    #             to=self.get_lbs_by_tc(TC.priest),
    #         ):
    #             act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
    #             act.Priest.Divine_Hymn()
    #
    # def build_hk_ctrl_numpad_10_hymn_of_mana(self: "Mode"):
    #     """
    #     todo: docstring
    #     """
    #     with hk.Hotkey(
    #         id="Ctrl Numpad10",
    #         key=KN.SCROLOCK_ON(KN.CTRL_NUMPAD_0),
    #     ) as self.hk_ctrl_numpad_10:
    #         with hk.SendLabel(
    #             id=TC.priest.name,
    #             to=self.get_lbs_by_tc(TC.priest),
    #         ):
    #             act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
    #             act.Priest.Hymn_of_Hope()

    def build_hk_ctrl_numpad_11_tank_1_taunt(self: "Mode"):
        """
        todo: docstring
        """
        with hk.Hotkey(
            id="Ctrl Numpad11 - 主坦克嘲讽",
            key=KN.SCROLOCK_ON(KN.CTRL_NUMPAD_11_DIVIDE),
        ) as self.hk_ctrl_numpad_11:
            if self.lb_tank1:
                with hk.SendLabel(
                    id="tank1",
                    to=[self.lb_tank1],
                ):
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                    act.PaladinProtection.Hand_of_Reckoning()

    def build_hk_ctrl_numpad_12_tank_2_taunt(self: "Mode"):
        """
        todo: docstring
        """
        with hk.Hotkey(
            id="Ctrl Numpad12 - 副坦克嘲讽",
            key=KN.SCROLOCK_ON(KN.CTRL_NUMPAD_12_MULTIPLY),
        ) as self.hk_ctrl_numpad_12:
            if self.lb_tank2:
                with hk.SendLabel(
                    id="tank2",
                    to=[self.lb_tank2],
                ):
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                    act.DK.Dark_Command()

    def build_hk_group_09_ctrl_numpad_1_to_12_mixin(self: "Mode"):
        """
        todo: docstring
        """
        # self.build_hk_ctrl_numpad_1_silence_shot_focus_target()
        # self.build_hk_ctrl_numpad_2_counter_spell_focus_target()
        # self.build_hk_ctrl_numpad_3_aggressive_dispel()
        # self.build_hk_ctrl_numpad_4_aoe_fear()
        # self.build_hk_ctrl_numpad_5_typhoon()
        # self.build_hk_ctrl_numpad_6_thunder_storm()
        # self.build_hk_ctrl_numpad_7_hymn_of_life()
        # self.build_hk_ctrl_numpad_10_hymn_of_mana()
        self.build_hk_ctrl_numpad_11_tank_1_taunt()
        self.build_hk_ctrl_numpad_12_tank_2_taunt()
