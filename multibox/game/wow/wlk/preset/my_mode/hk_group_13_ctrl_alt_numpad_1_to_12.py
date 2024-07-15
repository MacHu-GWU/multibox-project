# -*- coding: utf-8 -*-

"""
实现 Ctrl Alt + 小键盘 1-12 的快捷键功能. 通常是一些 Boss 战中需要安排减伤链, 抬血链,
回蓝链的技能.
"""

import typing as T

from ordered_set import OrderedSet
from hotkeynet import api as hk
from hotkeynet.api import KN

from multibox.game.wow.wlk.api import TalentCategory as TC
from ..my_act import api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


class HotkeyGroup13CtrlAltNumpad1To12Mixin:
    """
    todo: docstring.
    """

    def build_hk_ctrl_alt_numpad_1_2_3_paladin_1_2_3_divine_sacrifice(self: "Mode"):
        """
        **说明**

        所有的骑士轮流放神圣牺牲团队减伤. 适用团队中有多个骑士打团本的情况.

        **使用方法**

        Ctrl Alt + Numpad 1/2/3 分别对应 1/2/3 号骑士. 优先顺序是 惩戒骑, 奶骑, 防骑.

        **动作条安排**

        - 动作条按钮上就是神圣牺牲宏. 该宏按一下是放神圣牺牲, 再按一下是取消自己分担伤害的 Buff,
            只保留团队减伤效果.
        - 动作条按钮要绑定 ``Shift + C`` 快捷键, 并确保跟 ``act.PaladinProtection.Divine_Sacrifice``
            中的定义一致.
        """
        lbs_paladin_dps = self.get_lbs_by_tc(TC.paladin_dps)
        lbs_paladin_healer = self.get_lbs_by_tc(TC.paladin_healer)
        lbs_paladin_tank = self.get_lbs_by_tc(TC.paladin_tank)
        lbs_paladin = OrderedSet.union(
            lbs_paladin_tank,
            lbs_paladin_healer,
            lbs_paladin_dps,
        )
        keys = [
            KN.CTRL_ALT_NUMPAD_1,
            KN.CTRL_ALT_NUMPAD_2,
            KN.CTRL_ALT_NUMPAD_3,
        ]
        i = 0
        self.hk_list_divine_sacrifice: T.List[hk.Hotkey] = list()
        for lb, key in zip(lbs_paladin[:3], keys):
            i += 1
            with hk.Hotkey(
                id=f"Ctrl Alt Numpad{i} - {i} 号骑士开神圣牺牲全团减伤",
                key=KN.SCROLOCK_ON(key),
            ) as hotkey:
                with hk.SendLabel(
                    id=f"Ctrl Alt Numpad{i} - {i} 号骑士开神圣牺牲全团减伤",
                    to=[lb],
                ):
                    act.PaladinProtection.Divine_Sacrifice()
                    act.PaladinProtection.Divine_Sacrifice()
                self.hk_list_divine_sacrifice.append(hotkey)

    def build_hk_ctrl_alt_numpad_7_to_12_priest_1_2_3_divine_and_hope_hymn(
        self: "Mode",
    ):
        """
        **说明**

        所有的牧师轮流放神圣赞美诗 (血歌, 团队抬血) / 希望颂歌 (蓝歌, 团队回蓝). 适用团队中
        有多个牧师打团本的情况.

        **使用方法**

        Ctrl Alt + Numpad 7/8/9 分别对应 1/2/3 号血歌牧师.
        Ctrl Alt + Numpad 10/11/12 分别对应 1/2/3 号蓝歌牧师.
        优先顺序是 暗牧, 戒律牧, 神牧.

        **动作条安排**

        - 动作条按钮上就是血歌和蓝歌技能既可.
        - 动作条按钮要绑定 ``Ctrl + G`` (血歌), ``Ctrl + X`` (蓝歌) 快捷键,
        并确保跟 ``act.Priest.Divine_Hymn``, ``act.Priest.Hymn_of_Hope`` 中的定义一致.
        """
        lbs_priest_shadow = self.get_lbs_by_tc(TC.priest_shadow)
        lbs_priest_disco = self.get_lbs_by_tc(TC.priest_disco)
        lbs_priest_holy = self.get_lbs_by_tc(TC.priest_holy)
        lbs_priest = OrderedSet.union(
            lbs_priest_holy,
            lbs_priest_disco,
            lbs_priest_shadow,
        )

        keys = [
            KN.CTRL_ALT_NUMPAD_7,
            KN.CTRL_ALT_NUMPAD_8,
            KN.CTRL_ALT_NUMPAD_9,
        ]
        i = 0
        self.hk_list_divine_hymn_of: T.List[hk.Hotkey] = list()
        for lb, key in zip(lbs_priest[:3], keys):
            i += 1
            with hk.Hotkey(
                id=f"Ctrl Alt Numpad{i + 6} - {i} 号牧师开血歌",
                key=KN.SCROLOCK_ON(key),
            ) as hotkey:
                with hk.SendLabel(
                    id=f"Ctrl Alt Numpad{i + 6} - {i} 号牧师开血歌",
                    to=[lb],
                ):
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                    act.Priest.Divine_Hymn()
                self.hk_list_divine_hymn_of.append(hotkey)

        keys = [
            KN.CTRL_ALT_NUMPAD_0,
            KN.CTRL_ALT_NUMPAD_11_DIVIDE,
            KN.CTRL_ALT_NUMPAD_12_MULTIPLY,
        ]
        i = 0
        self.hk_list_hymn_of_hope: T.List[hk.Hotkey] = list()
        for lb, key in zip(lbs_priest[:3], keys):
            i += 1
            with hk.Hotkey(
                id=f"Ctrl Alt Numpad{i + 9} - {i} 号牧师开蓝歌",
                key=KN.SCROLOCK_ON(key),
            ) as hotkey:
                with hk.SendLabel(
                    id=f"Ctrl Alt Numpad{i + 9} - {i} 号牧师开蓝歌",
                    to=[lb],
                ):
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                    act.Priest.Hymn_of_Hope()
                self.hk_list_hymn_of_hope.append(hotkey)

    def build_hk_group_13_ctrl_alt_numpad_1_to_12_mixin(self: "Mode"):
        """
        todo: docstring
        """
        self.build_hk_ctrl_alt_numpad_1_2_3_paladin_1_2_3_divine_sacrifice()
        self.build_hk_ctrl_alt_numpad_7_to_12_priest_1_2_3_divine_and_hope_hymn()
