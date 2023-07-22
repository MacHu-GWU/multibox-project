# -*- coding: utf-8 -*-

from hotkeynet.api import CAN

class BeastMastery:
    # 兽王系主打技能
    Bestial_Wrath = None  # 狂野怒火, 让你的宠物在短时间内增加大量伤害, 兽王系天赋技能
    Intimidation = None  # 胁迫, 控制技, 兽王系天赋技能
    The_Beast_Within = None  # 人面兽心, 俗称小红人, 人和宠物都免疫控制, 兽王系天赋技能
    Kill_Command = CAN.X  # 杀戮命令
    Master_s_Call = CAN.ALT_T  # 主人的呼唤, 解除宠物身上的控制技能

    # 守护
    Aspect_of_the_Beast = None  # 野兽守护, 让自己变得无法追踪
    Aspect_of_the_Cheetah = None  # 猎豹守护, 单体加移动速度
    Aspect_of_the_Dragonhawk = None  # 龙鹰守护, 同时具有雄鹰守护和灵猴守护的效果
    Aspect_of_the_Hawk = None  # 雄鹰守护, 加远程攻击强度
    Aspect_of_the_Monkey = None  # 灵猴守护, 加 18% 躲闪
    Aspect_of_the_Pack = None  # 豹群守护, 群体加移动速度
    Aspect_of_the_Viper = None  # 蝮蛇守护, 回蓝
    Aspect_of_the_Wild = None  # 野性守护, 加自然抗性

    Aspect_of_Pact_or_dragon_hawk = CAN.SHIFT_F  # 豹群 和 龙鹰 守护相互切换
    """
    #showtooltip
    /castsequence !豹群守护, !龙鹰守护
    """
    Aspect_of_viper_or_dragon_hawk = CAN.SHIFT_G  # 蝮蛇 和 龙鹰 守护相互切换
    """
    #showtooltip
    /castsequence !蝮蛇守护, !龙鹰守护
    """

    # 宠物相关
    Beast_Lore = None  # 野兽知识
    Call_Pet = None  # 召唤宠物
    Dismiss_Pet = None  # 解散宠物
    Feed_Pet = None  # 喂食
    Mend_Pet = None  # 治疗宠物
    Revive_Pet = None  # 复活宠物
    Tame_Beast = None  # 驯服野兽
    Eyes_of_the_Beast = None  # 野兽之眼, 以你的宠物的视角操控你它

    Eagle_Eye = None  # 鹰眼术

    Scare_Beast = None  # 恐吓野兽


class Marksmanship:
    # 射击系主打技能
    Serpent_Sting = CAN.KEY_1  # 毒蛇钉刺
    Steady_Shot = CAN.KEY_2  # 稳固射击
    Chimera_Shot = CAN.KEY_3  # 奇美拉设计, 射击系天赋技能
    Aimed_Shot = CAN.KEY_4  # 瞄准射击
    Silencing_Shot = CAN.R  # 沉默射击, 射击系天赋技能
    Kill_Shot = CAN.KEY_5  # 杀戮射击, 对血量低于一定值的目标可用, 斩杀阶段技能
    Multi_Shot = CAN.ALT_4  # 多重射击
    Volley = CAN.ALT_X  # 乱射
    Trueshot_Aura = CAN.KEY_9  # 强击光环

    Hunter_s_Mark = CAN.CTRL_G  # 猎人印记
    Periodical_add_Hunter_s_Mark = CAN.KEY_6  # 猎人印记

    Viper_Sting = CAN.CTRL_X  # 蝮蛇钉刺, 吸蓝效果
    Scorpid_Sting = None  # 毒蝎钉刺, 降低命中率

    Arcane_Shot = CAN.KEY_6  # 奥术射击
    Concussive_Shot = CAN.Z  # 震荡射击
    Tranquilizing_Shot = CAN.SHIFT_TAB  # 宁神射击, 移除激怒效果

    Distracting_Shot = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 扰乱, 使目标攻击你, 猎人的嘲讽
    Flare = CAN.CTRL_G  # 照明弹, 侦测隐形

    Rapid_Fire = CAN.ALT_D  # 急速射击, 长 CD 冷却技能
    Readiness = CAN.ALT_F  # 预备, 重置你的技能 CD, 射击系天赋技能


class Survival:
    # 生存系主打技能
    Black_Arrow = None  # 黑蚀箭, 生存系天赋技能
    Wyvern_Sting = None  # 奇美拉钉刺, 使目标进入沉睡, 苏醒后造成伤害, 生存系天赋技能
    Explosive_Shot = None  # 爆炸射击, 生存系天赋技能

    # 生存类技能
    Counterattack = None  # 还击, 近战技能, 招架后使用, 造成伤害并使得目标定身, 生存系天赋技能
    Deterrence = CAN.SHIFT_F1  # 威慑, 100% 躲闪以及偏斜法术, 保命技能
    Disengage = CAN.SHIFT_R  # 逃脱, 向后跳, 位移技能
    Mongoose_Bite = None  # 近战攻击技能
    Raptor_Strike = CAN.G  # 猛禽一击, 近战攻击技能
    Feign_Death = CAN.ALT_E  # 假死

    # 陷阱
    Immolation_Trap = None  # 献祭陷阱
    Snake_Trap = None  # 毒蛇陷阱

    # 控制类技能
    Scatter_Shot = None  # 驱散射击, 控制技能, 生存系天赋技能
    Freezing_Arrow = CAN.ALT_R  # 冰冻箭, 远程版本的冰冻陷阱
    Freezing_Trap = CAN.CTRL_E  # 冰冻陷阱, 使目标无法做出任何动作, 控制技能
    Frost_Trap = CAN.CTRL_R  # 冰霜陷阱, 使进入范围内的敌人移动速度降低
    Wing_Clip = CAN.T  # 摔绊, 近战技能, 使目标减速

    # 追踪
    Track_Beasts = None  # 追踪野兽
    Track_Demons = None  # 追踪恶魔
    Track_Dragonkin = None  # 追踪龙类
    Track_Elementals = None  # 追踪元素
    Track_Giants = None  # 追踪巨人
    Track_Hidden = None  # 追踪隐形
    Track_Humanoids = None  # 追踪人形生物
    Track_Undead = None  # 追踪亡灵

    Misdirection = CAN.ALT_1  # 误导, 使你下几次攻击造成的仇恨转移到指定目标身上

    Misdirection_Focus_Macro = CAN.ALT_Z  # 焦点误导宏
    """
    焦点误导宏. 如果你的焦点是友军, 则对其施放误导. 如果你的焦点的目标是友军 (通常是你将 boss 设为
      焦点的情况), 则对焦点的目标施放误导. 如果你的目标是友军, 则对其施放误导. 并且之后可以选中你施放了误导的目标. 该功能通常不开启
    
    ::
    
        #showtooltip
        /cast [target=focus,noharm] Misdirection; [help] Misdirection
        #/target [target=focus,noharm] focus; [] focustarget
    """


class Healbot:
    HB_Misdirection = CAN.RIGHT_CLICK  # 误导, 使你下几次攻击造成的仇恨转移到指定目标身上


class Hunter(BeastMastery, Marksmanship, Survival, Healbot):
    pass


class HunterBeastMastery(Hunter):
    Bestial_Wrath = None  # 狂野怒火, 让你的宠物在短时间内增加大量伤害, 兽王系天赋技能
    Intimidation = None  # 胁迫, 控制技, 兽王系天赋技能
    The_Beast_Within = None  # 人面兽心, 俗称小红人, 人和宠物都免疫控制, 兽王系天赋技能


class HunterMarksmanship(Hunter):
    Chimera_Shot = CAN.KEY_3  # 奇美拉射击, 射击系天赋技能
    Silencing_Shot = CAN.R  # 沉默射击, 射击系天赋技能
    Trueshot_Aura = CAN.KEY_9  # 强击光环
    Readiness = CAN.ALT_F  # 预备, 重置你的技能 CD, 射击系天赋技能


class HunterSurvival(Hunter):
    Counterattack = None  # 还击, 近战技能, 招架后使用, 造成伤害并使得目标定身, 生存系天赋技能
    Black_Arrow = None  # 黑蚀箭, 生存系天赋技能
    Wyvern_Sting = None  # 奇美拉钉刺, 使目标进入沉睡, 苏醒后造成伤害, 生存系天赋技能
    Explosive_Shot = None  # 爆炸射击, 生存系天赋技能


hunter = Hunter()
hunter_beastMastery = HunterBeastMastery()
hunter_marksmanship = HunterMarksmanship()
hunter_survival = HunterSurvival()
