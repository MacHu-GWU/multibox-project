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


class AltShiftTMixin:
    """
    todo: docstring
    """

    def build_hk_default_alt_shift_t(self: "Mode"):
        """
        **说明**

        所有有进攻驱散技能的角色放进攻驱散 (驱散怪物身上的 Buff).

        - 优先让至少 2 个 DPS 职业 (猎人, 法师, DPS 萨满, 暗牧) 对焦点的目标施放进攻驱散.
        - 如果没有能进攻驱散的 DPS 职业再考虑让治疗职业 (恢复萨, 治疗牧师) 施放.
        - 如果已经有至少 1 个角色施放了进攻驱散, 而还有其他的 DPS 职业可用, 则让最多
            3 个角色随机按 Tab 选择敌人施放进攻驱散.

        **使用方法**

        按就行了.

        **动作条安排**

        - 动作条按钮上就是台风技能.
        - 动作条按钮要绑定 ``G`` 快捷键, 并确保跟 ``act.DruidBalance.Typhoon``
            中的定义一致.
        """
        with hk.Hotkey(
            id="Alt Shift T - 进攻驱散",
            key=KN.SCROLOCK_ON(KN.ALT_SHIFT_T),
        ) as self.hk_alt_shift_g_take_turn_offensive_dispel:
            lbs_shaman_dps = self.get_lbs_by_tc(TC.shaman_dps)
            lbs_shaman_healer = self.get_lbs_by_tc(TC.shaman_healer)
            lbs_hunter = self.get_lbs_by_tc(TC.hunter)
            lbs_mage = self.get_lbs_by_tc(TC.mage)
            lbs_priest_shadow = self.get_lbs_by_tc(TC.priest_shadow)
            lbs_priest_healer = self.get_lbs_by_tc(TC.priest_healer)
            # priority: mage -> shaman ps -> priest shadow -> hunter -> priest healer -> shaman healer
            lbs_all = OrderedSet(
                [
                    *lbs_shaman_healer,
                    *lbs_priest_healer,
                    *lbs_hunter,
                    *lbs_priest_shadow,
                    *lbs_shaman_dps,
                    *lbs_mage,
                ]
            )
            lbs_dps = OrderedSet(
                [
                    *lbs_shaman_healer,
                    *lbs_priest_healer,
                ]
            )
            # create label to key mapping
            lb_to_spell_mapping = dict()
            for lb in (lbs_shaman_dps | lbs_shaman_healer):
                lb_to_spell_mapping[lb] = act.Shaman.Purge
            for lb in lbs_hunter:
                lb_to_spell_mapping[lb] = act.Hunter.Tranquilizing_Shot
            for lb in lbs_mage:
                lb_to_spell_mapping[lb] = act.Mage.Spellsteal
            for lb in (lbs_priest_shadow | lbs_priest_healer):
                lb_to_spell_mapping[lb] = act.Priest.Dispel_Magic
            # get the two dps to dispel
            if len(lbs_all):
                lb = lbs_all.pop()
                with hk.SendLabel(to=[lb]):
                    act.Target.TARGET_FOCUS_TARGET()
                    lb_to_spell_mapping[lb]()
            else:
                return
            if len(lbs_all):
                lb = lbs_all.pop()
                with hk.SendLabel(to=[lb]):
                    act.Target.TARGET_FOCUS_TARGET()
                    lb_to_spell_mapping[lb]()
            else:
                return
            # get the rest of the dps (max to 3 chars) to dispel
            lbs_dps = lbs_all.intersection(lbs_dps)[:3]
            for lb in lbs_dps:
                with hk.SendLabel(to=[lb]):
                    act.Target.TARGET_NEAREST_ENEMY()
                    lb_to_spell_mapping[lb]()

    def build_alt_shift_t_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_alt_shift_t()
