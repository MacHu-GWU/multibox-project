# -*- coding: utf-8 -*-

"""
todo: doctstring
"""

import enum
import hotkeynet.api as hk
import multibox.game.wow.wlk.preset.my_act.api as act


class TargetEnum(enum.Enum):
    """
    在构建 HotkeyNet 脚本的代码中, 我们会用到这个枚举类作为一些函数的参数, 更进一步地利用
    type hint 来确保代码的正确性. 这个枚举的 value 都是 ``hotkeynet.api.KeyMaker`` 对象.
    """

    TARGET_FOCUS = act.Target.TARGET_FOCUS
    TARGET_FOCUS_TARGET = act.Target.TARGET_FOCUS_TARGET
    TARGET_FOCUS_TARGET_TARGET = act.Target.TARGET_FOCUS_TARGET_TARGET
    TARGET_SELF = act.Target.TARGET_SELF
    TARGET_PARTY = act.Target.TARGET_PARTY
    TARGET_RAID = act.Target.TARGET_RAID

    def to_key(self) -> hk.Key:
        return self.value()
