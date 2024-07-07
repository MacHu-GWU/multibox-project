# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.preset.my_mode.utils import TargetEnum

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class Act7Mixin:
    """
    todo: docstring
    """

    def build_default_act7(self: "Mode"):
        """
        See :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        self.build_tank_default_action(key=KN.KEY_6)
        self.build_dps_default_action(key=KN.KEY_6)
        self.build_healer_default_action(
            key=KN.KEY_6,
            target=TargetEnum.TARGET_FOCUS_TARGET,
        )

    def build_act7(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act7()
