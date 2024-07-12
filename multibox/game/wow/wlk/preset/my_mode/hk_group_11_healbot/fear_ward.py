# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

from ordered_set import OrderedSet
import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TC
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class HealBotFearWardMixin:
    """
    todo: docstring
    """

    def build_hk_default_healbot_fear_ward(self: "Mode"):
        """
        **说明**

        在 Leader 角色的窗口内用鼠标选择团队框架上的角色, 然后按住 Ctrl + Numpad 4/5/6,
        可以分别让 1, 2, 3 号牧师给目标施放反恐惧结界, 并且让其他 Tank 和 DPS 继续正常打怪.

        分配任务的逻辑是:

        暗牧优先于其他牧师.

        **使用方法**

        按就行了.

        **动作条安排**

        todo
        """
        lbs_priest_shadow = self.get_lbs_by_tc(TC.priest_shadow)
        lbs_priest_healer = self.get_lbs_by_tc(TC.priest_healer)
        lbs_priest = OrderedSet.union(
            lbs_priest_healer,
            lbs_priest_shadow,
        )

        lbs_assigned = OrderedSet()
        for i, key in [
            (4, KN.CTRL_NUMPAD_4),
            (5, KN.CTRL_NUMPAD_5),
            (6, KN.CTRL_NUMPAD_6),
        ]:
            if len(lbs_priest):
                lb = lbs_priest.pop()
                lbs_assigned.add(lb)
                with hk.Hotkey(
                    id=f"Healbot Fear Ward {i}",
                    key=KN.SCROLOCK_ON(key),
                ) as self.hk_healbot_fear_ward:
                    with hk.SendLabel(
                        id=f"Healbot Priest {i} cast Fear Ward",
                        to=[lb],
                    ):
                        act.Priest.Fear_Ward()

        # other
        self._build_other_guy_do_your_job(
            lbs_assigned=lbs_assigned,
            id="Healbot Fear Ward {role}",
        )

    def build_healbot_fear_ward(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_healbot_fear_ward()
