# -*- coding: utf-8 -*-

from hotkeynet.api import CAN

# fmt: off
class Arcane:
    # 奥系主打攻击技能
    Arcane_Missiles = CAN.KEY_1  # 奥术飞弹
    Arcane_Blast = CAN.KEY_2  # 奥术冲击
    Arcane_Barrage = CAN.ALT_F  # 奥术弹幕, 奥系天赋技能

    Arcane_Explosion = CAN.Z  # 奥术爆炸
    Presence_of_Mind = CAN.ALT_F1  # 气定神闲, 下一个法术瞬发, 奥系天赋技能
    Arcane_Power = CAN.ALT_F2  # 奥术强化, 俗称奥强, 奥系天赋技能

    Slow = CAN.G  # 缓速术

    # Buff
    Arcane_Intellect = None  # 奥术智力
    Arcane_Brilliance = None  # 奥术光辉
    Amplify_Magic = CAN.KEY_3  # 法力增效
    Dampen_Magic = CAN.ALT_3  # 魔法抑制
    Focus_Magic = CAN.ALT_Z  # 专注魔法, 奥系天赋技能

    Mage_Armor = None  # 法师护甲
    Blink = CAN.SHIFT_R  # 闪现术
    Counterspell = CAN.R  # 魔法反制
    """
    智能魔法反制宏::
    
        #showtooltip
        /stopcasting
        /cast [target=focus,harm] Counter Spell; [target=focustarget,harm] Counter Spell; [] Counter Spell
    """
    Remove_Curse = CAN.T  # 移除诅咒
    Evocation = CAN.CTRL_F  # 唤醒
    Invisibility = CAN.ALT_E  # 隐身术
    Mirror_Image = CAN.SHIFT_F2  # 镜像术
    Mana_Shield = CAN.ALT_5  # 法力护盾
    Polymorph = CAN.CTRL_E  # 变形术
    Slow_Fall = CAN.ALT_T  # 缓落术
    Spellsteal = CAN.CTRL_R  # 偷取魔法

    Conjure_Mana_Gem = None  # 制造法力宝石
    Conjure_Food = None  # 制造魔法食物
    Conjure_Water = None  # 制造魔法饮料
    Conjure_Refreshment = None  # 制造魔法餐点
    Ritual_of_Refreshment = None  # 召唤餐点仪式

    Teleport_Dalaran = None  # 传送 达拉然
    Teleport_Darnassus_Alliance = None  # 传送 达纳苏斯
    Teleport_Exodar_Alliance = None  # 传送 埃索达
    Teleport_Ironforge_Alliance = None  # 传送 铁炉堡
    Teleport_Orgrimmar_Horde = None  # 传送 奥格瑞玛
    Teleport_Shattrath_Alliance = None  # 传送 沙塔斯城
    Teleport_Shattrath_Horde = None  # 传送 沙塔城
    Teleport_Silvermoon_Horde = None  # 传送 银月城
    Teleport_Stonard_Horde = None  # 传送 斯通纳德
    Teleport_Stormwind_Alliance = None  # 传送 暴风城
    Teleport_Theramore_Alliance = None  # 传送 塞拉摩
    Teleport_Thunder_Bluff_Horde = None  # 传送 雷霆崖
    Teleport_Undercity_Horde = None  # 传送 幽暗城

    Portal_Dalaran = None  # 传送门 达拉然
    Portal_Darnassus_Alliance = None  # 传送门 达纳苏斯
    Portal_Exodar_Alliance = None  # 传送门 埃索达
    Portal_Ironforge_Alliance = None  # 传送门 铁炉堡
    Portal_Orgrimmar_Horde = None  # 传送门 奥格瑞玛
    Portal_Shattrath_Alliance = None  # 传送门 沙塔斯城
    Portal_Shattrath_Horde = None  # 传送门 沙塔城
    Portal_Silvermoon_Horde = None  # 传送门 银月城
    Portal_Stonard_Horde = None  # 传送门 斯通纳德
    Portal_Stormwind_Alliance = None  # 传送门 暴风城
    Portal_Theramore_Alliance = None  # 传送门 塞拉摩
    Portal_Thunder_Bluff_Horde = None  # 传送门 雷霆崖
    Portal_Undercity_Horde = None  # 传送门 幽暗城


class Fire:
    # 火系主打攻击技能
    Fireball = CAN.KEY_2  # 火球术
    Fire_Blast = CAN.KEY_3  # 火焰冲击
    Scorch = CAN.ALT_3  # 灼烧
    Pyroblast = CAN.KEY_1  # 炎爆术, 火系天赋技能
    Living_Bomb = CAN.G  # 活体炸弹, 火系天赋技能
    Frostfire_Bolt = CAN.CTRL_X  # 霜火箭

    # AOE
    Flamestrike = CAN.X  # 烈焰风暴
    Blast_Wave = CAN.ALT_G  # 冲击波, 火系天赋技能
    Dragon_s_Breath = CAN.ALT_F  # 龙息术, 火系天赋技能

    Molten_Armor = None  # 熔岩护甲
    Combustion = CAN.SHIFT_C  # 燃魂, 火系天赋技能
    Fire_Ward = CAN.SHIFT_F  # 火焰防护结界


class Frost:
    # 冰系主打攻击技能
    Frostbolt = CAN.KEY_2  # 寒冰箭
    Ice_Lance = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 冰枪术
    Deep_Freeze = CAN.ALT_F  # 深度冻结, 冰系天赋技能

    # AOE
    Cone_of_Cold = CAN.KEY_5  # 冰锥术
    Blizzard = CAN.ALT_X  # 暴风雪
    Frost_Nova = CAN.KEY_4  # 冰霜新星

    # 爆发技能
    Icy_Veins = CAN.SHIFT_C  # 冰冷血脉, 使你的施法速度提高, 冰系天赋技能
    Cold_Snap = None  # 急速冷却, 重置你的冰系技能 CD, 冰系天赋技能

    # 防护技能
    Ice_Armor = None  # 冰甲术
    Frost_Ward = CAN.SHIFT_G  # 冰霜防护结界
    Ice_Barrier = CAN.ALT_5  # 寒冰护盾, 冰系天赋技能
    Ice_Block = CAN.SHIFT_F1  # 寒冰屏障, 俗称冰箱

    Summon_Water_Elemental = CAN.G  # 召唤水元素
    Water_Elemental_Nova = CAN.ALT_G  # 水元素的冰冻术技能


class Healbot:
    HB_Amplify_Magic = None  # 法力增效
    HB_Dampen_Magic = None  # 魔法抑制
    HB_Remove_Curse_for_mbox = CAN.MIDDLE_CLICK  # 移除诅咒
    HB_Remove_Curse = CAN.CTRL_LEFT_CLICK  # 移除诅咒
    HB_Focus_Magic = CAN.RIGHT_CLICK  # 专注魔法, 奥系天赋技能


class Mage(Arcane, Fire, Frost, Healbot):
    pass


class MageArcane(Mage):
    Arcane_Barrage = CAN.ALT_F  # 奥术弹幕, 奥系天赋技能
    Presence_of_Mind = CAN.ALT_F1  # 气定神闲, 下一个法术瞬发, 奥系天赋技能
    Arcane_Power = CAN.ALT_G  # 奥术强化, 俗称奥强, 奥系天赋技能
    Slow = CAN.G  # 缓速术


class MageFire(Mage):
    Pyroblast = CAN.KEY_1  # 炎爆术, 火系天赋技能
    Living_Bomb = CAN.G  # 活体炸弹, 火系天赋技能
    Blast_Wave = CAN.ALT_G  # 冲击波, 火系天赋技能
    Dragon_s_Breath = CAN.ALT_F  # 龙息术, 火系天赋技能
    Combustion = CAN.SHIFT_C  # 燃魂, 火系天赋技能


class MageFrost(Mage):
    Deep_Freeze = CAN.ALT_F  # 深度冻结, 冰系天赋技能
    Icy_Veins = CAN.SHIFT_C  # 冰冷血脉, 使你的施法速度提高, 冰系天赋技能
    Cold_Snap = None  # 急速冷却, 重置你的冰系技能 CD, 冰系天赋技能
    Summon_Water_Elemental = CAN.G  # 召唤水元素
    Water_Elemental_Nova = CAN.ALT_G  # 水元素的冰冻术技能
# fmt: on
