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


class ActAlt5Mixin:
    """
    todo: docstring
    """

    def build_hk_default_act_alt_5(self: "Mode"):
        """
        See :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="Alt 5",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.KEY_5)),
        ) as self.hk_alt_5:
            with hk.SendLabel(
                id=TC.priest_healer.name,
                to=self.get_lbs_by_tc(tc=TC.priest_healer),
            ):
                act.Target.TARGET_SELF()
                act.Priest.Prayer_of_Healing()

            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.get_lbs_by_tc(tc=TC.shaman),
            ):
                act.Target.TARGET_SELF()
                act.Shaman.Chain_Heal()

    def build_act_alt_5(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_act_alt_5()
