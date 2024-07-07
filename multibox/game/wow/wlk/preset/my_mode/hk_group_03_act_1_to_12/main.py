# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T

from ordered_set import OrderedSet
import hotkeynet.api as hk
from hotkeynet.api import KN, CAN
import multibox.game.wow.wlk.api as wlk
import multibox.game.wow.wlk.preset.my_act.api as act
from multibox.game.wow.wlk.preset.my_mode.utils import TargetEnum

from .act1 import Act1Mixin
from .act2 import Act2Mixin
from .act3 import Act3Mixin
from .act4 import Act4Mixin
from .act5 import Act5Mixin
from .act6 import Act6Mixin
from .act7 import Act7Mixin

if T.TYPE_CHECKING:  # pragma: no cover
    from ..mode import Mode


def make_default_action_send_label_id(
    key: str,
    talent: wlk.Talent,
) -> str:
    return f"key-{key}-default-action-for-talent-{talent.name}"


class HotkeyGroup03Act1To12Mixin(
    Act1Mixin,
    Act2Mixin,
    Act3Mixin,
    Act4Mixin,
    Act5Mixin,
    Act6Mixin,
    Act7Mixin,
):
    """
    这个类定义了多开时按下 1-12 按键时的行为.

    See:

    - :mod:`multibox.game.wow.wlk.preset.my_mode.hk_group_03_act_1_to_12.act1`
    """

    def build_default_action_by_talents(
        self: "Mode",
        key: str,
        talents: OrderedSet[wlk.Talent],
        target: T.Optional[TargetEnum] = None,
    ) -> T.Dict[str, hk.SendLabel]:
        """
        这是一个用来减少重复代码的工厂函数. 用于生成非常普通的同步按键行为. 例如你按 1,
        那么所有的窗口就也按 1. 由于这也是大多数按键的行为, 在很多地方都会用到这个逻辑,
        所以我们专门设计了一个函数.

        :param key: 按键.
        :param talents: 天赋的集合, 用于筛选出对应的角色的窗口的 label.
        :param target: 可选项, 用于在按键之前选择目标. 默认是不特意选择目标.
            see :class:`~multibox.game.wow.wlk.preset.my_mode.utils.TargetEnum`.
        """
        send_label_mapping = dict()
        for talent in talents:
            lbs = self.get_lbs_by_tl(talent)
            if len(lbs):
                # 这个 id 是为了给开发者一些自定义的空间, 以便在后续的代码中可以根据这个 id
                # 找到对应的 SendLabel 对象然后对其进行修改.
                # 比如你用这样的代码 ``send_label = send_label_mapping["your-id"]``
                # 获得了 send_label 对象之后, 可以用下面的代码对默认行为进行魔改.
                # with send_label():
                #     send_label.blocks = [...]
                # 注意, 这样做会让代码变得更难以理解, 不推荐这么做.
                send_label_id = make_default_action_send_label_id(
                    key=key,
                    talent=talent,
                )
                with hk.SendLabel(
                    id=send_label_id,
                    to=lbs,
                ) as send_label:
                    if target is not None:
                        target.to_key()
                    hk.Key.make(key)
                    send_label_mapping[send_label_id] = send_label
        return send_label_mapping

    def build_tank_default_action(
        self: "Mode",
        key: str,
        target: T.Optional[TargetEnum] = None,
    ) -> T.Dict[str, hk.SendLabel]:
        """
        大多数跟战斗相关的多开按键对于坦克来说都是无需特别选定目标, 都是多开按什么键,
        每个 tank 的窗口就还是按什么键 (通常是技能) 攻击即可.
        """
        return self.build_default_action_by_talents(
            key=key,
            talents=wlk.TC.tank.talents,
            target=target,
        )

    def build_dps_default_action(
        self: "Mode",
        key: str,
        target: T.Optional[TargetEnum] = TargetEnum.TARGET_FOCUS_TARGET,
    ) -> T.Dict[str, hk.SendLabel]:
        """
        大多数跟战斗相关的多开按键对于 DPS 来说都是需要选择焦点的目标, 然后多开按什么键,
        每个 dps 的窗口就还是按什么键 (通常是技能) 攻击即可.
        """
        return self.build_default_action_by_talents(
            key=key,
            talents=wlk.TC.dps.talents,
            target=target,
        )

    def build_healer_default_action(
        self: "Mode",
        key: str,
        target: T.Optional[TargetEnum] = None,
    ) -> T.Dict[str, hk.SendLabel]:
        """
        对于治疗来说具体对哪个目标施放治疗技能取决于特定的技能以及特定的场景. 我们这里不做任何预设.
        """
        return self.build_default_action_by_talents(
            key=key,
            talents=wlk.TC.healer.talents,
            target=target,
        )

    def build_hk_group_03_act_1_to_12_mixin(self: "Mode"):
        self.build_act1()
        self.build_act2()
        self.build_act3()
        self.build_act4()
        self.build_act5()
        self.build_act6()
        self.build_act7()
