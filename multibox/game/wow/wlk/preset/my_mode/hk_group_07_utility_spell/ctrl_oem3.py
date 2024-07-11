# -*- coding: utf-8 -*-

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
import multibox.game.wow.wlk.api as wlk
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class CtrlOem3Mixin:
    def build_hk_ctrl_oem3(self: "Mode"):
        for i in range(1, 1 + 6):
            with hk.Hotkey(
                id=f"Ctrl {i}",
                key=KN.SCROLOCK_ON(getattr(KN, f"CTRL_{i}")),
            ):
                with hk.SendLabel(
                    name="all",
                    to=self.lbs_all,
                ):
                    act.Target.TARGET_FOCUS_TARGET()
                    act.General.TRIGGER()

    def build_ctrl_oem3_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_ctrl_oem3()
