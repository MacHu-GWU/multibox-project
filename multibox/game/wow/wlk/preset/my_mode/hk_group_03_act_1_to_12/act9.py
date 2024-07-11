# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN


if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class Act9Mixin:
    """
    todo: docstring
    """

    def build_default_act9(self: "Mode"):
        """
        See :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="Key8",
            key=KN.SCROLOCK_ON(KN.KEY_9),
        ) as self.hk_8:
            with hk.SendLabel(
                id="all",
                to=self.get_lbs_all(),
            ):
                CAN.KEY_9()

    def build_act9(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act9()
