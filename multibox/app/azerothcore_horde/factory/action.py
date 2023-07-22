# -*- coding: utf-8 -*-

from hotkeynet.api import CAN, KeyMaker
from multibox.game.wow.wlk.api import Window


class Movement:
    """
    移动类的按键绑定. 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.
    """

    MOVE_LEFT = CAN.Q  # 往左平移
    MOVE_RIGHT = CAN.E  # 往右平移
    MOVE_FORWARD = CAN.UP  # 往前
    MOVE_BACKWARD = CAN.DOWN  # 往后
    MOVE_LEFT_TOP = KeyMaker(f"{MOVE_LEFT} {MOVE_FORWARD}")  # 左上
    MOVE_RIGHT_TOP = KeyMaker(f"{MOVE_RIGHT} {MOVE_FORWARD}")  # 右上
    MOVE_LEFT_BOTTOM = KeyMaker(f"{MOVE_LEFT} {MOVE_BACKWARD}")  # 左下
    MOVE_RIGHT_BOTTOM = KeyMaker(f"{MOVE_RIGHT} {MOVE_BACKWARD}")  # 右下
    TURN_LEFT = CAN.LEFT  # 向左转
    TURN_RIGHT = CAN.RIGHT  # 向右转
    JUMP = CAN.SPACE  # 跳跃
    TOGGLE_AUTO_RUN = CAN.OEM3_WAVE_OR_BACK_QUOTE  # 切换自动奔跑
    FOLLOW_TARGET = CAN.OEM5_PIPE_OR_BACK_SLASH  # 跟随目标
    FOLLOW_FOCUS = CAN.NUMPAD_12_MULTIPLY  # 跟随焦点目标
    PITCH_UP = CAN.INSERT  # 在水中/空中上浮
    PITCH_DOWN = CAN.DELETE  # 在水中/空中下沉


class PetAction:
    """
    操作宠物的按键绑定. 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.
    """

    ATTACK = CAN.CTRL_1  # 宠物攻击主人的目标
    FOLLOW = CAN.CTRL_2  # 宠物跟随主人
    STAY = CAN.CTRL_3  # 宠物停留
    AGGRESSIVE = CAN.CTRL_1  # 进攻模式
    DEFENSIVE = CAN.CTRL_2  # 防御模式
    PASSIVE = CAN.CTRL_3  # 被动模式


class Target:
    """
    选择目标相关的按键绑定. 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.

    1. 如果无需用宏, 例如选择最近的敌人可以用 Tab, 选择自己可以用 F1 这些都是游戏自带按键
        设定. 你在游戏按键设定中按照这个设置好即可.
    2. 如果需要用到宏, 例如选择某个特定的坦克, 那么你需要做宏, 并且将其放置在动作条的特定位置
        上, 然后把动作条的特定位置添加上按键绑定.
    """

    TARGET_NEAREST_ENEMY = CAN.TAB
    TARGET_NEAREST_FRIEND = CAN.CTRL_TAB
    TARGET_SELF = CAN.F1
    TARGET_PARTY_MEMBER_1 = CAN.F2
    TARGET_PARTY_MEMBER_2 = CAN.F3
    TARGET_PARTY_MEMBER_3 = CAN.F4
    TARGET_PARTY_MEMBER_4 = CAN.F5

    INTERACT_WITH_TARGET = CAN.J
    INTERACT_WITH_MOUSE_OVER = CAN.UNKNOWN
    ASSIST_TARGET = CAN.F

    SET_TARGET_AS_FOCUS = CAN.CTRL_ALT_F
    TARGET_FOCUS = CAN.COMMA
    TARGET_LAST_TARGET = CAN.PERIOD

    TARGET_PARTY = CAN.NUMPAD_1
    """
    The ``MB-TgtParty`` Macro, randomly select a party member, if in camera::

        /targetparty
    """

    TARGET_RAID = CAN.NUMPAD_2
    """
    The ``MB-TgtRaid`` Macro, randomly select a raid member, if in camera::

        /targetraid
    """

    TARGET_FOCUS_TARGET = CAN.NUMPAD_3
    """
    The ``MB-TgtFcsTgt`` Macro, when focus is tank, usually it assist the leader::

        /assist focus
    """

    TARGET_FOCUS_TARGET_TARGET = CAN.NUMPAD_4
    """
    The ``MB-TgtFcsTgtTgt`` Macro, when focus is tank, usually it select the
    boss current target player::

        /assist focus
        /assist
    """

    # --- Target specific person
    # 以下的几个设置需要配合宏命令
    # w01
    TARGET_W01_RA = CAN.SHIFT_(CAN.INSERT)

    # w10
    TARGET_W10_RJ = CAN.SHIFT_(CAN.HOME)


target_leader_key_mapper = {
    Window.make(1).label: Target.TARGET_W01_RA,
    Window.make(10).label: Target.TARGET_W10_RJ,
}


class Camera:
    """
    视角, 摄像头相关的按键绑定, 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.

    保持所有人物角色的视角统一有助于用使用需要选择施法区域的技能.
    """

    # 移动摄像机, 将其移动到第 N 套设置 ...
    # 第一个视角永远是视角拉到最近, 第一人称视角, 也就是按下 Home 键的效果.
    SET_FIRST_CAMERA_VIEW_1 = CAN.CTRL_SHIFT_ALT_(CAN.INSERT)
    # 第二个视角永远是视角拉到最远, 并且开启摄像头永远跟随的模式时系统自动的高度.
    SET_FIRST_CAMERA_VIEW_2 = CAN.CTRL_SHIFT_ALT_(CAN.HOME)
    # 第三个视角备用
    SET_FIRST_CAMERA_VIEW_3 = CAN.CTRL_SHIFT_ALT_(CAN.PAGE_UP)

    SAVE_FIRST_CAMERA_VIEW_1 = CAN.CTRL_SHIFT_ALT_(CAN.DELETE)
    SAVE_FIRST_CAMERA_VIEW_2 = CAN.CTRL_SHIFT_ALT_(CAN.END)
    SAVE_FIRST_CAMERA_VIEW_3 = CAN.CTRL_SHIFT_ALT_(CAN.PAGE_DOWN)


class System:
    """
    客户端系统相关的按键绑定, 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.
    """

    MASTER_VOLUME_DOWN = CAN.CTRL_11_MINUS  # 音量调大
    MASTER_VOLUME_UP = CAN.CTRL_12_PLUS  # 音量调小
    TOGGLE_USER_INTERFACE = CAN.CTRL_F12  # 开关用户界面


class General:
    """
    通用类功能的按键绑定. 所有职业都需要按照这个设置.  以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.
    """

    ESC = CAN.ESC  # 按 ECS 键
    TRIGGER = CAN.TRIGGER  # Hotkey 里面的 %Trigger% 语法, 把触发器作为动作按下去

    STOP_CASTING_KEY_OEM1_SEMICOLUMN = CAN.OEM1_SEMICOLUMN  # 取消施法
    STOP_ATTACKING_KEY_OEM7_QUOTE = CAN.OEM7_QUOTE  # 取消攻击
    LEAVE_PARTY_MACRO_KEY_ALT_END = CAN.ALT_(CAN.END)  # 离开队伍宏
    """
    The ``MB-LeaveParty`` Macro::

        /script LeavePart()
    """

    CONFIRM_MACRO_KEY_NUMPAD_5 = CAN.NUMPAD_5  # 按下接受按钮宏, 可以用于接收组队, 进入随机地下城
    """
    The ``MB-Confirm`` Macro::

        /click StaticPopup1Button1
    """

    SET_FOCUS_KEY_NUMPAD_6 = CAN.NUMPAD_6  # 设置当前目标为焦点宏
    """
    The ``MB-FocusSet`` Macro::

        /focus
    """

    CLEAR_FOCUS_NUMPAD_7 = CAN.NUMPAD_7  # 取消已设置的焦点
    """
    The ``MB-FocusClear`` Macro::

        /clearfocus
    """

    MOUNT_UP_MACRO_KEY_NUMPAD_11_DIVIDE = CAN.NUMPAD_11_DIVIDE
    """
    The ``MountUp`` Macro. 简单来说逻辑是如果已经在 坐骑上, 或是进入了飞行模式, 则
    stopmacro; 其他情况根据当地是否可以飞行, 使用不同的坐骑和进入德鲁伊飞行形态::

        #showtooltip
        /stopmacro [mounted]
        /stopmacro [stance:6] # 平衡恢复用 6, 野性用 5, 非德鲁伊职业不需要这行
        /cast [flyable] ${YourFlyMountSpellNameOrDruidFlightFormSkill}
        /cast [noflyable] ${YourLandMountSpellName}
    """

    MOUNT_DOWN_MACRO_CTRL_OEM3_WAVE = CAN.CTRL_OEM3_WAVE_OR_BACK_QUOTE
    """
    The ``MountDown`` Macro. 简单来说就是尝试清除掉坐骑和飞行形态的光环::

        #showtooltip
        /cancelaura ${YourLandMountSpellName}
        /cancelaura ${YourFlyMountSpellName}
        /cancelaura Swift Flight Form, 非德鲁伊职业不需要这行
    """

    LAND_MOUNT_SPELL_KEY_CTRL_Z = CAN.CTRL_Z  # 陆地坐骑, 不是宏
    """
    陆地专用坐骑.
    """

    EAT_FOOD_KEY_CTRL_T = CAN.CTRL_T  # 吃喝食物

    BUFF_SELF_MACRO_KEY_8 = CAN.KEY_8  # 给自己刷 Buff 的宏
    """
    用于给自己刷 Buff 的宏或技能, 这个因职业而异

    例如防惩骑士的是::

        #showtooltip
        /target player
        /castsequence [spec:1] reset=target Seal of Vengeance, !Retribution Aura, Greater Blessing of Kings
        /castsequence [spec:2] reset=target Righteous Fury, Seal of Vengeance, !Devotion Aura, Greater Blessing of Sanctuary
    """

    BUFF_RAID_MACRO_KEY_9 = CAN.KEY_9  # 给团队刷 Buff
    """
    用于给团队刷 Buff 的宏或技能, 这个因职业而异
    """

    RACIAL_SKILL_KEY_ALT_A = CAN.ALT_A  # 种族天赋 1
    USE_TRINKET_1_KEY_ALT_S = CAN.ALT_S  # 使用饰品 1
    USE_TRINKET_2_KEY_ALT_D = CAN.ALT_D  # 使用饰品 2

    DPS_BURST_MACRO_KEY_ALT_D = CAN.ALT_D  # DPS 爆发宏
    """
    The DPS Burst Skill macro, different class game different macro.

    caster may game something like::

        #showtooltip
        /stopcasting
        /cast ${NonGCDBurstSkillName}
        /game ${TrinketOrEngineeringEnchantingItemName}
    """

    SHOOT_WAND_OR_RANGE_WEAPON_KEY_SHIFT_TAB = CAN.SHIFT_TAB  # 使用魔杖宏
    """
    Mage / Warlock / Priest shoot wand, Warrior / Rogue shoot range weapon
    """

    TOGGLE_MAIN_GAME_MENU = CAN.CTRL_SHIFT_ALT_E  # 开关游戏选项界面, 可以用于一键登出


class Warrior:
    """
    战士职业的按键绑定.
    """

    pass


class Paladin:
    """
    圣骑士职业的按键绑定.
    """

    ALL_SPEC_DIVINE_PLEA = CAN.MIDDLE_CLICK  # 神圣恩求 (回蓝技能)
    ALL_SPEC_AVENGING_WRATH = CAN.SHIFT_F  # 复仇之怒 (爆发技能)

    # --- Defensive CD 防御性CD技能 ---
    ALL_SPEC_DIVINE_SHIELD = CAN.SHIFT_F1  # 圣盾术 (无敌)
    ALL_SPEC_DIVINE_PROTECTION = CAN.SHIFT_F2  # 圣佑术 (50% 减伤)
    ALL_SPEC_DIVINE_SACRIFICE = CAN.SHIFT_C  # 神圣牺牲 (团队减伤技能)
    ALL_SPEC_AURA_MASTERY = CAN.ALT_Z  # 光环掌握

    # --- Hand Of xxx 给他人释放的功能性的祝福 ---
    ALL_SPEC_HAND_OF_PROTECTION = CAN.SHIFT_G  # 保护祝福
    ALL_SPEC_HAND_OF_SALVATION = CAN.CTRL_R  # 拯救祝福
    ALL_SPEC_HAND_OF_SACRIFICE = CAN.ALT_R  # 牺牲祝福
    ALL_SPEC_HAND_OF_FREEDOM = CAN.SHIFT_R  # 自由祝福

    # --- CC 控制类技能 ---
    ALL_SPEC_HAMMER_OF_JUSTICE = CAN.CTRL_E  # 制裁之锤
    ALL_SPEC_HOLY_WRATH = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 神圣愤怒 (对亡灵群体昏迷) Shift + ~
    ALL_SPEC_TURN_EVIL = CAN.CTRL_F  # 恐惧亡灵

    # --- 治疗类技能 ---
    ALL_SPEC_FLASH_OF_LIGHT = CAN.X  # 圣光闪现
    ALL_SPEC_HOLY_LIGHT = CAN.ALT_X  # 圣光术
    ALL_SPEC_CLEANSE = CAN.T  # 清洁术
    ALL_SPEC_SACRED_SHIELD = CAN.CTRL_X  # 圣洁护盾

    # --- 其他 ----
    ALL_SPEC_EXORCISM = CAN.G  # 驱邪术 (读条施法攻击技能, 对亡灵必爆)

    # --- 防护天赋下专属键位 ---
    PROTECT_SPEC_KEY_1_JUDGEMENT = CAN.KEY_1  # 智慧 | 光明 | 公正 审判
    PROTECT_SPEC_KEY_ALT_1_HAND_OF_RECKONING = CAN.Z  # 嘲讽 (单体嘲讽)
    PROTECT_SPEC_KEY_2_HAMMER_OF_THE_RIGHTEOUS = (
        CAN.KEY_2
    )  # 公正之锤 (防护 51 点天赋技能, 近战群拉高仇恨)
    PROTECT_SPEC_KEY_ALT_2_SHIELD_OF_RIGHTEOUSNESS = CAN.ALT_2  # 复仇之盾, 近战单体仇恨技能
    PROTECT_SPEC_KEY_3_HOLY_SHIELD = CAN.KEY_3  # 神圣之盾 (防护 31 点天赋技能, 短CD加大量格挡)
    PROTECT_SPEC_KEY_ALT_3_AVENGER_SHIELD = (
        CAN.ALT_3
    )  # 防御者之盾 (防护 41点天赋技能, 远程群体攻击, 打断施法并减速)
    PROTECT_SPEC_KEY_4_CONSECRATION = CAN.KEY_4  # 奉献 (AOE)
    PROTECT_SPEC_KEY_2_SACRED_SHIELD = CAN.KEY_5  # 圣洁护盾
    PROTECT_SPEC_KEY_Z_HAND_OF_RECKONING = CAN.Z  # 嘲讽 (单体嘲讽)
    PROTECT_SPEC_KEY_ALT_F_RIGHTEOUS_DEFENCE = CAN.ALT_F  # 正义防护 (群体嘲讽)

    # --- 惩戒天赋下专属键位 ---
    RETRIBUTION_SPEC_KEY_1_JUDGEMENT = CAN.KEY_1  # 智慧 | 光明 | 公正 审判
    RETRIBUTION_SPEC_KEY_ALT_1_HAND_OF_RECKONING = CAN.Z  # 嘲讽 (单体嘲讽)
    RETRIBUTION_SPEC_KEY_2_CRUSADER_STRIKE = CAN.KEY_2  # 十字军打击 (惩戒 41 点天赋技能)
    RETRIBUTION_SPEC_KEY_3_DIVINE_STORM = CAN.KEY_3  # 神圣风暴 (惩戒 51 点天赋技能)
    RETRIBUTION_SPEC_KEY_4_CONSECRATION = CAN.KEY_4  # 奉献 （AOE)
    RETRIBUTION_SPEC_KEY_5_SACRED_SHIELD = CAN.KEY_5  # 圣洁护盾
    RETRIBUTION_SPEC_KEY_ALT_E_REPENTANCE = CAN.ALT_E  # 忏悔 (惩戒 31 点天赋技能)
    RETRIBUTION_SPEC_KEY_Z_HAND_OF_RECKONING = CAN.Z  # 嘲讽 (单体嘲讽)
    RETRIBUTION_SPEC_KEY_ALT_F_RIGHTEOUS_DEFENCE = CAN.ALT_F  # 正义防护 (群体嘲讽)

    # --- 神圣天赋下专属键位 ---
    HOLY_SPEC_KEY_1_ONE_MINUTE_HEAL_ROTATION_MACRO = CAN.KEY_1
    """
    以1分钟为一个循环 (根据你的急速) 的治疗宏
    以 /castsequence reset=30 为起始, 以 4 圣闪 1 圣光 或者 3闪 1 光, 或是 2 闪 2 光
    为一个 5 - 6 秒的循环, 在第30秒的时候释放 神圣恳求 回蓝, 然后根据你的急速填充满 60 秒循环
    例如:

    /castsequence reset=30 Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Divine Plea,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,Flash of Light,Flash of Light,Flash of Light,Holy Light,
    """
    HOLY_SPEC_KEY_2_ONE_MINUTE_HEAL_ROTATION_MACRO = CAN.KEY_2

    HOLY_SPEC_KEY_3_PERIODICAL_BEACON_OF_LIGHT_ON_FOCUS_MACRO = CAN.KEY_3
    """
    每 1.5 分钟一次的给焦点刷新圣光道标宏. 里面的,的数量决定了刷新道标的概率.
    例如有 9 个逗号, 意味着按 10 下该技能会生效一次. 在坦克模式平均你每 30 秒会按 10 下
    键盘 3. 那么也就是 30 秒会刷新一次道标.

    #showtooltip
    /target focus
    /castsequence Beacon of Light,,,,,,,,,,,,,,,,,,
    """

    HOLY_SPEC_KEY_4_PERIODICAL_JUDGEMENT_OF_LIGHT_ON_FOCUS_TARGET_MACRO = CAN.KEY_4
    """
    每 15 秒一次的对焦点的目标打审判宏. 偶尔给自己补圣洁护盾

    #showtooltip
    /assist focus
    /startattack
    /castsequence Judgement of Light,Judgement of Light,Sacred Shield
    """
    HOLY_SPEC_KEY_5_HOLY_LIGHT = CAN.KEY_5  # 圣光术, 只有在神圣天赋下该键位有效
    HOLY_SPEC_KEY_6_FLASH_OF_LIGHT = CAN.KEY_6  # 圣光闪现, 只有在神圣天赋下该键位有效
    HOLY_SPEC_KEY_7_HOLY_LIGHT = CAN.KEY_7  # 圣光术, 只有在神圣天赋下该键位有效
    HOLY_SPEC_KEY_Z_HOLY_SHOCK = CAN.Z  # 神圣震击 (神圣 31 点天赋技能)
    HOLY_SPEC_KEY_R_FOCUS_JUDGEMENT = CAN.R
    """
    如果焦点是敌人, 则对焦点, 如果焦点是友方, 则对焦点目标打审判.
    通常用于设置坦克或者Boss为焦点的情况下使用, 避免选择目标的麻烦.

    #showtooltip
    /cast [target=focustarget,harm][target=focus,harm][] Judgement of Light;
    """
    HOLY_SPEC_KEY_0_BEACON_OF_LIGHT = CAN.KEY_0  # 圣光道标 (神圣 51 点天赋)

    # --- Healbot 团队框架快捷键 ---
    # Left | Right | Middle Click
    HEAL_BOT_LEFT_CLICK_HOLY_LIGHT = CAN.LEFT_CLICK  # 圣光术
    HEAL_BOT_RIGHT_CLICK_FLASH_OF_LIGHT = CAN.RIGHT_CLICK  # 圣光闪现
    HEAL_BOT_MIDDLE_CLICK_BEACON_OF_LIGHT = CAN.MIDDLE_CLICK  # 圣光道标

    # Shift | Alt | Ctrl + Left Click
    HEAL_BOT_BEACON_OF_LIGHT = CAN.SHIFT_LEFT_CLICK  # 圣光道标
    HEAL_BOT_SACRED_SHIELD = CAN.ALT_LEFT_CLICK  # 圣洁护盾
    HEAL_BOT_CLEANSE = CAN.CTRL_LEFT_CLICK  # 清洁术

    # Shift | Alt | Ctrl + Right Click
    HEAL_BOT_HOLY_SHOCK = CAN.SHIFT_RIGHT_CLICK  # 神圣震击
    HEAL_BOT_HAND_OF_FREEDOM = CAN.ALT_RIGHT_CLICK  # 自由祝福
    # HEAL_BOT_UNKNOWN = CAN.CTRL_RIGHT_CLICK  #

    # Shift | Alt | Ctrl + Middle Click
    HEAL_BOT_HAND_OF_SACRIFICE = CAN.SHIFT_MIDDLE_CLICK  # 牺牲祝福
    HEAL_BOT_HAND_OF_SALVATION = CAN.ALT_MIDDLE_CLICK  # 拯救祝福
    HEAL_BOT_HAND_OF_PROTECTION = CAN.CTRL_MIDDLE_CLICK  # 保护祝福


class DK:
    """
    死亡骑士职业的按键绑定.
    """

    ALL_SPEC_BLOOD_STRIKE = CAN.KEY_1  # 鲜血打击
    ALL_SPEC_HEART_STRIKE = CAN.KEY_1  # 心脏打击 (血天赋)

    ALL_SPEC_PESTILENCE_ALT_1 = CAN.ALT_1  # 传染
    ALL_SPEC_PESTILENCE_SHIFT_OEM3 = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 传染

    ALL_SPEC_ICE_TOUCH = CAN.KEY_2  # 冰冷触摸

    ALL_SPEC_CHAIN_OF_ICE_ALT_2 = CAN.ALT_2  # 寒冰锁链 (减速)
    ALL_SPEC_CHAIN_OF_ICE_CTRL_E = CAN.CTRL_E  # 寒冰锁链 (减速)

    ALL_SPEC_UNHOLY_STRIKE = CAN.KEY_3  # 邪恶打击
    ALL_SPEC_DEATH_COIL = CAN.ALT_3  # 死亡缠绕
    ALL_SPEC_FROST_STRIKE = CAN.ALT_3  # 冰霜打击 (冰天赋技能, 可以取代 死亡缠绕)

    ALL_SPEC_DEATH_STRIKE = CAN.KEY_4  # 死亡打击 (回血技能)
    """
    #showtooltip
    #spec1=unholy dps,spec2=frost dps
    /cast [mod:alt,spec:1] Scourge Strike; [mod:alt,spec:2] Obliterate; Death Strike
    """
    ALL_SPEC_OBLITERATE = CAN.ALT_4  # 湮没
    ALL_SPEC_SCOURGE_STRIKE = CAN.ALT_4  # 天灾打击 (邪天赋技能, 可以取代 湮没)

    ALL_SPEC_BLOOD_BOIL = CAN.KEY_5  # 血液沸腾
    ALL_SPEC_BLOOD_PRESENCE = CAN.SHIFT_Q  # 鲜血领域
    ALL_SPEC_FROST_PRESENCE = CAN.SHIFT_W  # 冰霜领域
    ALL_SPEC_UNHOLY_PRESENCE = CAN.SHIFT_E  # 邪恶领域

    ALL_SPEC_DARK_COMMAND_KEY_Z = CAN.Z  # 黑暗命令 (嘲讽)
    ALL_SPEC_RUNE_TAP_KEY_T = CAN.T  # 符文分流 (血天赋, 回血技能)
    ALL_SPEC_DEATH_GRIP_KEY_G = CAN.G  # 死亡之握 (远程嘲讽 加 拉人)
    ALL_SPEC_DEATH_AND_DECAY_KEY_ALT_X = CAN.ALT_X  # 死亡凋零
    ALL_SPEC_MIND_FREEZE_KEY_R = CAN.R  # 心灵冻结 (打断施法)
    ALL_SPEC_RUNE_STRIKE_KEY_ALT_E = CAN.ALT_E  # 符文打击 (类似于战士的打击, 高仇恨技能)
    ALL_SPEC_ICE_BOUND_FORTITUDE_KEY_SHIFT_F1 = CAN.SHIFT_F1  # 冰固坚韧
    ALL_SPEC_HORN_OF_WINTER_KEY_SHIFT_TAB = CAN.SHIFT_TAB  # 凛冬号角 (力量敏捷 Buff)
    ALL_SPEC_ANTI_MAGIC_SHIELD_KEY_SHIFT_F = CAN.SHIFT_F  # 反魔法护盾
    ALL_SPEC_EMPOWERED_RUNED_WEAPON_KEY_CTRL_R = CAN.CTRL_R  # 强化符文武器

    BLOOD_SPEC_VAMPIRIC_BLOOD = CAN.SHIFT_F2  # 吸血鬼之血 (DK版 战士的 破釜沉舟 技能)
    BLOOD_SPEC_HYSTERIA = CAN.SHIFT_C  # 狂血术
    BLOOD_SPEC_MARK_OF_BLOOD = CAN.ALT_F  # 鲜血印记
    BLOOD_SPEC_DANCING_RUNE_WEAPON = CAN.CTRL_F  # 符文武器之舞

    UNHOLY_SPEC_BONE_SHIELD = CAN.SHIFT_F2  # 骨盾
    UNHOLY_SPEC_SUMMON_GARGOYLE = CAN.SHIFT_C  # 召唤石像鬼
    UNHOLY_SPEC_ANTI_MAGIC_ZONE = CAN.SHIFT_G  # 反魔法领域
    UNHOLY_SPEC_CORPSE_EXPLOSION_ALF_F = CAN.ALT_F  # 尸体爆炸
    UNHOLY_SPEC_DPS_ROTATE_MACRO = CAN.KEY_2
    """
    #showtooltip
    /castsequence reset=9 Icy Touch,Plague Strike,Pestilence,Scourge Strike,Blood Strike,Death Coil,Scourge Strike,Blood Strike,Scourge Strike,Blood Strike,Death Coil
    """
    UNHOLY_SPEC_BUFF_SELF_MACRO = CAN.KEY_8
    """
    #showtooltip
    /castsequence !Unholy Presence,Raise Dead
    """

    FROST_SPEC_UNBREAKABLE_ARMOR = CAN.SHIFT_F2  # 铜墙铁壁 (提高护甲和力量)
    FROST_SPEC_DEATH_CHILL = CAN.SHIFT_C  # 死亡之寒 (下一击必爆)
    FROST_SPEC_HUNGERING_COLD = CAN.CTRL_F  # 饥饿之寒 (群体定身)
    FROST_SPEC_HOWLING_BLAST = CAN.ALT_F  # 凛风冲击 (远程瞬发AOE, 没有数量上限)


class Hunter:
    """
    猎人职业的按键绑定.
    """

    ALL_SPEC_HUNTERS_MARK = CAN.CTRL_G  # 猎人印记

    ALL_SPEC_SERPENT_STING = CAN.KEY_1  # 毒蛇钉刺 (Dot 伤害)
    ALL_SPEC_MISDIRECTION = CAN.ALT_1  # 误导
    ALL_SPEC_MISDIRECTION_FOCUS_MACRO = CAN.ALT_Z  # 误导焦点宏
    """
    ::

        #showtooltip
        /cast [target=focus,noharm] Misdirection; [target=focustarget,noharm] Misdirection
        #/target [target=focus,noharm] focus; [] focustarget
    """
    ALL_SPEC_STEADY_SHOT = CAN.KEY_2  # 稳固射击
    ALL_SPEC_AIMED_SHOT = CAN.KEY_4  # 瞄准射击
    ALL_SPEC_MULTI_SHOT = CAN.ALT_4  # 多重射击
    ALL_SPEC_KILL_SHOT = CAN.KEY_5  # 杀戮射击
    ALL_SPEC_ARCANE_SHOT = CAN.KEY_6  # 奥术射击

    ALL_SPEC_CONCUSSIVE_SHOT = CAN.Z  # 震荡射击
    ALL_SPEC_WIND_CLIP = CAN.T  # 摔绊 (减速)
    ALL_SPEC_KILL_COMMAND_X = CAN.X  # 杀戮命令 (宠物加攻速)

    ALL_SPEC_SCORPID_STING = CAN.KEY_1  # 毒蝎钉刺 (降低命中)

    ALL_SPEC_FREEZING_TRAP = CAN.CTRL_E  # 冰冻陷阱
    ALL_SPEC_FROST_TRAP = CAN.CTRL_R  # 冰霜陷阱
    ALL_SPEC_FREEZING_ARROW = CAN.ALT_R  # 冰冻箭
    ALL_SPEC_SNAKE_TRAP = CAN.SHIFT_MIDDLE_CLICK  # 毒蛇陷阱
    ALL_SPEC_EXPLOSIVE_TRAP = CAN.CTRL_MIDDLE_CLICK  # 爆裂陷阱

    ALL_SPEC_VOLLEY_ALT_X = CAN.ALT_X  # 乱射 (AOE)

    ALL_SPEC_DETERRENCE = CAN.SHIFT_F1  # 威慑 (招架所有攻击和法术)
    ALL_SPEC_FEIGN_DEATH = CAN.ALT_E  # 假死
    ALL_SPEC_DISENGAGE = CAN.SHIFT_R  # 逃脱 (向后跳)

    ALL_SPEC_DISTRACTING_SHOT = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 扰乱射击
    ALL_SPEC_TRANQUILIZING_SHOT = CAN.SHIFT_TAB  # 凝神射击
    ALL_SPEC_VIPER_STING = CAN.CTRL_X  # 蝮蛇钉刺 (吸蓝)

    ALL_SPEC_ASPECT_OF_PACT_OR_DRAGON_HAWK = CAN.SHIFT_F  # 豹群 和 龙鹰 守护相互切换
    ALL_SPEC_ASPECT_OF_VIPER_OR_DRAGON_HAWK = CAN.SHIFT_G  # 蝮蛇 和 龙鹰 守护相互切换
    ALL_SPEC_TRUE_SHOT_AURA = CAN.KEY_9  # 强击光环

    # 射击天赋
    MARKSMAN_SPEC_DPS_ROTATE_MACRO = CAN.KEY_2  # 射击猎人 用于 dps 循环的宏
    """
    """
    MARKSMAN_SPEC_CHIMERA_SHOT = CAN.KEY_3  # 奇美拉射击
    MARKSMAN_SPEC_SILENCING_SHOT = CAN.R  # 沉默射击
    MARKSMAN_SPEC_HUNTERS_MARK = CAN.KEY_6  # 猎人印记

    # 生存天赋
    SURVIVAL_SPEC_DPS_ROTATE_MACRO = CAN.KEY_2  # 生存猎人 用于 dps 循环的宏
    """
    """
    SURVIVAL_SPEC_WYVERN_STING = CAN.KEY_1  # 翼龙钉刺 (使目标沉睡)
    SURVIVAL_SPEC_BLACK_ARROW = CAN.KEY_1  # 黑噬箭 (debuff 使你对该目标的伤害获得加成)
    SURVIVAL_SPEC_EXPLOSIVE_ARROW = CAN.KEY_1  # // 爆裂箭 (debuff 使你对该目标的每次攻击都会造成爆炸额外伤害)
    SURVIVAL_SPEC_HUNTERS_MARK = CAN.KEY_6  # 猎人印记

    # 兽王天赋
    BEAST_SPEC_DPS_ROTATE_MACRO = CAN.KEY_1  # 生存猎人 用于 dps 循环的宏
    """
    """
    BEAST_SPEC_INTIMIDATION = CAN.KEY_1  # 胁迫 (兽王天赋 宝宝昏迷目标, 并造成大量威胁值)
    BEAST_SPEC_BESTIAL_WRATH = CAN.KEY_1  # 狂野怒火 (兽王天赋 宝宝和自身免疫控制, 提高造成的伤害)
    BEAST_SPEC_HUNTER_MARK = CAN.KEY_6  # 猎人印记

    HEAL_BOT_MISDIECTION = CAN.MOUSE_RButton  # 对团队框架的目标施放误导


class Shaman:
    """
    萨满职业的按键绑定.
    """

    ALL_SPEC_CALL_OF_THE_ELEMENTS = (
        CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE
    )  # 远古呼唤, 同时召唤 4 个图腾
    ALL_SPEC_TOTEMIC_RECALL = CAN.SHIFT_TAB  # 召回图腾

    # earth totem
    ALL_SPEC_TREMOR_TOTEM = CAN.ALT_F1  # 战栗图腾 (解除恐惧)
    ALL_SPEC_EARTHBIND_TOTEM = CAN.SHIFT_F  # 地缚图腾 (类似冰霜陷阱, 减速)
    ALL_SPEC_EARTH_ELEMENTAL_TOTEM = CAN.ALT_MIDDLE_CLICK  # 大地元素图腾
    ALL_SPEC_STONECLAW_TOTEM = CAN.SHIFT_F1  # 石爪图腾 (嘲讽怪物)

    # fire totem
    ALL_SPEC_FIRE_ELEMENTAL_TOTEM = CAN.SHIFT_MIDDLE_CLICK  # 火元素图腾

    # water totem
    ALL_SPEC_CLEANSING_TOTEM = CAN.ALT_F2  # 净化图腾 (驱除疾病和毒)
    ALL_SPEC_HEALING_STREAM_TOTEM = CAN.KEY_1  # 生命之泉
    ALL_SPEC_MANA_SPRING_TOTEM = CAN.KEY_1  # 法力之泉

    # air totem
    ALL_SPEC_GROUNDINIG_TOTEM = CAN.SHIFT_G  # 根基图腾 (吸收指向性法术)

    # elemental shield
    ALL_SPEC_KEY_G_WATER_SHELD = CAN.G  # 水之盾
    ALL_SPEC_KEY_G_LIGHTNING_SHIELD = CAN.G  # 闪电盾
    ALL_SPEC_KEY_0_WATER_OR_LIGHTNING_SHIELD = CAN.KEY_0  # 水盾或电盾

    ALL_SPEC_FROST_SHOCK = CAN.Z  # 冰霜震击
    ALL_SPEC_BLOOD_THIRST_HEROISM = CAN.CTRL_F  # 嗜血, 英勇
    ALL_SPEC_FIRE_NOVA = CAN.CTRL_X  # 火焰新星

    # utility spell
    ALL_SPEC_HEX = CAN.CTRL_E  # 妖术
    ALL_SPEC_PURGE = CAN.CTRL_R  # 进攻魔法驱散
    ALL_SPEC_CURE_TOXINS = CAN.ALT_R  # 驱毒术
    ALL_SPEC_GHOST_WOLF = CAN.SHIFT_R  # 幽灵狼形态
    ALL_SPEC_WIND_SHEAR_MACRO = CAN.R  # 打断施法
    """
    This should be a macro

    #showtooltip
    /stopcasting
    /cast [target=focus,harm] Wind Shear; [target=focustarget,harm] Wind Shear; [] Wind Shear
    """
    ALL_SPEC_DISPEL = CAN.T  # 驱散

    """
    风剪术 宏, 没有焦点时对目标打断, 有焦点时焦点打  断 (如果焦点是敌人则打断敌人, 如果是友方则打断焦点的目标)::

        #showtooltip
        /stopcasting
        /cast [target=focus,harm] Wind Shear; [target=focustarget,harm] Wind Shear; [] Wind Shear
    """

    ALL_SPEC_CHAIN_HEAL = CAN.CTRL_G  # 治疗链
    ALL_SPEC_LESS_HEALING_WAVE = CAN.ALT_X  # 次级治疗波
    ALL_SPEC_HEAL_WAVE = CAN.X  # 治疗波

    RESTO_SPEC_EARTH_SHIELD = CAN.ALT_G  # 大地之盾
    RESTO_SPEC_LESS_HEALING_WAVE_KEY_6 = CAN.KEY_6  # 次级治疗波
    RESTO_SPEC_LESS_HEALING_WAVE_KEY_X = CAN.X  # 次级治疗波
    RESTO_SPEC_HEALING_WAVE_KEY_7 = CAN.KEY_7  # 治疗波
    RESTO_SPEC_HEALING_WAVE_KEY_ALT_X = CAN.ALT_X  # 治疗波
    RESTO_SPEC_RIPTIDE = CAN.ALT_F  # 激流
    RESTO_SPEC_CLEANSING_SPIRIT = CAN.T  # 灵魂净化 (驱散)

    RESTO_SPEC_TIDAL_FORCE = CAN.SHIFT_C  # 潮汐之力 (恢复系天赋 提高下三次治疗法术的暴击)
    RESTO_SPEC_MANA_TIDE_TOTEM = CAN.ALT_E  # 法力之潮图腾 (恢复系天赋 团队恢复大量法力)
    RESTO_SPEC_NATURE_SWIFTNESS = CAN.MIDDLE_CLICK  # 自然迅捷 (恢复系天赋 下一个技能瞬发)

    ELEMENTAL_SPEC_DPS_ROTATE_MACRO = CAN.KEY_2  # 元素萨满 输出循环
    """
    """
    ELEMENTAL_SPEC_ELEMENTAL_MASTERY = CAN.SHIFT_C  # 元素精通
    ELEMENTAL_SPEC_THUNDER_STORM = CAN.ALT_F  # 雷霆风暴
    ELEMENTAL_SPEC_CURE_TOXIC = CAN.T  # 净化疾病中毒

    ENHANCEMENT_SPEC_DPS_ROTATE_MACRO = CAN.KEY_2  # 增强萨满 输出循环
    ENHANCEMENT_SPEC_FERAL_SPIRIT = CAN.SHIFT_C  # 野性之魂
    ENHANCEMENT_SPEC_SHAMANISTIC_RAGE = CAN.ALT_F  # 萨满之怒
    ENHANCEMENT_SPEC_CURE_TOXIC = CAN.T  # 净化疾病中毒

    # Left | Right | Middle
    HEAL_BOT_HEALING_WAVE_LEFT_CLICK = CAN.LEFT_CLICK  # 治疗波
    HEAL_BOT_RIPTIDE_RIGHT_CLICK = CAN.RIGHT_CLICK  # 激流
    HEAL_BOT_CHAIN_HEAL_MIDDLE_CLICK = CAN.MIDDLE_CLICK  # 治疗链

    # Shift, Alt, Ctrl Left Click
    HEAL_BOT_CHAIN_HEAL_SHIFT_LEFT_CLIICK = CAN.SHIFT_LEFT_CLICK  # 治疗链
    HEAL_BOT_LESS_HEALING_WAVE_ALT_LEFT_CLICK = CAN.ALT_LEFT_CLICK  # 次级治疗波
    HEAL_BOT_CLEANSE_CTRL_LEFT_CLICK = CAN.CTRL_LEFT_CLICK  # 先祖驱散

    # Shift, Alt, Ctrl Right Click
    HEAL_BOT_EARTH_SHIELD_ALT_RIGHT_CLICK = CAN.ALT_RIGHT_CLICK  # 大地之盾
    HEAL_BOT_CURE_TOXINS_CTRL_RIGHT_CLICK = CAN.CTRL_RIGHT_CLICK  # 驱毒术


class Rogue:
    """
    盗贼职业的按键绑定.
    """

    pass


class Druid:
    """
    德鲁伊职业的按键绑定.
    """

    ALL_SPEC_ENTANGLING_ROOTS = CAN.CTRL_E  # 纠缠根须
    ALL_SPEC_REJUVENATION = CAN.Z  # 回春
    ALL_SPEC_REVIVE = CAN.KEY_1  # 复活
    ALL_SPEC_REBIRTH = CAN.CTRL_X  # 战斗复活
    ALL_SPEC_INNERVATE = CAN.CTRL_F  # 激活
    ALL_SPEC_TRANQUILITY = CAN.CTRL_G  # 宁静
    ALL_SPEC_FAERI_FIRE = CAN.R  # 精灵之火
    ALL_SPEC_CYCLONE = CAN.ALT_E  # 龙卷风 (强力 CC 技能, 期间目标无法被攻击)
    ALL_SPEC_HURRICANE = CAN.ALT_X  # 飓风 (主力 AOE 技能)
    ALL_SPEC_BARK_SKIN = CAN.SHIFT_F1  # 树皮术
    ALL_SPEC_ABOLISH_POISON = CAN.ALT_R  # 清毒术
    ALL_SPEC_REMOVE_CURSE = CAN.T  # 驱除诅咒
    ALL_SPEC_SOOTHE_ANIMAL = CAN.ALT_Z  # 安抚野兽龙类
    ALL_SPEC_HIBERNATE = CAN.ALT_T  # 睡眠野兽龙类

    ALL_SPEC_CAT_STEALTH_MACRO = CAN.ALT_F1  # 强制进入潜行状态

    SHAPE_SHIFT_BEAR_FORM = CAN.SHIFT_Q  # 熊形态
    SHAPE_SHIFT_CAT_FORM = CAN.SHIFT_W  # 猫形态
    SHAPE_SHIFT_TRAVEL_FORM = CAN.SHIFT_Q  # 旅行形态
    SHAPE_SHIFT_SWIM_FORM = CAN.ALT_F2  # 游泳形态
    SHAPE_SHIFT_MOONKIN_FORM = CAN.SHIFT_E  # 枭兽形态
    SHAPE_SHIFT_TREE_OF_LIFE_FORM = CAN.SHIFT_E  # 生命之树形态
    SHAPE_SHIFT_FLIGHT_FORM = CAN.NUMPAD_11_DIVIDE  # 飞行形态

    BALANCE_SPEC_MOON_FIRE_KEY_1 = CAN.KEY_1  # 月火术 (Dot)
    BALANCE_SPEC_WRATH_KEY_2 = CAN.KEY_2  # 愤怒 (施法较快的直接攻击法术)
    BALANCE_SPEC_STAR_FIRE_KEY_3 = CAN.KEY_3  # 星火术 (施法较快的直接攻击法术)
    BALANCE_SPEC_INSECT_SWARM_KEY_4 = CAN.KEY_4  # 虫群 (Dot, 天赋技能)
    BALANCE_SPEC_HURRICANE_KEY_5 = CAN.KEY_5  # 飓风 (主力 AOE 技能)
    BALANCE_SPEC_FAERI_FIRE_KEY_6 = CAN.KEY_6  # 精灵之火
    BALANCE_SPEC_STAR_FALL_ALT_F = CAN.ALT_F  # 星落 (强力 AOE 技能, 天赋技能)
    BALANCE_SPEC_TYPHOON_KEY_G = CAN.G  # 台风 (击退面前的敌人)
    BALANCE_SPEC_FORCE_OF_NATURE = CAN.MIDDLE_CLICK  # 自然之力 (召唤树人)

    BALANCE_SPEC_DPS_ROTATE_MACRO = CAN.KEY_2
    """
    一键 DPS 循环宏::

        #showtooltip
        /castsequence reset=30 [nonchannel] 愤怒, 星火术
    """

    RESTO_SPEC_HOT_HEAL_MACRO = CAN.KEY_1
    """
    给目标上 Hot 宏::

        #showtooltip
        /castsequence reset=target 回春, 愈合, 生命之花, 生命之花, 生命之花,,,,,,
    """

    RESTO_SPEC_HEAL_RAID_MACRO_KEY_2 = CAN.KEY_2
    """
    团队随机治疗宏::

        #showtooltip
        /castsequence reset=30 野性生长, 回春, 回春, 回春, 回春, 回春
    """

    RESTO_SPEC_NOURISH_KEY_3 = CAN.KEY_3  # 滋养
    RESTO_SPEC_REGROWTH_KEY3 = CAN.ALT_3  # 愈合
    RESTO_SPEC_SWIFT_MEND_KEY_4 = CAN.KEY_4  # 迅捷治愈
    RESTO_SPEC_WILD_GROWTH_KEY_5 = CAN.KEY_5  # 野性生长 (恢复系 51 天赋)
    RESTO_SPEC_REJUVENATION_KEY_6 = CAN.KEY_6  # 回春术
    RESTO_SPEC_NOURISH_KEY_7 = CAN.KEY_7  # 滋养

    RESTO_SPEC_LIFE_BLOOM = CAN.KEY_1  # 自然之花
    RESTO_SPEC_NATURE_SWIFTNESS = CAN.MIDDLE_CLICK  # 自然迅捷
    RESTO_SPEC_HEALING_TOUCH = CAN.KEY_1  # 治疗之触

    FERAL_SPEC_SURVIVAL_INSTINCT = CAN.SHIFT_F2  # 生存本能 (类似于战士的破釜沉舟)

    # Left | Shift/Ctrl/Alt+Left
    HEAL_BOT_LEFT_CLICK_REJUVENATION = CAN.LEFT_CLICK  # 回春术
    HEAL_BOT_SHIFT_LEFT_WILD_GROWTH = CAN.SHIFT_LEFT_CLICK  # 野性生长, 群体 HOT 治疗
    HEAL_BOT_CTRL_LEFT_REMOVE_CURSE = CAN.CTRL_LEFT_CLICK  # 驱散诅咒
    HEAL_BOT_ALT_LEFT_REGROWTH = CAN.ALT_LEFT_CLICK  # 愈合

    # Right | Shift/Ctrl/Alt+Right
    HEAL_BOT_RIGHT_CLICK_NOURISH = CAN.RIGHT_CLICK  # 滋养
    HEAL_BOT_SHIFT_RIGHT_HEALING_TOUCH = CAN.SHIFT_RIGHT_CLICK
    HEAL_BOT_CTRL_RIGHT_ABOLISH_POISON = CAN.CTRL_RIGHT_CLICK  # 驱毒术
    HEAL_BOT_ALT_RIGHT_SWIFT_MEND = CAN.ALT_RIGHT_CLICK  # 迅捷治愈

    HEAL_BOT_MIDDLE_CLICK_INNERVATE = CAN.MIDDLE_CLICK  # 激活


class Mage:
    """
    法师职业的按键绑定.
    """

    ALL_SPEC_ICE_BLOCK = CAN.SHIFT_F1  # 寒冰屏障 (冰箱)
    ALL_SPEC_MIRROR_IMAGE = CAN.SHIFT_F2  # 镜像术 (暂时丢失仇恨)
    ALL_SPEC_BLINK = CAN.SHIFT_R  # 闪现
    ALL_SPEC_FIRE_WARD = CAN.SHIFT_F  # 火焰护盾
    ALL_SPEC_FROST_WARD = CAN.SHIFT_G  # 并刷昂护盾
    ALL_SPEC_POLYMORPH = CAN.CTRL_E  # 变羊术
    ALL_SPEC_SPELL_STEAL = CAN.CTRL_R  # 法术偷取
    ALL_SPEC_EVOCATION = CAN.CTRL_F  # 唤醒术
    ALL_SPEC_INVISIBILITY = CAN.ALT_E  # 隐身术

    ALL_SPEC_FIRE_BLAST = CAN.KEY_3  # 火焰冲击
    ALL_SPEC_SCROTCH = CAN.ALT_3  # 灼烧
    ALL_SPEC_DAMPEN_MAGIC = CAN.KEY_3  # 魔法抑制, 跟宏绑定, 当目标是友方时使用该技能
    ALL_SPEC_AMPLIFY_MAGIC = CAN.ALT_3  # 魔法增效, 跟宏绑定, 当目标是友方时使用该技能
    ALL_SPEC_FROST_NOVA = CAN.KEY_4  # 冰霜新星
    ALL_SPEC_CONE_OF_COLD = CAN.KEY_5  # 冰锥术
    ALL_SPEC_MANA_SHIELD = CAN.ALT_5  # 法力护盾
    ALL_SPEC_ARCANE_EXPLOSION = CAN.Z  # 奥爆术
    ALL_SPEC_COUNTER_SPELL_MACRO = CAN.R  # 法术反制
    """
    This should be a macro

    #showtooltip
    /stopcasting
    /cast [target=focus,harm] Counter Spell; [target=focustarget,harm] Counter Spell; [] Counter Spell
    """
    ALL_SPEC_REMOVE_CURSE = CAN.T  # 解除诅咒
    ALL_SPEC_FLAME_STRIKE = CAN.X  # 烈焰风暴
    ALL_SPEC_BLIZZARD = CAN.ALT_X  # 暴风雪
    ALL_SPEC_ICE_LANCE = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 冰枪术
    ALL_SPEC_FROST_FIRE_BOLT = CAN.CTRL_X  # 霜火箭
    ALL_SPEC_FOCUS_MAGIC = CAN.ALT_Z  # 专注魔法
    ALL_SPEC_SLOW_FALL = CAN.ALT_F1  # 缓落术

    FIRE_SPEC_DPS_ROTATE_MACRO = CAN.KEY_2  # 火法 用于 dps 循环的宏
    FIRE_SPEC_PYROBLAST = CAN.KEY_1  # 炎爆术
    FIRE_SPEC_FIRE_BALL = CAN.KEY_2  # 火球术
    FIRE_SPEC_LIVING_BOMB = CAN.G  # 活体炸弹

    FIRE_SPEC_COMBUSTION = CAN.SHIFT_C  # 燃烧
    FIRE_SPEC_BLAST_WAVE = CAN.ALT_G  # 冲击波
    FIRE_SPEC_DRAON_BREATH = CAN.ALT_F  # 龙息

    ARCANE_SPEC_DPS_ROTATE_MACRO = CAN.KEY_2  # 奥法 用于 dps 循环的宏
    """
    ::

        #showtooltip
        /castsequence reset=15 [nochanneling] Arcane Blast, Arcane Blast, Arcane Blast, Arcane Missiles
    """
    ARCANE_SPEC_ARCANE_MISSLE_KEY_1 = CAN.KEY_1  # 奥术飞弹
    ARCANE_SPEC_ARCANE_BLAST_KEY_2 = CAN.KEY_2  # 奥术冲击
    ARCANE_SPEC_SLOW_KEY_6 = CAN.KEY_6  # 减速术 (奥系天赋 减少 移动, 施法, 远程攻击速度)
    ARCANE_SPEC_ARCANE_BARRAGE = CAN.ALT_F  # 奥术弹幕
    ARCANE_SPEC_ARCANE_POWER = CAN.ALT_G  # 奥术强化
    ARCANE_SPEC_ICY_VEINS = CAN.SHIFT_C  # 冰冷血脉 (冰系天赋 短时间内提高施法速度, 施法无法不受伤害影响)
    ARCANE_SPEC_SLOW = CAN.G  # 减速术 (奥系天赋 减少 移动, 施法, 远程攻击速度)
    ARCANE_SPEC_PRESENCE_OF_MIND = CAN.MIDDLE_CLICK  # 气定神闲 (奥系天赋, 法术瞬发)

    FROST_SPEC_DPS_ROTATE_MACRO = CAN.KEY_1  # 冰法 用于 dps 循环的宏
    """
    ::

        #showtooltip
        /castsequence reset=15 [nochanneling] Frostbolt,Frostbolt,Frostbolt,Frostbolt,Frostbolt,Frostfire Bolt
    """
    FROST_SPEC_ICE_BARRIER = CAN.ALT_G  # 寒冰护盾 (冰天赋 吸收伤害盾)
    FROST_SPEC_ICY_VEIN = CAN.SHIFT_C  # 冰冷血脉 (冰系天赋 短时间内提高施法速度, 施法无法不受伤害影响)
    FROST_SPEC_DEEP_FREEZE = CAN.ALT_F  # 深度冻结
    FROST_SPEC_ELEMENTAL_WATER = CAN.G  # 召唤水元素
    FROST_SPEC_ELEMENTAL_WATER_NOVA = CAN.G  # 水元素霜冻新星

    HEAL_BOT_TARGET_RAID_FRAME = CAN.LEFT_CLICK  # 选择目标
    HEAL_BOT_FOCUS_MAGIC = CAN.RIGHT_CLICK  # 专注魔法
    HEAL_BOT_REMOVE_CURSE = CAN.MIDDLE_CLICK  # 驱散诅咒
    HEAL_BOT_REMOVE_CURSE_CTRL_LEFT = CAN.CTRL_LEFT_CLICK  # 驱散诅咒


class Warlock:
    """
    术士职业的按键绑定.
    """

    # curse
    ALL_SPEC_CURSE_OF_AGONY = CAN.KEY_1  # 痛苦诅咒
    ALL_SPEC_CURSE_OF_DOOM = CAN.ALT_E  # 厄运诅咒
    ALL_SPEC_CURSE_OF_ELEMENT = CAN.T  # 元素诅咒
    ALL_SPEC_TONGUES = CAN.G  # 语言诅咒

    ALL_SPEC_CURSE_OF_WEEKNESS = CAN.ALT_T  # 虚弱诅咒
    ALL_SPEC_CURSE_OF_EXHAUSION = CAN.ALT_G  # 疲劳诅咒

    ALL_SPEC_USE_HEALTH_STONE = CAN.SHIFT_F1  # 使用生命石
    ALL_SPEC_SHADOW_WARD = CAN.SHIFT_F2  # 灵魂碎裂 (减仇恨)

    ALL_SPEC_DRAIN_LIFE = CAN.SHIFT_F  # 生命吸取
    ALL_SPEC_DRAIN_MANA = CAN.SHIFT_G  # 法力吸取

    ALL_SPEC_FEAR = CAN.CTRL_E  # 恐惧
    ALL_SPEC_DRAIN_SOUL = CAN.CTRL_R  # 吸取灵魂
    ALL_SPEC_DEATH_COIL = CAN.CTRL_F  # 死亡缠绕
    ALL_SPEC_HOWL_OF_TERROR = CAN.ALT_F1  # 恐怖嚎叫

    ALL_SPEC_LIFE_TAP = CAN.Z  # 生命分流 (血转蓝)
    ALL_SPEC_SHADOW_FLAME = CAN.X  # 暗影烈焰
    ALL_SPEC_RAIN_OF_FIRE = CAN.ALT_X  # 火焰之雨
    ALL_SPEC_HELL_FIRE = CAN.CTRL_G  # 地狱烈焰

    ALL_SPEC_BANISH = CAN.CTRL_X  # 放逐
    ALL_SPEC_FEL_ARMOR = CAN.KEY_0  # 邪甲术

    ALL_SPEC_DEMONIC_CIRCLE_SUMMON = CAN.ALT_R  # 恶魔法阵: 召唤
    ALL_SPEC_DEMONIC_CIRCLE_TELEPORT = CAN.SHIFT_R  # 恶魔法阵: 传送
    ALL_SPEC_SOUL_SHATTLE = CAN.ALT_Z  # 灵魂碎裂 (减仇恨)

    ALL_SPEC_CORRUPTION = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 腐蚀术
    ALL_SPEC_SEED_OF_CORRUPTION = CAN.R  # 腐蚀之种

    DEMON_SPEC_DPS_ROTATE = CAN.KEY_2  # 恶魔术 用于 dps 循环的宏
    """
    ::

        #showtooltip
    """
    DEMON_SPEC_METAMORPHOSIS = CAN.ALT_D  # 恶魔变身 (恶魔系 51点天赋)
    DEMON_SPEC_DEMONIC_EMPOWERMENT = CAN.ALT_F  # 恶魔增效
    DEMON_SPEC_FEL_DOMINATION = CAN.SHIFT_C  # 恶魔支配 (瞬发召唤恶魔)

    AFFLICTION_SPEC_DPS_ROTATE = CAN.KEY_2  # 痛苦术 用于 dps 循环的宏
    """
    ::

        #showtooltip
    """
    AFFLICTION_SPEC_UNSTABLE_AFFLICTION = CAN.KEY_1  # 不稳定的痛苦
    AFFLICTION_SPEC_HAUNT = CAN.KEY_1  # 鬼影重重

    DESTRUCTION_SPEC_DPS_ROTATE = CAN.KEY_2  # 毁灭术 用于 dps 循环的宏
    """
    ::

        #showtooltip
    """
    DESTRUCTION_SPEC_SHADOW_FURY = CAN.ALT_F  # 暗影之怒
    DESTRUCTION_SPEC_SHADOW_BURN = CAN.SHIFT_C  # 暗影灼烧

    DESTRUCTION_SPEC_CONFLAGRATE = CAN.KEY_1  # 点燃
    DESTRUCTION_SPEC_CHAOS_BOLT = CAN.KEY_1  # 混乱箭

    HEAL_BOT_TARGET_RAID_FRAME = CAN.LEFT_CLICK  # 选择团队框架成员


class Priest:
    """
    牧师职业的按键绑定.
    """

    ALL_SPEC_FADE = CAN.SHIFT_R  # 渐隐术
    ALL_SPEC_FEAR_WARD = CAN.SHIFT_F  # 反恐惧结界
    ALL_SPEC_MANA_BURN = CAN.SHIFT_G  # 法力燃烧
    ALL_SPEC_SHACKLE_UNDEAD = CAN.CTRL_E  # 束缚亡灵
    ALL_SPEC_MIND_CONTROL = CAN.CTRL_F  # 精神控制

    ALL_SPEC_POWER_WORLD_SHIELD = CAN.SHIFT_OEM3_WAVE_OR_BACK_QUOTE  # 真言术盾

    ALL_SPEC_MASS_DISPEL = CAN.CTRL_R  # 群体驱散
    ALL_SPEC_ABOLISH_DISEASE = CAN.ALT_R  # 驱除疾病
    ALL_SPEC_DISPEL_MAGIC = CAN.T  # 驱散魔法

    ALL_SPEC_PRAYER_OF_HEALING = CAN.ALT_G  # 治疗祷言
    ALL_SPEC_HOLY_NOVA = CAN.G  # 神圣新星

    ALL_SPEC_HYMN_OF_HOPE = CAN.CTRL_G  # 希望赞歌
    ALL_SPEC_DIVINE_HYMN = CAN.CTRL_X  # 神圣赞美诗
    ALL_SPEC_SHADOW_FIEND = CAN.ALT_T  # 召唤暗影魔

    ALL_SPEC_INNER_FIRE = CAN.Z  # 心灵之火
    ALL_SPEC_FLASH_HEAL = CAN.X  # 快速治疗
    ALL_SPEC_PHYCHIC_SCREAM = CAN.MIDDLE_CLICK  # 心灵尖啸 (群体恐惧)

    # 暗影天赋下
    SHADOW_SPEC_DPS_ROTATE_SPEC = CAN.KEY_2  # 暗牧 一键输出循环宏
    SHADOW_SPEC_DISPERSION = CAN.ALT_F  # 影散 (暗影系 51点天赋, 大量减伤, 回蓝)
    SHADOW_SPEC_SILENCE = CAN.SHIFT_C  # 沉默
    SHADOW_SPEC_PSYCHIC_HORROR = CAN.ALT_E  # 心灵恐惧
    SHADOW_SPEC_SHADOW_FORM = CAN.KEY_1  # 暗影形态

    SHADOW_SPEC_SHADOW_WORD_PAIN = CAN.KEY_6  # 暗言术: 痛
    SHADOW_SPEC_DEVOURING_PLAGUE = CAN.KEY_1  # 噬灵瘟疫
    SHADOW_SPEC_VAMPIRIC_TOUCH = CAN.KEY_1  # 吸血鬼之触
    SHADOW_SPEC_VAMPIRIC_EMBRACE = CAN.KEY_1  # 吸血鬼之吻

    DISC_SPEC_DESPERATE_PRAYER = CAN.ALT_F1  # 绝望祷言
    DISC_SPEC_POWER_INFUSION = CAN.ALT_F2  # 灌注魔法
    DISC_SPEC_INNER_FOCUS = CAN.SHIFT_C  # 心灵专注
    DISC_SPEC_PAIN_SUPPRESSION = CAN.ALT_F  # 痛苦压制

    DISC_SPEC_PENANCE_KEY_1 = CAN.KEY_1  # 苦修 (戒律系 51点天赋, 大量治疗或伤害)
    DISC_SPEC_HEAL_RAID_MACRO_KEY_2 = CAN.KEY_2
    """
    全团套盾宏::

        #showtooltip
        # 1是戒律,2是神圣
        /targetraid
        /castsequence [spec:1] 真言术盾
        /castsequence [spec:2] reset=6, 治疗之环,真言术盾,真言术盾,真言术盾,真言术盾
    """

    HOLY_SPEC_GUARDIAN_SPIRIT_ALT_F = CAN.ALT_F  # 守护天使
    HOLY_SPEC_RENEW = CAN.KEY_1  # 恢复
    HOLY_SPEC_FLASH_HEAL = CAN.KEY_1  # 快速治疗
    HOLY_SPEC_GREATER_HEAL = CAN.KEY_1  # 强效治疗术
    HOLY_SPEC_PRAYER_OF_MENDING_KEY_1 = CAN.KEY_1  # 愈合祷言 (受攻击后回血, 在团队中跳跃)
    HOLY_SPEC_BINDING_HEAL = CAN.KEY_1  # 联结治疗 (治疗目标和你自己)
    HOLY_SPEC_LIGHT_WELL = CAN.KEY_1  # 治疗之泉
    HOLY_SPEC_CIRCLE_OF_HEALING = CAN.R  # 治疗之环
    HOLY_SPEC_HEAL_RAID_MACRO_KEY_2 = CAN.KEY_2
    HOLY_SPEC_DESPERATE_PRAYER_ALT_F1 = CAN.ALT_F1  # 绝望祷言
    """
    全团治疗宏::

        #showtooltip
        # 1是戒律,2是神圣
        /targetraid
        /castsequence [spec:1] 真言术盾
        /castsequence [spec:2] reset=6, 治疗之环,真言术盾,真言术盾,真言术盾,真言术盾
    """

    # ALL Spec
    HEAL_BOT_ALL_SPEC_TARGET_RAID_FRAME = CAN.LEFT_CLICK  # 选择团队框架成员
    HEAL_BOT_ALL_SPEC_ABOLISH_DISEASE = CAN.CTRL_LEFT_CLICK  # 驱除疾病

    HEAL_BOT_ALL_SPEC_POWER_WORD_SHIELD = CAN.RIGHT_CLICK  # 真言术盾
    HEAL_BOT_ALL_SPEC_DISPEL_MAGIC = CAN.CTRL_RIGHT_CLICK  # 驱散魔法

    HEAL_BOT_ALL_SPEC_FEAR_WARD = CAN.CTRL_MIDDLE_CLICK  # 反恐结界

    # --- 戒律
    # Left | Shift/Ctrl/Alt+Left
    HEAL_BOT_DISCO_AND_HOLY_SPEC_FLASH_HEAL = CAN.SHIFT_LEFT_CLICK  # 快速治疗
    HEAL_BOT_DISCO_AND_HOLY_SPEC_PRAYER_OF_MENDING = CAN.ALT_LEFT_CLICK  # 愈合祷言

    # Right | Shift/Ctrl/Alt+Right
    HEAL_BOT_RENEW = CAN.SHIFT_RIGHT_CLICK  # 恢复

    HEAL_BOT_DISCO_SPEC_PENANCE = CAN.ALT_RIGHT_CLICK  # 苦修 (戒律系 51点天赋, 大量治疗或伤害)
    HEAL_BOT_HOLY_SPEC_CIRCLE_OF_HEAL = CAN.ALT_RIGHT_CLICK  # 治疗之环 (神圣系 41 点天赋, AOE 治疗)
