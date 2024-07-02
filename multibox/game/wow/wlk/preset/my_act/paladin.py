# -*- coding: utf-8 -*-

"""
说明
------------------------------------------------------------------------------
This is a sample script to configure your spell key binding for multiboxing.

You should copy and paste this script as your foundation and fill in your own
spell key binding.

该文件是一个用来定义你游戏中的技能键位绑定的配置文件模版. 请不要直接在本文件上修改. 而是将其拷贝一份到 app 文件夹下进行修改. 该文件是基于圣骑士的, 其他职业也是同理.

这个文件有这么几个类:

- class $Talent1: 属于该系的职业技能, 这些技能的键位设定应该是无论你当前使用的什么天赋, 都应该是用这个键位. 我们以 ``class Retribution`` 距离. 例如 惩戒天赋中如果有 神圣风暴 技能. 该技只会在 惩戒天赋下 才会用到. 所以你在这个类中请让他保持 None, 而是转而到 ``class PaladinRetribution`` 中定义它的快捷键
- class $Talent2: 同上
- class $Talent3: 同上
- class Healbot: 使用 Healbot 团队框架施放的技能, 这些技能的键位设定应该是无论你当前使用的什么天赋, 都应该是用这个键位.
- class $ClassName: 汇总所有无论你当前使用的什么天赋都适用的键位. 该类继承了 $Talent1, $Talent2, $Talent3, Healbot 四个类
- class $ClassName$Talent1: 设定使用特定天赋时特定的键位, 该类继承了 $ClassName, 特定键位只要覆盖父类的属性即可
- class $ClassName$Talent2: 同上
- class $ClassName$Talent3: 同上

如何编辑该配置文件
------------------------------------------------------------------------------
"""

from hotkeynet.api import CAN

# fmt: off
class Retribution:
    # 惩戒系主打技能
    Judgement_of_Light = CAN.R  # 光明审判
    Judgement_of_Wisdom = CAN.R  # 智慧审判
    Judgement_of_Justice = CAN.R  # 公正审判
    Crusader_Strike = CAN.KEY_2  # 十字军打击
    Divine_Storm = CAN.KEY_3  # 神圣风暴

    # 光环
    Retribution_Aura = None  # 惩戒光环
    Crusader_Aura = None  # 十字军光环

    # 祝福
    Blessing_of_Might = None  # 力量祝福
    Greater_Blessing_of_Might = None  # 强效力量祝福

    Avenging_Wrath = CAN.SHIFT_F  # 复仇之怒
    Hammer_of_Wrath = CAN.SHIFT_TAB  # 愤怒之锤
    Repentance = CAN.ALT_T  # 忏悔
    Seal_of_Command = None  # 命令圣印
    Seal_of_Vengeance_Corruption = None  # 复仇/腐蚀 圣印


class Protection:
    # 防护系主打技能
    Shield_of_Righteousness = CAN.ALT_2  # 复仇之盾
    Hammer_of_the_Righteous = CAN.KEY_2  # # 公正之锤
    Avenger_s_Shield = CAN.ALT_3  # 复仇者之盾
    Holy_Shield = CAN.KEY_3  # 神圣之盾

    # 坦克技能
    Righteous_Fury = None  # 正义之怒
    Hand_of_Reckoning = CAN.Z  # 清算之手, 嘲讽
    Righteous_Defense = CAN.ALT_F  # 正义防御

    # 光环
    Devotion_Aura = CAN.SHIFT_Q  # 虔诚光环
    Fire_Resistance_Aura = None  # 火焰抗性光环
    Frost_Resistance_Aura = CAN.SHIFT_E  # 冰霜抗性光环
    Shadow_Resistance_Aura = None  # 暗影抗光环

    # 祝福
    Blessing_of_Kings = None  # 王者祝福
    Greater_Blessing_of_Kings = None  # 王者祝福
    Blessing_of_Sanctuary = None  # 庇护祝福
    Greater_Blessing_of_Sanctuary = None  # 强效庇护祝福

    Divine_Intervention = CAN.ALT_F2  # 神圣干涉
    Divine_Protection = CAN.SHIFT_F2  # 圣佑术, 减伤
    Divine_Sacrifice = CAN.SHIFT_C  # 神圣牺牲, 团队减伤
    Divine_Shield = CAN.SHIFT_F1  # 圣盾术, 无敌

    Hammer_of_Justice = CAN.CTRL_E  # 制裁之锤, 控制技

    # 特殊效果的祝福
    Hand_of_Freedom = CAN.SHIFT_R  # 自由祝福
    Hand_of_Protection = CAN.SHIFT_G  # 保护祝福
    Hand_of_Sacrifice = CAN.ALT_R  # 牺牲祝福
    Hand_of_Salvation = CAN.CTRL_R  # 拯救祝福
    Seal_of_Justice = None  # 公正圣印 (有几率打晕敌人)


class Holy:
    # 神圣系主打技能
    Beacon_of_Light = CAN.ALT_G  # 圣光道标
    Holy_Light = CAN.ALT_X  # 圣光术
    Flash_of_Light = CAN.X  # 圣光闪现
    Holy_Shock = CAN.Z  # 神圣冲击
    Aura_Mastery = CAN.ALT_Z  # 光环掌握

    # 光环
    Concentration_Aura = CAN.SHIFT_W  # 专注光环

    # 祝福
    Blessing_of_Wisdom = None  # 智慧祝福
    Greater_Blessing_of_Wisdom = None  # 超级智慧祝福

    Cleanse = CAN.T  # 净化术, 驱散 魔法, 中毒, 疾病
    Consecration = CAN.KEY_4  # 奉献
    Divine_Favor = CAN.ALT_F  # 神恩术, 下一个法术必暴
    Divine_Illumination = CAN.ALT_T  # 神启术, 耗蓝降低 50%
    Divine_Plea = CAN.ALT_E  # 神圣恳求
    Exorcism = CAN.X  # 驱邪术
    Holy_Wrath = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 神圣愤怒, 对亡灵怪群晕
    Lay_on_Hands = CAN.ALT_F1  # 圣疗术
    Purify = None  # 纯净术, 低等级技能, 会被 净化术 所取代
    Redemption = None  # 复活
    Sacred_Shield = CAN.CTRL_X  # 圣洁护盾
    Seal_of_Light = None  # 光明圣印
    Seal_of_Righteousness = None  # 公正圣印
    Seal_of_Wisdom = None  # 智慧圣印
    Sense_Undead = None  # 感知亡灵
    Turn_Evil = CAN.CTRL_F  # 转化亡灵, 恐惧亡灵怪


class Healbot:
    HB_Holy_Light = CAN.MOUSE_LButton
    HB_Sacred_Shield = CAN.ALT_LEFT_CLICK
    HB_Cleanse = CAN.CTRL_LEFT_CLICK
    HB_Beacon_of_Light = CAN.SHIFT_LEFT_CLICK

    HB_Flash_of_Light = CAN.MOUSE_RButton
    HB_Holy_Shock = CAN.SHIFT_RIGHT_CLICK
    HB_Hand_of_Freedom = CAN.ALT_RIGHT_CLICK

    HB_Hand_of_Protection = CAN.ALT_MIDDLE_CLICK
    HB_Hand_of_Salvation = CAN.CTRL_MIDDLE_CLICK
    HB_Hand_of_Sacrifice = CAN.SHIFT_MIDDLE_CLICK

    HB_Righteous_Defense = None
    HB_Divine_Intervention = None
    HB_Lay_on_Hands = None


class Paladin(Retribution, Protection, Holy, Healbot):
    pass


class PaladinProtection(Paladin):
    Hand_of_Reckoning = CAN.Z
    Hammer_of_the_Righteous = CAN.KEY_2
    Shield_of_Righteousness = CAN.ALT_2

    Holy_Shield = CAN.KEY_3
    Avenger_s_Shield = CAN.ALT_3
    Consecration = CAN.KEY_4
    Righteous_Defense = CAN.ALT_F


class PaladinRetribution(Paladin):
    Hand_of_Reckoning = CAN.Z
    Crusader_Strike = CAN.KEY_2
    Divine_Storm = CAN.KEY_3
    Consecration = CAN.KEY_4
    Repentance = CAN.ALT_E
    Righteous_Defense = CAN.ALT_F


class PaladinHoly(Paladin):
    """
    由于奶骑按照职业顺序 (板甲 -> 布甲, 单一职业 -> 混合职业) 是第一个治疗职业, 而 Healbot
    的快捷键我们是按照一定的逻辑来的. 这里我们就来解说一下这个逻辑.

    - 左键 / 右键 是最高频的治疗技能
    - Shift / Alt + 左键 / 右键 是次高频的治疗技能
    - Ctrl + 左键 / 右键 是驱散类技能, 其中 Ctrl + 左键为更主要的驱散技能
    - 中键 是临时性的技能, 例如骑士给保护祝福, 德鲁伊给激活等
    """
    Beacon_of_Light = CAN.KEY_0

    # --- 神圣天赋下专属键位 ---
    One_Minute_Heal_Rotation_Macro_copy_1 = CAN.KEY_1
    """
    以 1 分钟为一个循环 (根据你的急速) 的治疗宏
    以 /castsequence reset=30 为起始, 以 X 圣闪 Y 圣光 的比例组成一个 5 - 6 秒的循环, 
    在第 30 秒的时候施放 神圣恳求 回蓝. 这个 X, Y 的比例取决于你的缺不缺蓝. 你不缺蓝则圣光
    多一点, 缺蓝则圣闪多一些. 然后根据你的急速填充满 60 秒循环.
    
    宏命令的例子如下:

    /castsequence reset=30 Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Divine Plea,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,
    """
    One_Minute_Heal_Rotation_Macro_copy_2 = CAN.KEY_2  # 和上面的技能效果一样, 不过放在了另一个键位, 我们有特殊原因.

    Periodical_Beacon_of_Light_on_Focus_Macro = CAN.KEY_3
    """
    每 1.5 分钟一次的给焦点刷新圣光道标宏. 里面的 ``,`` 的数量决定了刷新道标的概率. 注意,
    这个宏里不能有 ``/stopcasting``, 不然你一按到这个键就打断当前治疗施法可不行. 也就是说
    这个宏即使我们轮到了施放圣光道标, 也不一定会成功, 我们就算这个概率是 50% 好了.
    例如有 9 个逗号, 意味着按 10 下该技能会生效一次. 如果你平均每 3 秒按一下这个键, 那么
    平均 30 秒会放一次圣光道标, 结合 50% 的概率, 平均每 60 秒刷新一次道标.

    #showtooltip
    /target focus
    /castsequence Beacon of Light,,,,,,,,,,,,,,,,,,
    """

    Periodical_Judgement_of_Light_on_Focus_Target_Macro = CAN.KEY_4
    """
    每 15 秒一次的对焦点的目标打审判宏以触发奶骑的急速 Buff. 偶尔给自己补圣洁护盾.
    这个也是一个用概率来实现周期性施法的宏. 例如我们平均 15 秒按一次这个技能, 大部分的时候
    我们是打审判, 偶尔是放圣洁护盾.

    #showtooltip
    /assist focus
    /startattack
    /castsequence Judgement of Light,Judgement of Light,Sacred Shield
    """

    Holy_Shock = CAN.Z
    Focus_Judgement = CAN.R
    """
    如果焦点是敌人, 则对焦点打审判. 如果焦点是友方, 则对焦点目标打审判.
    通常用于设置坦克或者Boss为焦点的情况下使用, 避免选择目标的麻烦.

    #showtooltip
    /cast [target=focustarget,harm][target=focus,harm][] Judgement of Light;
    """

    HB_Beacon_of_Light = CAN.MIDDLE_CLICK
    HB_Holy_Shock = CAN.SHIFT_RIGHT_CLICK
# fmt: on
