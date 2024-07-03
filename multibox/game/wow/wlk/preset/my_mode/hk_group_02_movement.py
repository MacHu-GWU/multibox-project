# -*- coding: utf-8 -*-

"""
实现与人物移动有关的快捷键.
"""

import typing as T

from hotkeynet import api as hk
from hotkeynet.api import KN

from multibox.game.wow.wlk.api import TalentCategory as TC
from ..my_act import api as act


if T.TYPE_CHECKING:  # pragma: no cover
    from .mode import Mode


T_LABEL_LIKE = T.Union[str, int]
T_LABEL_ARG = T.Union[T_LABEL_LIKE, T.List[T_LABEL_LIKE]]


class HotkeyGroup02MovementMixin:
    def preprocess_labels(
        self: "Mode",
        lbs: T_LABEL_ARG,
    ) -> T.List[str]:
        """
        把 "label liked" 参数转化成字符串形式的 labels. 可供 ``SendLabel(to=...)``
        API 使用.

        - 如果输入不是 list, 则转化成 list.
        - 如果 list 里的元素是 int, 则转化成 "w01" 这种形式.
        - 如果 list 里的元素是 str, 则不做处理.

        :param lbs: int, str, or list of int, list of str.
        """
        if isinstance(lbs, list) is False:
            lbs = [lbs]
        new_lbs = list()
        for ind in lbs:
            if isinstance(ind, int):
                new_lbs.append(f"w{str(ind).zfill(2)}")
            else:
                new_lbs.append(ind)
        return new_lbs

    def _go_up(self, lbs: T_LABEL_ARG):
        with hk.SendLabel(
            id="up",
            to=self.preprocess_labels(lbs),
        ) as send_label:
            act.Movement.MOVE_FORWARD()
            return send_label

    def _go_down(self, lbs: T_LABEL_ARG):
        with hk.SendLabel(
            id="down",
            to=self.preprocess_labels(lbs),
        ) as send_label:
            act.Movement.MOVE_BACKWARD()
            return send_label

    def _go_left(self, lbs: T_LABEL_ARG):
        with hk.SendLabel(
            id="left",
            to=self.preprocess_labels(lbs),
        ) as send_label:
            act.Movement.MOVE_LEFT()
            return send_label

    def _go_right(self, lbs: T_LABEL_ARG):
        with hk.SendLabel(
            id="right",
            to=self.preprocess_labels(lbs),
        ) as send_label:
            act.Movement.MOVE_RIGHT()
            return send_label

    def _go_left_up(self, lbs: T_LABEL_ARG):
        with hk.SendLabel(
            id="left_up",
            to=self.preprocess_labels(lbs),
        ) as send_label:
            act.Movement.MOVE_LEFT_TOP()
            return send_label

    def _go_left_down(self, lbs: T_LABEL_ARG):
        with hk.SendLabel(
            id="left_down",
            to=self.preprocess_labels(lbs),
        ) as send_label:
            act.Movement.MOVE_LEFT_BOTTOM()
            return send_label

    def _go_right_up(self, lbs: T_LABEL_ARG):
        with hk.SendLabel(
            id="right_up",
            to=self.preprocess_labels(lbs),
        ) as send_label:
            act.Movement.MOVE_RIGHT_TOP()
            return send_label

    def _go_right_down(self, lbs: T_LABEL_ARG):
        with hk.SendLabel(
            id="right_down",
            to=self.preprocess_labels(lbs),
        ) as send_label:
            act.Movement.MOVE_RIGHT_BOTTOM()
            return send_label

    def build_hk_all_move_up_down_turn_left_right(self: "Mode"):
        """
        按下键盘上的上下左右方向键, 分别使得所有窗口 前进, 后退, 左转, 右转.
        """
        with hk.MovementHotkey(
            id="All Move Up Down, Turn Left Right",
            key=KN.SCROLOCK_ON(f"{KN.UP}, {KN.DOWN}, {KN.LEFT}, {KN.RIGHT}"),
        ) as self.hk_all_move_up_down_turn_left_right:
            with hk.SendLabel(
                to=self.lbs_all,
            ):
                act.General.TRIGGER()

    def build_hk_non_tank_move_up_down_turn_left_right(self: "Mode"):
        """
        按下 Ctrl + 上下左右方向键, 非坦克职业按下同样的键. 用于实现非坦克职业进行走位躲避技能.
        """
        with hk.MovementHotkey(
            id="Non Tank Move Up Down, Turn Left Right",
            key=KN.SCROLOCK_ON(KN.CTRL_(f"{KN.UP}, {KN.DOWN}, {KN.LEFT}, {KN.RIGHT}")),
        ) as self.hk_non_tank_move_up_down_turn_left_right:
            with hk.SendLabel(
                to=self.lbs_by_tc(TC.non_tank),
            ):
                act.General.TRIGGER()

    def build_hk_non_tank_move_left_right(self: "Mode"):
        """
        按下 Ctrl + A / D, 非坦克职业进行 Q / E 平移, 走位躲避技能.
        """
        with hk.MovementHotkey(
            id="Non Tank Move Left",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.A)),
        ) as self.hk_non_tank_move_left:
            with hk.SendLabel(
                to=self.lbs_by_tc(TC.non_tank),
            ):
                act.Movement.MOVE_LEFT()

        with hk.MovementHotkey(
            id="Non Tank Move Right",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.D)),
        ) as self.hk_non_tank_move_right:
            with hk.SendLabel(
                to=self.lbs_by_tc(TC.non_tank),
            ):
                act.Movement.MOVE_RIGHT()

    def build_hk_all_jump(self: "Mode"):
        with hk.MovementHotkey(
            id="All Jump",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.SPACE)),
        ) as self.hk_all_jump:
            with hk.SendLabel(
                to=self.lbs_all,
            ):
                act.Movement.JUMP()

    def build_hk_spread_matrix(self: "Mode"):
        """
        **矩阵分散站位***

        角色分队

        G1: 防骑, 奶德, 法师, 猎人, 术士
        G2: DK坦, 奶骑, 萨满, 暗牧, 鸟德: 奶骑组群刷不厉害, 所以需要萨满, 暗牧辅助

        以下矩阵分散站位适用于所有人在Boss的一侧进行分散的情形. 典型的Boss战有:

        Naxx 蜘蛛1, 2; ICC 亡语女士
        ICC 亡语女士, 萨鲁法尔, 血腥女王

        先按下 "[" 键进行矩阵分散, 然后按下 "]" 将 法师和暗牧移动到边缘.

                   防骑   DK坦

              术士     猎人     元素萨

        法师    奶德     鸟德    奶骑     暗牧
        """
        # 人数少于 5 人时, 做精细化处理
        if len(self.lbs_all) <= 5:
            lbs_all = self.lbs_all
            lbs_healer = self.lbs_by_tc(TC.healer)
            self.remove_leader_labels(lbs_all)
            self.remove_leader_labels(lbs_healer)
            if len(lbs_healer):
                lb_healer = lbs_healer[0]
                lbs_all.remove(lb_healer)
                if lbs_all:
                    self._go_left(lbs_all[-1])
                    lbs_all.pop()
                if lbs_all:
                    self._go_right(lbs_all[-1])
                    lbs_all.pop()
                if lbs_all:
                    self._go_down(lbs_all[-1])
                    lbs_all.pop()
            else:
                if lbs_all:
                    self._go_left_down(lbs_all[-1])
                    lbs_all.pop()
                if lbs_all:
                    self._go_left(lbs_all[-1])
                    lbs_all.pop()
                if lbs_all:
                    self._go_right(lbs_all[-1])
                    lbs_all.pop()
                if lbs_all:
                    self._go_right_down(lbs_all[-1])
                    lbs_all.pop()

        # 人数大于 5 人时, 用矩阵分散
        else:
            with hk.MovementHotkey(
                id="Spread Matrix 1",
                key=KN.SCROLOCK_ON(KN.OEM4_SQUARE_BRACKET_LEFT),
            ) as self.hk_spread_matrix_1:
                send_label_list: T.List[hk.SendLabel] = [
                    self._go_left([6, 15, 14]),
                    self._go_right([3, 11, 18]),
                    self._go_left_down([4, 8, 16, 13]),
                    self._go_right_down([5, 9, 12, 17]),
                    self._go_down(
                        [
                            2,
                        ]
                    ),
                ]
                for send_label in send_label_list:
                    self.remove_inactive_labels(send_label.to)

            with hk.MovementHotkey(
                id="Spread Matrix 2",
                key=KN.SCROLOCK_ON(KN.OEM6_SQUARE_BRACKET_RIGHT),
            ) as self.hk_spread_matrix_2:
                send_label_list: T.List[hk.SendLabel] = [
                    self._go_left([4, 11, 12]),
                    self._go_right([5, 15, 16]),
                ]
                for send_label in send_label_list:
                    self.remove_inactive_labels(send_label.to)

    def build_hk_spread_circle(self: "Mode"):
        """
        **环形分散站位**

        以下环形分散站位适用于所有人相互距离8码, 而又需要小范围的移动而躲避技能的情况. 典型的Boss战有:

        - Naxx 克尔苏加德
        - ICC 烂肠, 腐面, 血亲王议会

        按下该快捷键后, 大家会分别向, 上下左右, 斜线方向移动, 并且面朝一致的方向, 也就是可以
        保持圆形队形不变向前后移动. 此适用于无法预先安排好阵型, 而需要在战斗中走到指定位置的情形.
        按下快捷键分散后, 大家离中心的距离其实是不一样的, 有的远有的近. 此时再按下跟随焦点键,
        所有人即可向中心靠拢, 然后再按后退键即可实现一个环形站位, 且环形大小可以通过前进后退进行调整.

                    鸟德/奶德2
            猎人                暗牧
                      DK坦
        奶德          boss          奶骑
                      防骑
            法师                元素萨
                    术士/奶德3
        """
        with hk.MovementHotkey(
            id="Spread Circle",
            key=KN.SCROLOCK_ON(KN.OEM5_PIPE_OR_BACK_SLASH),
        ) as self.hk_spread_circle1:
            send_label_list: T.List[hk.SendLabel] = [
                self._go_up([3, 14, 15]),
                self._go_down([6, 11, 18]),
                self._go_left([8, 12, 16]),
                self._go_right([9, 13, 17]),
                self._go_left_up([7, 19]),
                self._go_left_down([4, 20]),
                self._go_right_up([5, 21]),
                self._go_right_down([2, 22]),
            ]
            for send_label in send_label_list:
                self.remove_tank_labels(send_label.to)
                self.remove_inactive_labels(send_label.to)

    def build_hk_group_02_movement_mixin(self: "Mode"):
        self.build_hk_all_move_up_down_turn_left_right()
        self.build_hk_non_tank_move_up_down_turn_left_right()
        self.build_hk_non_tank_move_left_right()
        self.build_hk_all_jump()
        self.build_hk_spread_matrix()
        self.build_hk_spread_circle()
