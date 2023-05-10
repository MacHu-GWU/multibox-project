# -*- coding: utf-8 -*-

from hotkeynet.api import CAN


class Discipline:
    # 戒律系主打技能
    Penance = CAN.R  # 苦修, 通道型治疗技能, 戒律系天赋技能
    Power_Word_Shield = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 真言术盾
    Dispel_Magic = CAN.T  # 驱散魔法
    Mass_Dispel = CAN.CTRL_R  # 群体驱散

    Inner_Focus = CAN.SHIFT_C  # 心灵专注, 使你的下一个法术必暴击, 戒律系天赋技能
    Power_Infusion = CAN.SHIFT_F2  # 能量灌注, 使目标的施法速度提高, 戒律系天赋技能
    Pain_Suppression = CAN.ALT_F  # 痛苦压制, 减伤技能, 戒律系天赋技能

    Power_Word_Fortitude = None  # 真言术韧
    Prayer_of_Fortitude = None  # 真言术韧祷言
    Divine_Spirit = None  # 神圣精神
    Prayer_of_Spirit = None  # 神圣精神祷言

    Mana_Burn = CAN.SHIFT_G  # 法力燃烧
    Inner_Fire = CAN.Z  # 心灵之火
    Levitate = None  # 漂浮术
    Fear_Ward = CAN.SHIFT_F  # 防护恐惧结界

    Shackle_Undead = CAN.CTRL_E  # 束缚亡灵, 控制技能


class Holy:
    # 神圣系主打技能
    Renew = None  # 恢复
    Binding_Heal = CAN.KEY_6  # 联结治疗, 治疗目标与你自己
    Flash_Heal = CAN.X  # 快速治疗
    Greater_Heal = CAN.ALT_X  # 超级治疗术
    Holy_Nova = CAN.G  # 神圣新星
    Circle_of_Healing = CAN.R  # 治疗之环, 群体治疗技能, 神圣系天赋技能
    Prayer_of_Healing = CAN.ALT_G  # 治疗祷言, 群体治疗
    Desperate_Prayer = CAN.ALT_F1  # 绝望祷言, 神圣系天赋技能
    Lightwell = None  # 光明之井, 神圣系天赋技能
    Guardian_Spirit = CAN.ALT_F  # 守护天使, 保护目标不被一击必杀一次, 神圣系天赋技能

    Smite = None  # 惩击
    Holy_Fire = None  # 神圣之火, 神圣系天赋技能

    Abolish_Disease = CAN.ALT_R  # 驱除疾病

    Divine_Hymn = CAN.CTRL_G  # 神圣赞美诗, 长 CD 团队回血技能
    Hymn_of_Hope = CAN.CTRL_X  # 希望颂歌, 长 CD 团队回蓝技能

    Resurrection = None  # 复活


class Shadow:
    # 暗影系主打攻击技能
    Shadow_Word_Pain = CAN.KEY_1  # 暗言术 痛
    Devouring_Plague = CAN.KEY_6  # 噬灵瘟疫
    Vampiric_Touch = CAN.KEY_4  # 吸血鬼之触
    Mind_Flay = CAN.KEY_2  # 精神鞭笞
    Mind_Blast = CAN.KEY_3  # 心灵震爆
    Mind_Sear = CAN.KEY_5  # 精神灼烧
    Psychic_Horror = None  # 心灵惊骇, 远程恐惧单体目标, 暗影系天赋技能

    Silence = CAN.R  # 沉默, 暗影系天赋技能
    Shadowform = CAN.SHIFT_Q  # 暗影形态, 暗影系天赋技能
    Vampiric_Embrace = CAN.KEY_8  # 吸血鬼的拥抱, 暗影系天赋技能
    Dispersion = CAN.ALT_F  # 影散, 回蓝和减伤技能, 暗影系天赋技能
    Shadow_Word_Death = CAN.ALT_1  # 暗言术 死
    Shadowfiend = CAN.ALT_T  # 召唤暗影恶魔

    Fade = CAN.SHIFT_R  # 渐隐术, 暂时降低仇恨

    Mind_Control = CAN.CTRL_F  # 精神控制
    Mind_Soothe = None  # 精神安抚
    Mind_Vision = None  # 精神视界
    Psychic_Scream = CAN.ALT_E  # 精神尖啸, 群体恐惧
    Shadow_Protection = None  # 暗影防护
    Prayer_of_Shadow_Protection = None  # 暗影防护祷言


class Healbot:
    HB_Power_Word_Shield = CAN.RIGHT_CLICK  # 真言术盾
    HB_Penance = CAN.ALT_RIGHT_CLICK  # 苦修, 通道型治疗技能, 戒律系天赋技能
    HB_Pain_Suppression = None  # 痛苦压制, 减伤技能, 戒律系天赋技能
    HB_Dispel_Magic = CAN.CTRL_RIGHT_CLICK  # 驱散魔法
    HB_Abolish_Disease = CAN.CTRL_LEFT_CLICK  # 驱除疾病
    HB_Renew = CAN.SHIFT_RIGHT_CLICK  # 恢复
    HB_Prayer_of_Healing = CAN.ALT_LEFT_CLICK  # 愈合祷言
    HB_Binding_Heal = None  # 联结治疗, 治疗目标与你自己
    HB_Flash_Heal = CAN.LEFT_CLICK  # 快速治疗
    HB_Greater_Heal = None  # 超级治疗术
    HB_Holy_Nova = None  # 神圣新星
    HB_Circle_of_Healing = CAN.SHIFT_LEFT_CLICK  # 治疗之环, 群体治疗技能, 神圣系天赋技能
    HB_Guardian_Spirit = None  # 守护天使, 保护目标不被一击必杀一次, 神圣系天赋技能
    HB_Fear_Ward = CAN.MIDDLE_CLICK  # 防护恐惧结界


class Priest(Discipline, Holy, Shadow, Healbot):
    pass


class PriestDiscipline(Priest):
    Inner_Focus = CAN.SHIFT_C  # 心灵专注, 使你的下一个法术必暴击, 戒律系天赋技能
    Power_Infusion = CAN.ALT_F2  # 能量灌注, 使目标的施法速度提高, 戒律系天赋技能
    Pain_Suppression = CAN.ALT_F  # 痛苦压制, 减伤技能, 戒律系天赋技能
    Penance = CAN.R  # 苦修, 通道型治疗技能, 戒律系天赋技能
    Desperate_Prayer = CAN.ALT_F1  # 绝望祷言, 神圣系天赋技能


class PriestHoly(Priest):
    Inner_Focus = CAN.SHIFT_C  # 心灵专注, 使你的下一个法术必暴击, 戒律系天赋技能
    Desperate_Prayer = CAN.ALT_F1  # 绝望祷言, 神圣系天赋技能
    Holy_Fire = None  # 神圣之火, 神圣系天赋技能
    Circle_of_Healing = CAN.R  # 治疗之环, 群体治疗技能, 神圣系天赋技能
    Lightwell = None  # 光明之井, 神圣系天赋技能
    Guardian_Spirit = CAN.ALT_F  # 守护天使, 保护目标不被一击必杀一次, 神圣系天赋技能


class PriestShadow(Priest):
    Mind_Flay = CAN.KEY_2  # 精神鞭笞
    Vampiric_Embrace = None  # 吸血鬼的拥抱, 暗影系天赋技能
    Silence = CAN.R  # 沉默, 暗影系天赋技能
    Shadowform = CAN.SHIFT_Q  # 暗影形态, 暗影系天赋技能
    Psychic_Horror = CAN.ALT_E  # 心灵惊骇, 远程恐惧单体目标, 暗影系天赋技能Silence = None  # 沉默, 暗影系天赋技能
    Vampiric_Touch = CAN.KEY_5  # 吸血鬼之触
    Dispersion = CAN.ALT_F  # 影散, 回蓝和减伤技能, 暗影系天赋技能
