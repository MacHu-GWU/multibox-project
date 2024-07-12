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


class HealBotInnervateMixin:
    """
    todo: docstring
    """

    def build_hk_default_healbot_innervate(self: "Mode"):
        """
        **说明**

        在 Leader 角色的窗口内用鼠标选择团队框架上的角色, 然后按住 Ctrl + Numpad 1/2/3,
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
        hotkey_list = list()
        for i, key in [
            (1, KN.CTRL_NUMPAD_1),
            (2, KN.CTRL_NUMPAD_2),
            (3, KN.CTRL_NUMPAD_3),
        ]:
            with hk.Hotkey(
                id=f"Healbot Innervate {i}",
                key=KN.SCROLOCK_ON(key),
            ) as hotkey:
                if len(lbs_druid):
                    lb = lbs_druid.pop()
                    lbs_assigned.add(lb)
                    with hk.SendLabel(
                        id=f"Healbot Druid {i} cast Innervate",
                        to=[lb],
                    ):
                        act.Druid.HB_Innervate()
                # other
                self._build_other_guy_do_your_job(
                    lbs_assigned=lbs_assigned,
                    id="Healbot Innervate {role}",
                )
            hotkey_list.append(hotkey)

        self.hk_healbot_innervate_1 = hotkey_list[0]
        self.hk_healbot_innervate_2 = hotkey_list[1]
        self.hk_healbot_innervate_3 = hotkey_list[2]

    def build_healbot_innervate(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_healbot_innervate()
