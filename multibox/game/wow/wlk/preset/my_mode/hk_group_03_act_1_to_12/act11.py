# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class Act11Mixin:
    """
    todo: docstring
    """

    def build_default_act11(self: "Mode"):
        """
        See :ref:`wow-wlk-act-1-to-10-tank-dps-healer`
        """
        with hk.Hotkey(
            id="SetFocusMode1",
            key=KN.SCROLOCK_ON(KN.KEY_11_MINUS),
        ) as self.hk_11_focus_mode_1:
            for char in self.active_chars:
                if char.is_leader_1:  # 司机本人清除焦点
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[char.window.label],
                    ):
                        act.General.CLEAR_FOCUS_NUMPAD_7()
                else:  # 其他人设置焦点
                    if char.leader_1 is not None:
                        with hk.SendLabel(
                            id=char.account.username,
                            to=[char.window.label],
                        ):
                            self.target_key_mapping[char.leader_1.window.label]()
                            act.General.SET_FOCUS_KEY_NUMPAD_6()

    def build_act11(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_default_act11()
