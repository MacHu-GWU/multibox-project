# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.preset.my_mode.utils import TargetEnum


if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class Act6Mixin:
    """
    todo: docstring
    """

    def build_hk_default_act6(self: "Mode"):
        """
        See :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="Key6",
            key=KN.SCROLOCK_ON(KN.KEY_6),
        ) as self.hk_6:
            self.build_tank_default_action(key=KN.KEY_6)
            self.build_dps_default_action(key=KN.KEY_6)
            self.build_healer_default_action(
                key=KN.KEY_6,
                target=TargetEnum.TARGET_FOCUS_TARGET,
            )

    def build_act6(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_act6()
