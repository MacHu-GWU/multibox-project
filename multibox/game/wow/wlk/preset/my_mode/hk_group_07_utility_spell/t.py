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
        **说明**

        所有有驱散技能的职业随机选择团队成员并释放驱散技能. 对应的技能如下:

        1. 圣骑士: 净化术 (魔法, 中毒, 疾病)
        2. 恢复萨满: 净化灵魂 (诅咒, 中毒, 疾病)
        3. 非恢复萨满: 驱毒术 (中毒, 疾病)
        4. 德鲁伊: 驱散诅咒 (诅咒)
        5. 法师: 驱散诅咒 (诅咒)
        6. 牧师: 驱散魔法 (魔法)

        由于 /targetraid 宏无法选中自己, 所以一般要保证每种类型的驱散必须有起码 2 个职业负责.
        而对于中毒和疾病, 由于萨满的净化图腾的存在, 基本可以做到全团秒驱.

        **使用方法**

        不停地按就会随机选择团队成员并释放驱散技能.

        **动作条安排**

        - 动作条按钮上就是对应的驱散技能.
        - 动作条按钮要绑定 ``T`` 快捷键, 并确保每个职业的打断技能按钮都是 T.
        """
        with hk.Hotkey(
            id="T - 所有驱散职业随机选择团队成员驱散",
            key=KN.SCROLOCK_ON(KN.T),
        ) as self.hk_t_dispel_raid:
            with hk.SendLabel(
                id="T - 所有驱散职业随机选择团队成员驱散",
                to=self.get_lbs_by_tc(TC.dispeler),
            ):
                act.Target.TARGET_RAID()
                hk.Key.trigger()

    def build_t_mixin(self: "Mode"):
        if self.name == "special_mode":
            raise NotImplementedError
        else:
            self.build_hk_default_t()
