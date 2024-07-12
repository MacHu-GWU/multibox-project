# -*- coding: utf-8 -*-

"""
跟职业无关的常用快捷键绑定.
"""

from hotkeynet.api import KN, CAN, KeyMaker


# fmt: off
class Movement:
    """
    移动类的按键绑定. 所有职业都需要按照这个设置. 以下设置如果没有特殊说明, 都是
    在游戏内的按键绑定实现的.
    """

    MOVE_LEFT = CAN.Q  # 往左平移
    MOVE_RIGHT = CAN.E  # 往右平移
    MOVE_FORWARD = CAN.UP  # 往前
    MOVE_BACKWARD = CAN.DOWN  # 往后
    MOVE_LEFT_TOP = KeyMaker(f"{MOVE_LEFT.key} {MOVE_FORWARD.key}")  # 左上
    MOVE_RIGHT_TOP = KeyMaker(f"{MOVE_RIGHT.key} {MOVE_FORWARD.key}")  # 右上
    MOVE_LEFT_BOTTOM = KeyMaker(f"{MOVE_LEFT.key} {MOVE_BACKWARD.key}")  # 左下
    MOVE_RIGHT_BOTTOM = KeyMaker(f"{MOVE_RIGHT.key} {MOVE_BACKWARD.key}")  # 右下
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
    The ``MB-TgtFcsTgt`` Macro, when focus is tank, usually it assist the leader.
    在多开时, 虽然完全可以让 HotkeyNet 先点击 "选择焦点", 然后点击 "协助目标" 快捷键, 但是由于
    游戏内的宏命令的性能要远远高于用 HotkeyNet 模拟出的键盘点击事件, 而且由于选择焦点目标的
    操作在多开中是最高频的操作, 没有之一, 所以很有必要用一个宏来实现这个功能以提高性能.
    宏的内容如下::

        /assist focus
    """

    TARGET_FOCUS_TARGET_TARGET = CAN.NUMPAD_4
    """
    The ``MB-TgtFcsTgtTgt`` Macro, when focus is tank, usually it select the
    boss current target player::

        /assist focus
        /assist
    """


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

    CONFIRM_MACRO_KEY_NUMPAD_5 = (
        CAN.NUMPAD_5
    )  # 按下接受按钮宏, 可以用于接收组队, 进入随机地下城
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
# fmt: on
