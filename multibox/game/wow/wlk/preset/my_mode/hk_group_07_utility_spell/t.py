# -*- coding: utf-8 -*-

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TC
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class TMixin:
    def build_hk_default_t(self: "Mode"):
        """
        创建团队随机防御性驱散团队身上的 debuff 快捷键.

        - paladin put cleansing skill on Action Bar Key T
        - shaman put curse toxin skill on Action Bar Key on T
        - druid put remove curse skill on Action Bar Key on T
        - mage put remove curse skill on Action Bar Key on T
        - priest put dispel magic skill on Action Bar Key on T
        """
        with hk.Hotkey(
            id="T - 所有驱散职业随机选择团队成员驱散",
            key=KN.SCROLOCK_ON(KN.T),
        ) as self.hk_t_dispel_raid:
            with hk.SendLabel(
                id=TC.dispeler.name,
                to=self.get_lbs_by_tc(TC.dispeler),
            ):
                act.Target.TARGET_RAID()
                hk.Key.trigger()

    def build_t_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_t()
