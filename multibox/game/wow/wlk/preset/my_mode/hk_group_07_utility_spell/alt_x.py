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


class AltXMixin:
    """
    todo: docstring
    """

    def build_hk_default_alt_x(self: "Mode"):
        """
        **说明**

        有需要选择施放 AOE 区域的人使用 AOE 技能. 点击后会出现选择的 AOE 技能的施放地点的法阵,
        例如法师的暴风雪, 德鲁伊的飓风, 猎人的乱射, DK 的死亡凋零.

        **使用方法**

        先按 :meth:`...` 确保所有人的摄像头视角都是统一的斜上方 45 度视角. 然后按这个键,
        再用 :meth:`...` 让所有人在窗口中的同一个位置点左键.

        **动作条安排**

        - 动作条按钮上就是 AOE 技能.
        - 动作条按钮要绑定 ``Alt + X`` 快捷键, 并确保跟 ``act`` 中的定义一致.
        """
        with hk.Hotkey(
            id="Alt + X - 所有 AOE 职业放区域选定 AOE 技能, 例如法师暴风雪, DK死亡凋零",
            key=KN.SCROLOCK_ON(KN.ALT_X),
        ) as self.hk_alt_x_aoe_target_location:
            with hk.SendLabel(
                id=TC.dk.name,
                to=self.get_lbs_by_tc(TC.dk),
            ):
                # act.General.ESC()
                act.DK.Death_and_Decay()  # DK 放死亡凋零

            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.get_lbs_by_tc(TC.hunter),
            ):
                # act.General.ESC()
                act.Hunter.Volley()  # 猎人放乱射

            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.get_lbs_by_tc(TC.druid_balance),
            ):
                # act.General.ESC()
                act.DruidBalance.Hurricane()  # 平衡德放飓风

            with hk.SendLabel(
                id=TC.warlock.name,
                to=self.get_lbs_by_tc(TC.warlock),
            ):
                # act.General.ESC()
                act.Warlock.Rain_of_Fire()  # 术士放火雨

            with hk.SendLabel(
                id=TC.mage.name,
                to=self.get_lbs_by_tc(TC.mage),  # 法师放暴风雪
            ):
                # act.General.ESC()
                act.Mage.Blizzard()

            # todo, 暗牧放精神灼烧

    def build_alt_x_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_alt_x()
