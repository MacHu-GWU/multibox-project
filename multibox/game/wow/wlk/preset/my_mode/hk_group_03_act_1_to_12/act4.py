# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TL, TC
import multibox.game.wow.wlk.preset.my_act.api as act


if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class Act4Mixin:
    """
    todo: docstring
    """

    def build_default_act4(self: "Mode"):
        """
        Act 4 技能主要是周期性的补一些技能. 包括:

        1. 奶骑每 15 秒一次给焦点的目标 (boss) 补圣光审判.
        2. 奶萨每 30 秒一次给 tank 补大地之盾.
        3. 戒律牧和神牧每 15 秒一次给 tank 补愈合祷言.

        Tank 和 DPS 职业则自由正常拉怪打怪.

        Ref:

        - :ref:`wow-wlk-simulate-periodical-skill-casting`
        - :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="Key4",
            key=KN.SCROLOCK_ON(KN.KEY_4),
        ) as self.hk_4:
            self.build_tank_default_action(key=KN.KEY_4)
            self.build_dps_default_action(key=KN.KEY_4)

            # 奶骑
            for lb in self.get_lbs_paladin_holy():
                with hk.SendLabel(to=[lb]):
                    act.Target.TARGET_FOCUS_TARGET()
                    act.PaladinHoly.MB_Periodical_Judgement_of_Light_on_Focus_Target_Macro()

            # 奶萨, 奶德, 牧师
            for lb in (
                self.get_lbs_shaman_resto()
                | self.get_lbs_druid_resto()
                | self.get_lbs_priest_disco()
                | self.get_lbs_priest_holy()
            ):
                char = self.get_char_by_label(lb)
                if char.is_raid_healer:
                    with hk.SendLabel(to=[lb]):
                        CAN.KEY_4()

    def build_act4(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act4()
