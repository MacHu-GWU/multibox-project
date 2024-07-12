# -*- coding: utf-8 -*-

import typing as T

from .small_heal import HealBotSmallHealMixin
from .big_heal import HealBotBigHealMixin
from .aoe_heal import HealBotAoeHealMixin
from .dispel import HealBotDispelMixin
from .innervate import HealBotInnervateMixin

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class HotkeyGroup11HealBotMixin(
    HealBotSmallHealMixin,
    HealBotBigHealMixin,
    HealBotAoeHealMixin,
    HealBotDispelMixin,
    HealBotInnervateMixin,
):
    def build_hk_group_11_healbot_mixin(self: "Mode"):
        self.build_healbot_small_heal()
        self.build_healbot_big_heal()
        self.build_healbot_aoe_heal()
        self.build_healbot_dispel()
        self.build_healbot_innervate()