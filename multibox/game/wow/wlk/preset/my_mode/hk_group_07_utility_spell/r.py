# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TC
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class RMixin:
    """
    todo: docstring
    """

    def build_hk_default_r(self: "Mode"):
        """
        **说明**

        将所有有打断技能的职业分组轮流打断施法. 假设我们团队中有 3 个近战, 3 个远程打断职业,
        我们可以将它们分为 3 组, 每一组都有 1 个近战和 1 个远程. 这样可以保证每一个施法都有
        至少两个人在打断, 并且 Boss 几乎不会有施法成功的机会.

        这个方法假设你在 dataset 的 excel 中显式定义了分别哪个角色是 1, 2, 3 打断. 这个
        方法以前的实现方式是按照一定的逻辑分析团队中有哪些天赋的角色, 然后尝试自动分组. 后来
        发现这样的逻辑实现起来 bug 太多, 而且不够灵活. 所以现在改为显式定义.

        巫妖王之怒版本所有的打断技能请参考: https://docs.google.com/spreadsheets/d/1vr8NwGpVcjbpQKonHJ1_zRLQGxQULO_vUURaZ1dGH6Y/edit?gid=994045182#gid=994045182

        **使用方法**

        按 1 下就有一组人打断. 根据团队配置可能会有 3 个组, 也可能只有 1 或 2 个组.

        **动作条安排**

        - 动作条按钮上就是打断技能.
        - 动作条按钮要绑定 ``R`` 快捷键, 并确保每个职业的打断技能按钮都是 R.
        """
        with hk.Hotkey(
            id="R - 能打断的职业打断",
            key=KN.SCROLOCK_ON(KN.R),
        ) as self.hk_r_interrupt:
            lbs_warrior_dps = self.get_lbs_by_tc(TC.warrior_dps)
            lbs_warrior_tank = self.get_lbs_by_tc(TC.warrior_tank)
            lbs_dk = self.get_lbs_by_tc(TC.dk)
            lbs_hunter_marksman = self.get_lbs_by_tc(TC.hunter_marksman)
            lbs_shaman = self.get_lbs_by_tc(TC.shaman)
            lbs_rogue = self.get_lbs_by_tc(TC.rogue)
            lbs_warlock_affliction = self.get_lbs_by_tc(TC.warlock_affliction)
            lbs_mage = self.get_lbs_by_tc(TC.mage)

            lb_to_key_mapping = dict()
            for lb in lbs_warrior_dps:
                lb_to_key_mapping[lb] = act.Warrior.Pummel
            for lb in lbs_warrior_tank:
                lb_to_key_mapping[lb] = act.Warrior.Shield_Bash
            for lb in lbs_dk:
                lb_to_key_mapping[lb] = act.DK.Mind_Freeze
            for lb in lbs_hunter_marksman:
                lb_to_key_mapping[lb] = act.Hunter.Silencing_Shot
            for lb in lbs_shaman:
                lb_to_key_mapping[lb] = act.Shaman.Wind_Shear
            # for lb in lbs_rogue:
            #     lb_to_key_mapping[lb] = act.Rogue.Kick
            for lb in lbs_warlock_affliction:
                lb_to_key_mapping[lb] = CAN.CTRL_7  # 恶魔犬的法术反制
            for lb in lbs_mage:
                lb_to_key_mapping[lb] = act.Mage.Counterspell

            # fmt: off
            lbs_1 = [char.window.label for char in self.active_chars if char.is_1_interrupt]
            lbs_2 = [char.window.label for char in self.active_chars if char.is_2_interrupt]
            lbs_3 = [char.window.label for char in self.active_chars if char.is_3_interrupt]
            # fmt: on
            for lbs in [lbs_1, lbs_2, lbs_3]:
                if len(lbs):
                    with hk.Toggle():
                        for lb in lbs:
                            with hk.SendLabel(to=[lb]):
                                lb_to_key_mapping[lb]()

    def build_r_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_r()
