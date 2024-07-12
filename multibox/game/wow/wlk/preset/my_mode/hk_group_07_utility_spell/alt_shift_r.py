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


def make_hunter_tranquilizing_send_label(lbs: T.Iterable[str]):
    with hk.SendLabel(to=lbs):
        act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
        act.Target.TARGET_FOCUS_TARGET()
        act.Hunter.Tranquilizing_Shot()


class AltShiftRMixin:
    """
    todo: docstring
    """

    def build_hk_default_alt_shift_r(self: "Mode"):
        """
        将猎人分成两组轮流施放宁神射击. 宁神设计的 CD 是 8 秒, 并且猎人未命中的概率非常低,
        所以基本可以确保一个猎人盯 1 个怪宁神是不会 Miss 的. 但有的场景下会出现多个怪要打宁神
        的情况. 如果我们多开团队中只有 1 个 Leader, 这时我们把猎人分组就能保证每个怪都有 CD 打宁神.
        而如果团队有 2 个 Leader 分头行动, 那么这个方式就不适用了, 应该给每个 Leader 分配一个
        猎人, 让他们跟着自己的司机各自打宁神.

        注: 如果你按宁神技能但是怪物身上没有 buff 可驱散时, 技能并不会打出去. 所以不用担心在
        1 号 Leader 宁神的时候按出去了, 结果 2 号 Leader 那边的怪物激怒了结果按不出宁神的情况.
        """

        with hk.Hotkey(
            id="Alt Shift R - 猎人轮流对焦点目标放宁神射击",
            key=KN.SCROLOCK_ON(KN.ALT_SHIFT_R),
        ) as self.hk_alt_shift_r_hunter_take_turn_tranquilizing:
            lbs_hunter = self.get_lbs_by_tc(TC.hunter)
            n_hunter = len(lbs_hunter)
            if n_hunter == 1:
                make_hunter_tranquilizing_send_label(lbs_hunter)
            else:
                n_half = int(n_hunter / 2)
                lbs_first_half = lbs_hunter[:n_half]
                lbs_second_half = lbs_hunter[n_half:]
                with hk.Toggle():
                    make_hunter_tranquilizing_send_label(lbs_first_half)
                with hk.Toggle():
                    make_hunter_tranquilizing_send_label(lbs_second_half)

    def build_hk_alt_shift_r_all_shot(self: "Mode"):
        """
        所有猎人对焦点目标放宁神射击.

        .. seealso::

            :meth:build_hk_default_alt_shift_r
        """

        with hk.Hotkey(
            id="Alt Shift R - 所有猎人对焦点目标放宁神射击",
            key=KN.SCROLOCK_ON(KN.ALT_SHIFT_R),
        ) as self.hk_alt_shift_r_hunter_take_turn_tranquilizing:
            lbs_hunter = self.get_lbs_by_tc(TC.hunter)
            n_hunter = len(lbs_hunter)
            if n_hunter == 1:
                make_hunter_tranquilizing_send_label(lbs_hunter)
            else:
                n_half = int(n_hunter / 2)
                lbs_first_half = lbs_hunter[:n_half]
                lbs_second_half = lbs_hunter[n_half:]
                with hk.Toggle():
                    make_hunter_tranquilizing_send_label(lbs_first_half)
                with hk.Toggle():
                    make_hunter_tranquilizing_send_label(lbs_second_half)

    def build_alt_shift_r_mixin(self: "Mode"):
        # 在需要分头行动的 boss 战中用这个设定
        if self.name == "special_mode":
            self.build_hk_alt_shift_r_all_shot()
        else:
            self.build_hk_default_alt_shift_r()
