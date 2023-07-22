# -*- coding: utf-8 -*-

from hotkeynet.api import CAN


class Affliction:
    # 痛苦系主打技能
    Corruption = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 腐蚀术
    Curse_of_Agony = CAN.ALT_SHIFT_(CAN.OEM3_WAVE_OR_BACK_QUOTE)  # 痛苦诅咒
    Seed_of_Corruption = CAN.R  # 腐蚀之种, AOE 技能
    Unstable_Affliction = None  # 不稳定的痛苦, 痛苦系天赋技能
    Haunt = None  # 鬼影重重, 痛苦系天赋技能

    Death_Coil = CAN.CTRL_F  # 死亡缠绕

    # 诅咒
    Curse_of_Doom = CAN.ALT_E  # 厄运诅咒
    Curse_of_Exhaustion = None  # 疲劳诅咒, 痛苦系天赋技能
    Curse_of_the_Elements = CAN.T  # 元素诅咒
    Curse_of_Tongues = CAN.G  # 语言诅咒
    Curse_of_Weakness = CAN.ALT_T  # 虚弱诅咒

    Drain_Life = CAN.SHIFT_F  # 吸取生命
    Drain_Mana = CAN.SHIFT_G  # 吸取法力
    Drain_Soul = CAN.CTRL_R  # 吸取灵魂碎片

    # 恐惧
    Fear = CAN.CTRL_E  # 恐惧
    Howl_of_Terror = CAN.ALT_F1  # 恐惧咆哮, 群体恐惧

    # 回蓝
    Life_Tap = CAN.Z  # 生命分流, 生命转法力
    Dark_Pact = None  # 黑暗契约, 从宠物身上吸取法力, 痛苦系天赋技能


class Demonology:
    # 恶魔系主打技能
    Metamorphosis = CAN.SHIFT_Q  # 恶魔形态
    Challenging_Howl_Demon = None  # 挑战咆哮, 恶魔形态技能, 恶魔系天赋技能
    Demon_Charge_Demon = None  # 恶魔冲锋, 恶魔形态技能, 恶魔系天赋技能
    Shadow_Cleave_Demon = None  # 暗影顺劈斩, 恶魔形态技能, 恶魔系天赋技能
    Immolation_Aura_Demon = None  # 献祭光环, 恶魔形态技能, 恶魔系天赋技能

    Demonic_Empowerment = CAN.ALT_F  # 恶魔增效, 恶魔系天赋技能
    Soul_Link = None  # 灵魂链接, 让你的恶魔帮你分担受到的伤害, 恶魔系天赋技能

    Create_Firestone = None  # 创造火焰石
    Create_Healthstone = None  # 创造治疗石
    Create_Soulstone = None  # 创造灵魂石
    Create_Spellstone = None  # 创造法术石

    Demon_Armor = None  # 恶魔护甲
    Fel_Armor = CAN.KEY_0  # 邪甲术

    Demonic_Circle_Summon = CAN.ALT_R  # 恶魔之环 召唤
    Demonic_Circle_Teleport = CAN.SHIFT_R  # 恶魔之环 传送
    Ritual_of_Souls = None  # 灵魂仪式, 俗称发糖
    Ritual_of_Summoning = None  # 召唤仪式, 俗称拉人
    Inferno = None  # 召唤地狱火
    Ritual_of_Doom = None  # 末日仪式, 召唤地狱守卫
    Eye_of_KilroggSummon = None  # 基尔罗格之眼

    Detect_Invisibility = None  # 侦测隐形
    Unending_Breath = None  # 水下呼吸

    Sense_Demons = None  # 感知恶魔
    Enslave_Demon = None  # 奴役恶魔
    Fel_Domination = CAN.SHIFT_C  # 恶魔支配, 瞬发召唤恶魔
    Health_Funnel = None  # 生命通道, 治疗你的恶魔

    Shadow_Ward = CAN.SHIFT_F2  # 暗影防护结界
    Soulshatter = CAN.ALT_Z  # 灵魂碎裂, 减仇恨技能

    Banish = CAN.CTRL_X  # 放逐术, 放逐元素生物

    Summon_Imp = None  # 召唤小鬼
    Summon_Voidwalker = None  # 召唤虚空行者
    Summon_Succubus = None  # 召唤魅魔
    Summon_Felhunter = None  # 召唤地狱犬
    Summon_Felguard = None  # 召唤恶魔卫士


class Destruction:
    # 毁灭系主打技能
    Immolate = CAN.KEY_1  # 献祭
    Conflagrate = CAN.KEY_2  # 点燃, 毁灭系天赋技能
    Shadow_Bolt = CAN.KEY_2  # 暗影箭
    Incinerate = CAN.KEY_3  # 烧尽
    Chaos_Bolt = CAN.KEY_5  # 混乱箭, 能穿透伤害吸收盾, 毁灭系天赋技能
    Searing_Pain = CAN.ALT_2  # 灼热之痛, 高仇恨技能

    Shadowburn = None  # 暗影灼烧, 瞬发直接伤害技能, 毁灭系天赋技能
    Shadowflame = CAN.X  # 暗影烈焰, 群体 AOE 技能, 毁灭系天赋技能
    Shadowfury = CAN.ALT_F  # 暗影之怒, 群体控制技能, 毁灭系天赋技能
    Soul_Fire = None  # 灵魂之火

    # AOE
    Hellfire = CAN.CTRL_G  # 地狱火, 俗称自燃
    Rain_of_Fire = CAN.ALT_X  # 火焰之雨


class Healbot:
    pass


class Warlock(Affliction, Demonology, Destruction, Healbot):
    pass


class WarlockAffliction(Warlock):
    Unstable_Affliction = None  # 不稳定的痛苦, 痛苦系天赋技能
    Haunt = None  # 鬼影重重, 痛苦系天赋技能
    Dark_Pact = None  # 黑暗契约, 从宠物身上吸取法力, 痛苦系天赋技能


class WarlockDemonology(Warlock):
    Metamorphosis = CAN.SHIFT_Q  # 恶魔形态
    Challenging_Howl_Demon = None  # 挑战咆哮, 恶魔形态技能, 恶魔系天赋技能
    Demon_Charge_Demon = None  # 恶魔冲锋, 恶魔形态技能, 恶魔系天赋技能
    Shadow_Cleave_Demon = None  # 暗影顺劈斩, 恶魔形态技能, 恶魔系天赋技能
    Immolation_Aura_Demon = None  # 献祭光环, 恶魔形态技能, 恶魔系天赋技能
    Soul_Link = None  # 灵魂链接, 让你的恶魔帮你分担受到的伤害, 恶魔系天赋技能
    Summon_Felguard = None  # 召唤恶魔卫士
    Demonic_Empowerment = CAN.ALT_F  # 恶魔增效, 恶魔系天赋技能
    Fel_Domination = CAN.SHIFT_C  # 恶魔支配, 瞬发召唤恶魔


class WarlockDestruction(Warlock):
    Conflagrate = CAN.KEY_2  # 点燃, 毁灭系天赋技能
    Chaos_Bolt = CAN.KEY_5  # 混乱箭, 能穿透伤害吸收盾, 毁灭系天赋技能
    Shadowburn = None  # 暗影灼烧, 瞬发直接伤害技能, 毁灭系天赋技能
    Shadowfury = CAN.ALT_F  # 暗影之怒, 群体控制技能, 毁灭系天赋技能
