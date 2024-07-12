# -*- coding: utf-8 -*-

import typing as T
import itertools

import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
from multibox.game.wow.wlk.api import TC
import multibox.game.wow.wlk.preset.my_act.api as act

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class RMixin:
    def build_hk_default_r(self: "Mode"):
        with hk.Hotkey(
            id="R - 能打断的职业打断",
            key=KN.SCROLOCK_ON(KN.R),
        ) as self.hk_r_interrupt:
            # 近战打断, CD 都是 10 秒
            # lbs_warrior = self.lbs_by_tc(TC.warrior)
            # lbs_rogue = self.lbs_by_tc(TC.rogue)
            lbs_dk = self.get_lbs_by_tc(TC.dk)

            # 远程打断
            # 萨满打断技能 CD 很短, 只有 6 秒
            lbs_shaman_non_resto = self.get_lbs_by_tc(TC.shaman_non_resto)
            # 萨满打断技能 CD 很短, 只有 6 秒
            lbs_shaman_resto = self.get_lbs_by_tc(TC.shaman_resto)
            lbs_shaman = lbs_shaman_non_resto.union(lbs_shaman_resto)
            # 法师反制 CD 24 秒
            lbs_mage = self.get_lbs_by_tc(TC.mage)
            # 猎人 沉默射击 CD 24 秒
            lbs_marksman_hunter = self.get_lbs_by_tc(TC.hunter_marksman)
            # shadow_priest_lbs = self.lbs_by_tc(TC.priest_shadow) # 不是每一个牧师都会点出沉默

            n_melee = len(lbs_dk)
            n_shaman = len(lbs_shaman)
            n_range = len(lbs_mage) + len(lbs_marksman_hunter)

            melee_pairs = [(label, act.DK.Mind_Freeze) for label in lbs_dk]
            shaman_pairs = [(label, act.Shaman.Wind_Shear) for label in lbs_shaman]

            mage_pairs = [(label, act.Mage.Counterspell) for label in lbs_mage]
            hunter_pairs = [
                (label, act.HunterMarksmanship.Silencing_Shot)
                for label in lbs_marksman_hunter
            ]
            range_pairs = mage_pairs + hunter_pairs

            loop_melee = itertools.cycle(melee_pairs)
            loop_range = itertools.cycle(range_pairs)

            # 没有萨满的情况:
            if len(lbs_shaman) == 0:
                pass
            # 有一个 萨满的情况
            elif len(lbs_shaman) == 1:
                shaman_label, shaman_key = lbs_shaman[0], act.Shaman.Wind_Shear
                # 如果没有其他远程打断角色, 那么每次都是这个萨满来打断
                if n_range == 0:
                    with hk.SendLabel(
                        to=[
                            shaman_label,
                        ]
                    ):
                        shaman_key()
                # 如果有少于 2 个其他远程打断角色, 那么打断循环就是:
                # 角色 1 -> 萨满 -> 角色 2 -> 萨满 -> 角色 1 -> 萨满 -> ...
                elif len(range_pairs) <= 2:
                    for label, key in range_pairs:
                        with hk.Toggle():
                            with hk.SendLabel(to=[label]):
                                key()
                        with hk.Toggle():
                            with hk.SendLabel(
                                to=[
                                    shaman_label,
                                ]
                            ):
                                shaman_key()
                # 如果有多于 2 个 (3 个或 3 个以上) 其他远程打断角色, 那么打断循环就是:
                # 角色 1 和 萨满 -> 角色 2 和 萨满 -> 角色 3 和 萨满 -> 角色 1 和 萨满 -> ...
                else:
                    for label, key in range_pairs:
                        with hk.Toggle():
                            with hk.SendLabel(to=[label]):
                                key()
                            with hk.SendLabel(to=[shaman_label]):
                                shaman_key()
            # 有两个 萨满的情况, 两个萨满配合其他人轮流来
            elif len(lbs_shaman) >= 2:
                # 如果有其他远程打断角色, 那么这两个萨满还是轮流来
                # 但是穿插其他远程打断角色 以及 近战打断角色
                for label, key in shaman_pairs:
                    with hk.Toggle():
                        with hk.SendLabel(to=[label]):
                            key()
                        if n_melee:
                            label_melee, key_melee = next(loop_melee)
                            with hk.SendLabel(to=[label_melee]):
                                key_melee()
                        if n_range:
                            label_range, key_range = next(loop_range)
                            with hk.SendLabel(to=[label_range]):
                                key_range()
                # 重复两次是因为我们有可能 近战 / 远程 打断的数量多于萨满
                for label, key in shaman_pairs:
                    with hk.Toggle():
                        with hk.SendLabel(to=[label]):
                            key()
                        if n_melee:
                            label_melee, key_melee = next(loop_melee)
                            with hk.SendLabel(to=[label_melee]):
                                key_melee()
                        if n_range:
                            label_range, key_range = next(loop_range)
                            with hk.SendLabel(to=[label_range]):
                                key_range()

    def build_r_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_r()
