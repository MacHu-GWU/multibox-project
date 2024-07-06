# -*- coding: utf-8 -*-

import typing as T

import hotkeynet.api as hk
import multibox.game.wow.wlk.api as wlk

from .act1 import Act1Mixin

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


class HotkeyGroup03Act1To12Mixin(Act1Mixin):
    # def build_actions_default(
    #     self: "Mode",
    #     key: str,
    #     healer_target_nothing: bool = False,
    #     healer_target_focus: bool = False,
    #     healer_target_focus_target: bool = False,
    #     healer_target_self: bool = False,
    #     healer_target_party: bool = False,
    #     healer_target_raid: bool = False,
    # ) -> T.List[hk.SendLabel]:
    #     """
    #     通常情况下, 我们打怪的逻辑是: 坦克拉怪, DPS 输出, 治疗奶. 而我们有那么多键位. 为了
    #     避免为那么多键位写一大堆重复代码, 我们定义了一个工厂函数, 用于生成默认的设置.
    #     简单来说默认设置就是:
    #
    #     1. 坦克对当前选择的怪施放技能
    #     2. DPS 对焦点的目标释放技能
    #     3. 治疗 对某个目标释放技能, 这里的 "某个" 取决于哪个模式. 请参考下面的参数定义:
    #
    #     :param healer_target_nothing: 在施放治疗技能前不选择目标
    #     :param healer_target_focus: 治疗前 (下同), 先选定焦点, 通常是坦克司机
    #     :param healer_target_focus_target: 先选择焦点的目标, 通常是坦克选择队友然后治疗该队友
    #     :param healer_target_self: 先选择自己
    #     :param healer_target_party: 先用宏随机选定小队成员
    #     :param healer_target_raid: 先用宏随机选择团队成员
    #
    #     以上 5 个模式中必须选择其中的一个.
    #
    #     **注**
    #
    #     这里我们需要为所有的 Active Characters 的每一个特定的天赋创建一个 SendLabel 对象.
    #     这和我们之前为一类 TalentCategory 创建一个 SendLabel, 然后在 SendLabel.to
    #     里面指定多个 label 的模式不同. 虽然后者从代码的角度讲更加紧凑, 但是却丧失了之后为
    #     每个特定的天赋在特殊场景下指定不同的行为的能力. 所以我们才用的这种不符合直觉的写法.
    #     """
    #     if (
    #         sum(
    #             [
    #                 healer_target_nothing,
    #                 healer_target_focus,
    #                 healer_target_focus_target,
    #                 healer_target_self,
    #                 healer_target_party,
    #                 healer_target_raid,
    #             ]
    #         )
    #         != 1
    #     ):
    #         raise ValueError()
    #
    #     send_label_list = list()
    #
    #     # Tank
    #     for talent in wlk.TC.tank.talents:
    #         with hk.SendLabel(
    #             id=talent.name,
    #             to=self.lbs_by_tl(talent),
    #         ) as send_label:
    #             hk.Key.make(key)
    #             send_label_list.append(send_label)
    #
    #     # DPS
    #     for talent in TC.dps.talents:
    #         with hk.SendLabel(
    #             id=talent.name,
    #             to=self.lbs_by_tl(talent),
    #         ) as send_label:
    #             act.Target.TARGET_FOCUS_TARGET()
    #             hk.Key.make(key)
    #             send_label_list.append(send_label)
    #
    #     # Healer
    #     for talent in TC.healer.talents:
    #         with hk.SendLabel(
    #             id=talent.name,
    #             to=self.lbs_by_tl(talent),
    #         ) as send_label:
    #             if healer_target_nothing:
    #                 hk.Key.make(key)
    #             elif healer_target_focus:
    #                 act.Target.TARGET_FOCUS()
    #                 hk.Key.make(key)
    #             elif healer_target_focus_target:
    #                 act.Target.TARGET_FOCUS_TARGET()
    #                 hk.Key.make(key)
    #             elif healer_target_self:
    #                 act.Target.TARGET_SELF()
    #                 hk.Key.make(key)
    #             elif healer_target_party:
    #                 act.Target.TARGET_PARTY()
    #                 hk.Key.make(key)
    #             elif healer_target_raid:
    #                 act.Target.TARGET_RAID()
    #                 hk.Key.make(key)
    #             else:  # pragma: no cover
    #                 raise NotImplementedError
    #
    #             send_label_list.append(send_label)
    #
    #     return send_label_list

    def build_hk_group_03_act_1_to_12_mixin(self: "Mode"):
        self.build_act1()
        # self.build_act2()
        # self.build_act3()
        # self.build_act4()
        # self.build_act5()
