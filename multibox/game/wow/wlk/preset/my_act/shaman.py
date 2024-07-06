# -*- coding: utf-8 -*-

from hotkeynet.api import CAN

# fmt: off
class ElementalCombat:
    # 元素系主打技能
    Lightning_Bolt = None  # 闪电箭
    Chain_Lightning = None  # 闪电链
    Lava_Burst = None  # 熔岩爆发
    Thunderstorm = None  # 雷霆风暴, 元素系天赋技能

    # 震击
    Flame_Shock = None  # 火焰震击
    Earth_Shock = None  # 大地震击
    Frost_Shock = CAN.Z  # 冰霜震击

    Elemental_Mastery = CAN.SHIFT_C  # 元素掌握, 增加施法速度, 爆发技能, 元素系天赋技能
    Fire_Nova = CAN.CTRL_X  # 火焰新星, 火系图腾 AOE 伤害
    Hex = CAN.CTRL_E  # 妖术
    Purge = CAN.CTRL_R  # 净化术

    # 图腾
    Searing_Totem = None  # 灼热图腾, 攻击周围敌人
    Magma_Totem = None  # 熔岩爆裂图腾, 周期性 AOE 伤害
    Stoneclaw_Totem = CAN.SHIFT_F1  # 石爪图腾, 嘲讽周围敌人保护施法者
    Earthbind_Totem = CAN.SHIFT_F  # 地缚图腾, 进入范围内的敌人减速
    Wind_Shear = CAN.R  # 削风术, 打断敌人施法
    """
    风剪术 宏, 没有焦点时对目标打断, 有焦点时焦点打  断 (如果焦点是敌人则打断敌人, 如果是友方则打断焦点的目标)::

        #showtooltip
        /stopcasting
        /cast [target=focus,harm] Wind Shear; [target=focustarget,harm] Wind Shear; [] Wind Shear
    """

    Fire_Elemental_Totem = None  # 火元素图腾
    Totem_of_Wrath = CAN.ALT_E  # 愤怒图腾, 增加周围友军的法伤, 元素系天赋技能

    Call_of_the_Ancestors = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 一次性插 4 个图腾, 组合 1
    Call_of_the_Elements = None  # 一次性插 4 个图腾, 组合 2
    Call_of_the_Spirits = None  # 一次性插 4 个图腾, 组合 3


class Enhancement:
    # 增强系主打技能
    Stormstrike = None  # 风暴打击, 同时用双手武器攻击, 增强西天赋技能
    Lava_Lash = None  # 熔岩猛击, 用副手武器攻击, 增强系天赋技能

    Bloodlust_or_Heroism = CAN.CTRL_F  # 嗜血 / 英勇, 为团队提高急速
    Astral_Recall = None  # 先祖召回, 跟炉石一样
    Far_Sight = None  # 远视
    Feral_Spirit = None  # 召唤幽灵狼, 增强系天赋技能

    # 抗性图腾
    Fire_Resistance_Totem = None  # 火焰抗性图腾
    Frost_Resistance_Totem = None  # 冰霜抗性图腾
    Nature_Resistance_Totem = None  # 自然抗性图腾

    Stoneskin_Totem = None  # 石肤图腾, 为周围的团队成员增加护甲
    Strength_of_Earth_Totem = None  # 大地之力图腾, 为周围的团队成员增加力量敏捷
    Flametongue_Totem = None  # 火舌图腾, 为周围的团队成员增加法伤
    Windfury_Totem = None  # 风怒图腾, 为周围的团队成员增加近战急速
    Wrath_of_Air_Totem = None  # 空气之怒图腾, 为周围的团队成员增加施法急速
    Sentry_Totem = None  # 哨兵图腾, 可以切换视野
    Grounding_Totem = CAN.SHIFT_G  # 根基图腾, 吸收指向性技能
    Earth_Elemental_Totem = None  # 土元素图腾

    # 武器 Buff
    Flametongue_Weapon = None  # 火舌武器, 增加法伤, 攻击时带火焰伤害
    Frostbrand_Weapon = None  # 冰霜武器, 攻击时带减移动速度
    Rockbiter_Weapon = None  # 石化武器, 提高武器伤害
    Windfury_Weapon = None  # 风怒武器, 让你的攻击有可能触发连击效果

    Lightning_Shield = CAN.G  # 闪电盾
    Ghost_Wolf = CAN.SHIFT_R  # 变形幽灵狼

    Water_Breathing = None  # 水下呼吸
    Water_Walking = None  # 水上行走

    Shamanistic_Rage = None  # 萨满之怒, 天赋技能, 减伤并为普通攻击增加回蓝效果


class Restoration:
    # 恢复系主打技能
    Earth_Shield = CAN.ALT_G  # 大地之盾, 当被保护的人受到伤害时治疗他, 恢复系天赋技能
    Healing_Wave = CAN.ALT_X  # 治疗波
    Lesser_Healing_Wave = CAN.X  # 次级治疗波
    Chain_Heal = CAN.CTRL_G  # 治疗链
    Riptide = CAN.KEY_5  # 激流, 恢复系天赋技能

    Ancestral_Spirit = None  # 先祖灵魂, 复活
    Cleanse_Spirit = CAN.T  # 净化灵魂, 驱散 中毒, 疾病, 诅咒, 恢复系天赋技能
    Cure_Toxins = CAN.T  # 驱毒术, 驱散 中毒, 疾病

    Earthliving_Weapon = None  # 大地生命武器,

    Healing_Stream_Totem = None  # 治疗之泉图腾
    Mana_Spring_Totem = None  # 法力之泉图腾
    Cleansing_Totem = CAN.ALT_F2  # 净化图腾, 周期性为小队成员驱散 中毒, 疾病
    Mana_Tide_Totem = CAN.ALT_E  # 法力之潮图腾, 恢复系天赋技能
    Tremor_Totem = CAN.ALT_F1  # 战栗图腾, 周期性为小队驱散恐惧
    Totemic_Recall = CAN.SHIFT_TAB  # 召回图腾

    Nature_s_Swiftness = CAN.ALT_F  # 自然迅捷, 使下一个自然法术瞬发, 恢复系天赋技能
    Tidal_Force = CAN.SHIFT_C  # 潮汐之力, 恢复系天赋技能

    Water_Shield = CAN.G  # 水之护盾


class Healbot:
    HB_Healing_Wave = CAN.LEFT_CLICK  # 治疗波
    HB_Lesser_Healing_Wave = CAN.ALT_LEFT_CLICK  # 次级治疗波
    HB_Chain_Heal_for_mbox = CAN.MIDDLE_CLICK  # 治疗链
    HB_Chain_Heal_for_human = CAN.SHIFT_LEFT_CLICK  # 治疗链
    HB_Cleanse_Spirit = CAN.CTRL_LEFT_CLICK  # 净化灵魂, 驱散 中毒, 疾病, 诅咒, 恢复系天赋技能
    HB_Cure_Toxins = CAN.CTRL_LEFT_CLICK  # 驱毒术, 驱散 中毒, 疾病
    HB_Earth_Shield = CAN.ALT_RIGHT_CLICK  # 大地之盾, 当被保护的人受到伤害时治疗他, 恢复系天赋技能
    HB_Riptide = CAN.RIGHT_CLICK  # 激流, 恢复系天赋技能


class Shaman(ElementalCombat, Enhancement, Restoration, Healbot):
    pass


class ShamanElementalCombat(Shaman):
    Thunderstorm = CAN.ALT_F  # 雷霆风暴, 元素系天赋技能
    Elemental_Mastery = CAN.SHIFT_C  # 元素掌握, 增加施法速度, 爆发技能, 元素系天赋技能
    Totem_of_Wrath = CAN.ALT_E  # 愤怒图腾, 增加周围友军的法伤, 元素系天赋技能
    Water_Shield = CAN.G

    HB_Cure_Toxins = CAN.CTRL_LEFT_CLICK  # 驱毒术, 驱散 中毒, 疾病


class ShamanEnhancement(Shaman):
    Stormstrike = None  # 风暴打击, 同时用双手武器攻击, 增强西天赋技能
    Lava_Lash = None  # 熔岩猛击, 用副手武器攻击, 增强系天赋技能
    Feral_Spirit = CAN.ALT_E  # 召唤幽灵狼, 增强系天赋技能
    Shamanistic_Rage = CAN.ALT_F  # 萨满之怒, 天赋技能, 减伤并为普通攻击增加回蓝效果
    Lightning_Shield = CAN.G

    HB_Cure_Toxins = CAN.CTRL_LEFT_CLICK  # 驱毒术, 驱散 中毒, 疾病


class ShamanRestoration(Shaman):
    Earth_Shield = CAN.ALT_G  # 大地之盾, 当被保护的人受到伤害时治疗他, 恢复系天赋技能
    Riptide = CAN.KEY_5  # 激流, 恢复系天赋技能
    Cleanse_Spirit = CAN.T  # 净化灵魂, 驱散 中毒, 疾病, 诅咒, 恢复系天赋技能
    Mana_Tide_Totem = CAN.ALT_E  # 法力之潮图腾, 恢复系天赋技能
    Nature_s_Swiftness = CAN.ALT_F  # 自然迅捷, 使下一个自然法术瞬发, 恢复系天赋技能
    Tidal_Force = CAN.SHIFT_C  # 潮汐之力, 恢复系天赋技能
    Water_Shield = CAN.G

    HB_Cleanse_Spirit = CAN.CTRL_LEFT_CLICK  # 净化灵魂, 驱散 中毒, 疾病, 诅咒, 恢复系天赋技能
    HB_Earth_Shield = CAN.ALT_RIGHT_CLICK  # 大地之盾, 当被保护的人受到伤害时治疗他, 恢复系天赋技能
    HB_Riptide = CAN.RIGHT_CLICK  # 激流, 恢复系天赋技能

    MB_SLOW_HEAL = CAN.KEY_1
    """
    以 15 秒为一个循环 (因为一般大地之盾 15 秒就可以补了) 的治疗宏. 用于慢慢治疗单目标 (主要是坦克).
    
    宏命令的例子如下::
    
        #showtooltip
        /castsequence [nochanneling] reset=target 大地之盾,,次级治疗波,,次级治疗波,,次级治疗波
    """

    MB_HEAL_RAID = CAN.KEY_2
    """
    恢复萨的治疗循环. 无脑随机选择团队目标, 在激流6 秒CD的周期内完成一个循环. 平时该宏如下::
    
        #showtooltip
        #/targetraid
        /castsequence reset=6 激流,治疗链,治疗波,次级治疗波
    
    在长时间的的战斗中为了保证不空蓝, 可以在循环中穿插不耗蓝的水之盾技能, 降低蓝耗::
    
        #showtooltip
        #/targetraid
        /castsequence reset=6 激流,治疗链,水之护盾,治疗波,次级治疗波
    
    甚至可以更极端一点::
    
        #showtooltip
        #/targetraid
        /castsequence reset=6 激流,治疗链,水之护盾,治疗波,次级治疗波,水之护盾
    """

    MB_FAST_HEAL = CAN.KEY_3
    """
    单体快速治疗. 一般放一个 "治疗波" 技能就可以了, 不需要宏.
    """

    MB_Periodical_Refresh_Earth_Shield_on_Tank_Macro = CAN.KEY_4
    """
    按概率给坦克刷新大地之盾. 一般需要一个 castsequence 宏, 除了房大地之盾技能还要放很多空的逗号
    用于模拟概率.
    """

    MB_AOE_HEAL = CAN.KEY_5
    """
    群体治疗, 一般放一个 "治疗链" 技能就可以了.
    """

# fmt: on
