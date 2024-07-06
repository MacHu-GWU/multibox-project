# -*- coding: utf-8 -*-

"""
todo: docstring
"""

from hotkeynet.api import CAN

# fmt: off
class Balance:
    # 平衡系主打技能
    Moonfire = CAN.KEY_1  # 月火术
    Insect_Swarm = CAN.KEY_4  # 虫群, Dot, 平衡系天赋技能
    Wrath = CAN.KEY_2  # 愤怒
    Starfire = CAN.KEY_3  # 星火术
    Hurricane = CAN.ALT_X  # 飓风, 主力 AOE 技能
    Starfall = CAN.ALT_F  # 星落术, 强大的 AOE 技能, 平衡系天赋技能
    Typhoon = CAN.G  # 台风, 俗称推推, 造成伤害并将目标向后退
    Force_of_Nature = None  # 自然之力, 召唤树人, 平衡系天赋技能
    Moonkin_FormShapeshift = CAN.SHIFT_E  # 枭兽形态, 平衡系天赋技能

    # 控制技能
    Cyclone = CAN.ALT_E  # 旋风, 控制技能, 使目标无法做任何动作, 也无法被攻击
    Entangling_Roots = CAN.CTRL_E  # 纠缠根须, 控制技能, 使目标无法移动
    Hibernate = CAN.ALT_T  # 催眠, 控制技能, 只能对动物和龙类使用
    Nature_s_Grasp = None  # 自然之握, 使你被击中后自动召唤纠缠根须定身攻击者

    # 其他
    Barkskin = CAN.SHIFT_F1  # 树皮术
    Faerie_Fire = CAN.R  # 精灵之火, 破隐形, 降低护甲
    Innervate = CAN.CTRL_F  # 激活, 为目标回复大量法力
    Thorns = None  # 荆棘术
    Soothe_Animal = CAN.ALT_Z  # 安抚动物, 使目标的仇恨范围降低
    Teleport_Moonglade = None  # 传送 月光林地


class Restoration:
    # 恢复系主打技能
    Rejuvenation = CAN.Z  # 回春术
    Regrowth = CAN.ALT_3  # 愈合
    Nourish = CAN.KEY_3  # 滋养
    Lifebloom = CAN.KEY_1  # 生命之花, hot, 周期结束后会返回部分蓝耗
    Wild_Growth = CAN.KEY_5  # 野性生长, 群体治疗, 恢复系天赋技能
    Swiftmend = CAN.KEY_4  # 迅捷治愈, 恢复系天赋技能
    Tree_of_LifeShapeshift = CAN.SHIFT_E  # 治疗之树形态

    # Buff
    Gift_of_the_Wild = None  # 野性赐福
    Mark_of_the_Wild = None  # 野性印记

    # 驱散
    Abolish_Poison = CAN.ALT_R  # 驱毒术
    Cure_Poison = None  # 治疗中毒
    Remove_Curse = CAN.T  # 驱散诅咒

    Nature_s_Swiftness = CAN.ALT_F  # 自然迅捷, 下一个技能瞬发, 恢复系天赋技能
    Healing_Touch = None  # 治疗之触

    Revive = None  # 复活
    Rebirth = CAN.CTRL_X  # 战斗复活
    Tranquility = CAN.CTRL_G  # 宁静, 长 CD 小队治疗


class Feral:
    # 熊形态
    Bear_FormShapeshift = CAN.SHIFT_Q  # 熊形态

    # 仇恨技能
    Growl = CAN.ALT_1  # 嘲讽
    Lacerate = CAN.KEY_1  # 割伤, 仇恨技能
    Maul = None  # 锤击, 类似于战士的英勇打击
    Mangle_Bear = CAN.KEY_2  # 裂伤 熊形态, 野性系天赋技能
    Swipe_Bear = CAN.KEY_4  # 扫击 熊形态

    Bash = CAN.KEY_5  # 重击, 使目标昏迷, 控制技能
    Challenging_Roar = CAN.ALT_F2  # 挑战咆哮, 群体嘲讽
    Demoralizing_Roar = None  # 挫志咆哮
    Feral_Charge_Bear = None  # 野性冲锋 熊形态, 野性系天赋技能

    # 其他
    Enrage = CAN.SHIFT_G  # 激怒, 类似于战士的血性狂暴
    Survival_Instincts = CAN.SHIFT_F2  # 生存本能, 提高生命上限, 类似于战士的破釜沉舟
    Frenzied_Regeneration = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 狂暴回复, 怒气转血量

    # 猫形态
    Cat_FormShapeshift = CAN.SHIFT_W  # 猫形态
    Prowl = CAN.ALT_F1  # 潜行

    Enter_Prowl_Macro = CAN.ALT_F1  # 进入潜行状态宏
    """
    #showtooltips
    /cast [stance:0/1/2/4/5] 猎豹形态
    /cast [stance:3] !潜行
    """

    # 起手技
    Pounce = None  # 突袭, 使目标昏迷, 类似与盗贼的偷袭
    Ravage = None  # 毁灭, 类似于盗贼的伏击

    # 攒星技
    Rake = CAN.KEY_1  # 斜掠, 使目标流血
    Claw = CAN.KEY_2  # 爪击, 类似于盗贼的邪恶打击
    Shred = CAN.KEY_3  # 撕碎, 类似于盗贼的背刺
    Mangle_Cat = CAN.KEY_3  # 裂伤, 猫形态, 类似于盗贼的出血, 野性系天赋技能

    # 终结技
    Ferocious_Bite = None  # 凶猛撕咬, 类似于盗贼的剔骨
    Rip = None  # 割裂, 造成持续伤害, 类似于盗贼的割裂
    Maim = None  # 割碎, 使目标昏迷, 类似于盗贼的肾击
    Savage_Roar = None  # 野蛮咆哮, 短时间内提高物理伤害

    Berserk = None  # 狂暴, 熊猫通用爆发技能, 野性系天赋技能

    # 其他
    Feral_Charge_Cat = None  # 野性冲锋 猫形态, 野性系天赋技能
    Dash = CAN.SHIFT_R  # 冲刺, 类似于盗贼的疾跑
    Cower = None  # 畏缩, 降低仇恨
    Swipe_Cat = None  # 扫击 猫形态

    Faerie_Fire_Feral = None  # 精灵之火 野性
    Tiger_s_Fury = None  # 猛虎之怒, 提高物理伤害

    Track_Humanoids = None  # 追踪人形生物

    Aquatic_FormShapeshift = None  # 水栖形态
    Travel_FormShapeshift = None  # 旅行形态
    Flight_FormShapeshift = CAN.NUMPAD_11_DIVIDE  # 飞行形态


class Healbot:
    HB_Rejuvenation = CAN.MOUSE_LButton  # 回春术
    HB_Wild_Growth = CAN.SHIFT_LEFT_CLICK  # 野性生长, 群体治疗, 恢复系天赋技能
    HB_Remove_Curse = CAN.CTRL_LEFT_CLICK  # 驱散诅咒
    HB_Regrowth = CAN.ALT_LEFT_CLICK  # 愈合

    HB_Innervate = CAN.MOUSE_MButton  # 激活, 为目标回复大量法力
    HB_Lifebloom = None  # 生命之花, hot, 周期结束后会返回部分蓝耗

    HB_Nourish = CAN.MOUSE_RButton  # 滋养
    HB_Healing_Touch = CAN.SHIFT_RIGHT_CLICK  # 治疗之触
    HB_Abolish_Poison = CAN.CTRL_RIGHT_CLICK  # 驱毒术
    HB_Swiftmend = CAN.ALT_RIGHT_CLICK  # 迅捷治愈, 恢复系天赋技能


class Druid(Balance, Restoration, Feral, Healbot):
    pass


class DruidBalance(Druid):
    Starfall = CAN.ALT_F  # 星落术, 强大的 AOE 技能, 平衡系天赋技能
    Typhoon = CAN.G  # 台风, 俗称推推, 造成伤害并将目标向后退
    Force_of_Nature = None  # 自然之力, 召唤树人, 平衡系天赋技能
    Moonkin_FormShapeshift = CAN.SHIFT_E  # 枭兽形态, 平衡系天赋技能


class DruidRestoration(Druid):
    """
    对于治疗
    """
    Wild_Growth = CAN.KEY_5  # 野性生长, 群体治疗, 恢复系天赋技能
    Swiftmend = None  # 迅捷治愈, 恢复系天赋技能
    Tree_of_LifeShapeshift = CAN.SHIFT_E  # 治疗之树形态
    Nature_s_Swiftness = CAN.ALT_F  # 自然迅捷, 下一个技能瞬发, 恢复系天赋技能

    MB_SLOW_HEAL = CAN.KEY_1
    """
    以 15 秒为一个循环 (因为回春术的一个周期是 15) 的治疗宏. 用于慢慢治疗单目标 (主要是坦克).
    
    宏命令的例子如下::
    
        #showtooltip
        /castsequence [nochanneling] reset=target 回春术,愈合,生命绽放,生命绽放,生命绽放,,,,
    """
    MB_HEAL_RAID = CAN.KEY_2
    """
    随机选择团队成员丢回春和野性成长 (AOE 治疗 HOT).
    
    宏命令的例子如下::
    
        /cast [stance:0/1/2/3/4] 生命之树
        /castsequence reset=15 回春术,回春术,回春术,回春术,回春术,野性成长
    """
    MB_FAST_HEAL = CAN.KEY_3
    """
    单体快速治疗. 一般放一个 "滋养" 技能就可以了, 不需要宏
    """
    MB_AOE_HEAL = CAN.KEY_5
    """
    群体治疗, 一般放一个 "野性成长" 技能就可以了.
    """


class DruidFeral(Druid):
    Feral_Charge_Bear = None  # 野性冲锋 熊形态, 野性系天赋技能
    Feral_Charge_Cat = None  # 野性冲锋 猫形态, 野性系天赋技能
    Berserk = None  # 狂暴, 熊猫通用爆发技能, 野性系天赋技能
# fmt: on
