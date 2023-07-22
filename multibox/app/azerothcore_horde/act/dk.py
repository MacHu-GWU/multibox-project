# -*- coding: utf-8 -*-

from hotkeynet.api import CAN


class Blood:
    # 鲜血系系主打技能
    Blood_Presence = CAN.SHIFT_Q  # 血之领域
    Blood_Strike = CAN.KEY_1  # 鲜血打击
    Heart_Strike = CAN.KEY_1  # 心脏打击, 鲜血系天赋技能

    # 天赋技能
    Rune_Tap = CAN.T  # 符文分流, 瞬发治疗技能, 鲜血系天赋技能
    Mark_of_Blood = CAN.ALT_F  # 鲜血印记, 鲜血系天赋技能
    Hysteria = CAN.SHIFT_C  # 狂血术, 鲜血系天赋技能
    Vampiric_Blood = CAN.SHIFT_F2  # 吸血鬼之血, 类似战士的破釜沉舟, 鲜血系天赋技能
    Dancing_Rune_Weapon = CAN.CTRL_F  # 召唤符文武器, 鲜血系天赋技能

    # 其他
    Dark_Command = CAN.Z  # 黑暗命令, 嘲讽
    Pestilence = CAN.ALT_1  # 传染
    Blood_Boil = CAN.KEY_5  # 血液沸腾, AOE 伤害
    Death_Pact = None  # 血之契约
    Blood_Tap = None  # 鲜血分流
    Strangulate = None  # 绞袭


class Frost:
    # 冰霜系主打技能
    Frost_Presence = CAN.SHIFT_W  # 冰霜领域
    Icy_Touch = CAN.KEY_2  # 冰冷触摸, 在冰霜领域下高仇恨技能, 散播冰霜疫病
    Obliterate = CAN.ALT_4  # 湮没

    # 天赋技能
    Lichborne = None  # 巫妖之躯, 冰霜系天赋技能
    Deathchill = None  # 黑锋冰寒
    Hungering_Cold = CAN.CTRL_F  # 饥饿之寒, 群体控制
    Unbreakable_Armor = CAN.SHIFT_F2  # 铜墙铁壁, 提高护甲和力量, 冰霜系天赋技能
    Frost_Strike = CAN.ALT_3  # 冰霜打击, 冰霜系天赋技能, 替代死亡缠绕
    Howling_Blast = None  # 凛风冲击, 冰霜系天赋技能

    # 其他
    Chains_of_Ice = CAN.CTRL_E  # 寒冰锁链
    Empower_Rune_Weapon = CAN.CTRL_F  # 强化符文武器
    Horn_of_Winter = CAN.SHIFT_TAB  # 寒冬号角, buff 技能

    Icebound_Fortitude = CAN.SHIFT_F1  # 冰固坚韧, 减伤技能
    Mind_Freeze = CAN.R  # 心灵冰冻, 打断施法技能
    Path_of_Frost = None  # 冰霜之径, 群体水上行走
    Rune_Strike = CAN.ALT_E  # 符文打击, 高仇恨技能, 只能在躲闪招架之后使用


class Unholy:
    # 邪恶系主打技能
    Unholy_Presence = CAN.SHIFT_E  # 邪恶领域
    Plague_Strike = CAN.KEY_3  # 瘟疫打击, 散播血之疫病
    Death_Strike = CAN.KEY_4  # 死之打击, 按照疾病数量回血
    Scourge_Strike = CAN.ALT_4  # 天灾打击
    Death_Coil = CAN.ALT_3  # 死亡缠绕

    # 天赋技能
    Ghoul_Frenzy = None  # 食尸鬼狂乱
    Anti_Magic_Zone = CAN.SHIFT_G  # 反魔法领域
    Bone_Shield = CAN.SHIFT_F2  # 骨盾
    Summon_Gargoyle = CAN.SHIFT_C  # 召唤石像鬼
    Corpse_Explosion = None  # 尸体爆炸

    # 其他
    Anti_Magic_Shell = CAN.SHIFT_F  # 反魔法护盾
    Army_of_the_Dead = None  # 亡者大军
    Death_and_Decay = CAN.ALT_X  # 死亡凋零
    Death_Gate = None  # 死亡之门
    Death_Grip = CAN.G  # 死亡之握

    Raise_Ally = CAN.CTRL_G  # 复活友军
    Raise_Dead = CAN.CTRL_X  # 复活死者


class Healbot:
    pass


class DK(Blood, Frost, Unholy, Healbot):
    pass


class DKBlood(DK):
    Heart_Strike = CAN.KEY_1  # 心脏打击, 鲜血系天赋技能
    Rune_Tap = CAN.T  # 符文分流, 瞬发治疗技能, 鲜血系天赋技能
    Mark_of_Blood = CAN.ALT_F  # 鲜血印记, 鲜血系天赋技能
    Hysteria = CAN.SHIFT_C  # 狂血术, 鲜血系天赋技能
    Vampiric_Blood = CAN.SHIFT_F2  # 吸血鬼之血, 类似战士的破釜沉舟, 鲜血系天赋技能
    Dancing_Rune_Weapon = CAN.CTRL_F  # 召唤符文武器, 鲜血系天赋技能


class DKFrost(DK):
    Lichborne = None  # 巫妖之躯, 冰霜系天赋技能
    Deathchill = CAN.SHIFT_C  # 黑锋冰寒
    Hungering_Cold = CAN.CTRL_F  # 饥饿之寒, 群体控制
    Unbreakable_Armor = CAN.SHIFT_F2  # 铜墙铁壁, 提高护甲和力量, 冰霜系天赋技能
    Frost_Strike = CAN.ALT_3  # 冰霜打击, 冰霜系天赋技能, 替代死亡缠绕
    Howling_Blast = CAN.ALT_F  # 凛风冲击, 冰霜系天赋技能


class DKUnholy(DK):
    Scourge_Strike = CAN.ALT_4  # 天灾打击
    Ghoul_Frenzy = None  # 食尸鬼狂乱
    Anti_Magic_Zone = CAN.SHIFT_G  # 反魔法领域
    Bone_Shield = CAN.SHIFT_F2  # 骨盾
    Summon_Gargoyle = CAN.SHIFT_C  # 召唤石像鬼


dk = DK()
dk_blood = DKBlood()
dk_frost = DKFrost()
dk_unholy = DKUnholy()
