# -*- coding: utf-8 -*-

import typing as T

from hotkeynet.api import Hotkey, SendLabel, KN, CAN
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class Act1Mixin:
    def build_default_act1(self: "Mode"):
        pass

    def build_act1(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act1()
