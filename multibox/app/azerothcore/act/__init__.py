# -*- coding: utf-8 -*-

"""
本模块定义了各个人物, 职业的详细动作条设置, 哪个技能以及哪个宏应该绑定什么快捷键.

本模块还实现了 Key 和 Mouse 行为的抽象化, 用人类可读, 有具体含义的代码, 形如:
``Paladin.Protection.Hammer_of_the_Righteous`` 这样的代码来代替意义不明确的 ``<Key 1>``.
使得 Hotkey 代码本身就能反映出想要实现的功能, 避免了写注释, 避免了保持注释和代码一致的麻烦.

注: 在游戏中按照本模块的设置绑定好所有按键后, 一定要记得备份 WFT 中的配置文件, 以及 Domino
动作条的数据文件.

**开发者注意**

请参考 :meth:`hotkeynet.script.Block.__enter__` 中的文档. 因为上下文机制的存在,
这里所有的属性都 **不能够** 直接定义预先被创建好的 Block 实例. 而是要用工厂函数定义成
一个函数. 这样才能保证被引用的 Block 自动被添加到上下文中去.

**用户注意**

该模块是一套 Act 的模版. 你会发现所有的按键名都被定义, 但是值都是 None. 请拷贝后再在拷贝上
修改. 这里的 :mod:`multibox.game.wow.wlk.act` 模块中的代码请不要动!
"""

from .common import (
    Movement,
    PetAction,
    Target,
    target_leader_key_mapper,
    Camera,
    System,
    General,
)
from .paladin import (
    Paladin,
    PaladinRetribution,
    PaladinProtection,
    PaladinHoly,
)
from .dk import (
    DK,
    DKBlood,
    DKFrost,
    DKUnholy,
)
from .shaman import (
    Shaman,
    ShamanElementalCombat,
    ShamanEnhancement,
    ShamanRestoration,
)
from .hunter import (
    Hunter,
    HunterBeastMastery,
    HunterMarksmanship,
    HunterSurvival,
)
from .druid import (
    Druid,
    DruidBalance,
    DruidRestoration,
    DruidFeral,
)
from .warlock import (
    Warlock,
    WarlockAffliction,
    WarlockDemonology,
    WarlockDestruction,
)
from .mage import (
    Mage,
    MageArcane,
    MageFire,
    MageFrost,
)
from .priest import (
    Priest,
    PriestDiscipline,
    PriestHoly,
    PriestShadow,
)
