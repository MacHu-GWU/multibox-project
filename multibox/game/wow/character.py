# -*- coding: utf-8 -*-

import typing as T
from collections import OrderedDict

import attrs
from attrs_mate import AttrsClass

from .account import Account
from .window import Window


@attrs.define
class Character(AttrsClass):
    """
    代表着一个正在进行的游戏角色. 有着具体的天赋. 比如一个圣骑士角色有两套天赋.
    在天赋 1 下就算是一个 Character, 在天赋 2 下算是另一个 Character.

    :param account: 与该游戏角色所绑定的账号密码信息.
    :param name: 游戏角色名.
    :param window: 游戏窗口.
    :param nth_char: 在人物选择界面位于第几个人物, 从 1 开始计数.
    :param active: 设置这个人物是否是属于 HotkeyNet 的快捷键所操作的人物.
        例如你在一场游戏中定义了 5 个人物, 但是只启用了 1, 2, 3 号 3 个人物. 4, 5 号
        设置为 active = False. 在此情况下多开脚本的行为是这样的:

        1. 启动游戏时启动所有窗口
        2. 批量输入账号密码登录时, 只登录 3 个人物
        3. 按 1234 操作的时候只操作 3 个人物
        4. 使用单个窗口登录时, 可以选择全部的 5 个人物进行登录
        5. 可以用切换单个窗口快捷键切换到 5 个人物之一的窗口
        6. 用 Round robin 切换窗口时, 只在 3 个人物之间切换

        这样适合于专注于玩几个人物, 但保留快速登录其他人物的能力. 比如登录小号聊天, 倒东西等.
        如果你将一个角色设置为 inactive, 那么这个角色只能被登录, 但无法用 Hotkeynet 操作打怪.
    :param is_leader_1: 该角色是否为 1 号司机
    :param is_leader_2: 该角色是否为 2 号司机
    :param leader_1_window: 该角色的 1 号司机的游戏窗口
    :param leader_2_window: 该角色的 2 号司机的游戏窗口

    这里没有包含任何与职业, 天赋有关的设定. 因为该模块是所有 WoW 版本通用的. 跟职业, 天赋
    有关的设定在具体版本的子模块中被定义.

    **设计思路**

    一次游戏中我们会需要知道哪些角色是坦克, 哪些角色是治疗. 或者说那个角色是扮演主坦,
    哪个角色是副坦. 我们有两种方法可以定义这件事. 一种是在顶层的 Setup 中设计一个属性:
    tank1, 其值是一个 Character 对象. 还有一种方式是在 Character 对象中设计一个属性,
    is_tank1, 其值是一个 boolean 对象.

    个人认为第二种方式更好. 因为玩魔兽玩的就是角色, 从角色的视角出发更符合人类直觉. 而且
    扁平化的枚举所有用到的人物, 以及它们扮演的不同角色, 这样的代码更容易读和编辑.

    **注意事项**

    leader_1_window 和 leader_2_window 是要跟 HotkeyNet 脚本, 以及宏命令配合使用的.
    通常 leader 就是其他队员的焦点目标, 游戏中肯定是要有一个宏命令来先选中这个焦点目标,
    然后才能将其设置为焦点的. 由于宏命令和动作条, 我们不可能创建无数个宏命令. 所以我们会在
    act 中定义我们设定好的, 有限的几个宏命令. 你设定的 leader 的窗口必须要属于那几个宏命令
    之一才能工作.
    """

    account: Account = AttrsClass.ib_generic(Account, nullable=True, default=None)
    name: str = AttrsClass.ib_str(nullable=True, default=None)
    window: Window = AttrsClass.ib_generic(Window, nullable=True, default=None)
    nth_char: int = AttrsClass.ib_int(nullable=True, default=1)
    active: bool = AttrsClass.ib_bool(nullable=True, default=True)
    is_leader_1: bool = AttrsClass.ib_bool(nullable=True, default=False)
    is_leader_2: bool = AttrsClass.ib_bool(nullable=True, default=False)
    leader_1_window: Window = AttrsClass.ib_generic(Window, nullable=True, default=None)
    leader_2_window: Window = AttrsClass.ib_generic(Window, nullable=True, default=None)

    def set_window(self, window: Window) -> "Character":
        self.window = window
        return self

    def set_active(self) -> "Character":
        self.active = True
        return self

    def set_inactive(self) -> "Character":
        self.active = False
        return self

    def set_is_leader_1(self) -> "Character":
        self.is_leader_1 = True
        return self

    def set_not_leader_1(self) -> "Character":
        self.is_leader_1 = False
        return self

    def set_is_leader_2(self) -> "Character":
        self.is_leader_2 = True
        return self

    def set_not_leader_2(self) -> "Character":
        self.is_leader_1 = False
        return self

    def set_leader_1_window(self, window: Window) -> "Character":
        self.leader_1_window: Window = window
        return self

    def set_leader_2_window(self, window: Window) -> "Character":
        self.leader_2_window: Window = window
        return self

    @property
    def id(self) -> str:
        return f"{self.account.username}-{self.name}"

    def __hash__(self):
        return hash(self.id)


class CharacterHelper:
    """
    一些对 :class:`Character` 对象的操作的辅助方法.
    """
    @classmethod
    def deduplicate(
        cls,
        chars: T.Iterable["Character"],
    ) -> T.OrderedDict[str, "Character"]:
        """
        根据角色的 ID (account + character name) 对角色进行去重.
        """
        return OrderedDict((char.id, char) for char in chars)

    @classmethod
    def _find_key_char_window(
        cls,
        chars: T.Iterable["Character"],
        attribute: str,
    ) -> T.Optional[Window]:
        """
        一个用于内部实现的方法, 从一堆 Character 当中找到那个扮演某个特定队伍角色的人所在的窗口.

        例如找到谁是一堆角色中的 1 号司机.

        如果一个队伍里有多个人被设为 1 号司机, 那么就设为自然顺序遇到的第一个 1 号司机.
        其他人则会被取消设为一号司机 (该逻辑还没有实现).
        """
        window: T.Optional[Window] = None
        for char in chars:
            if getattr(char, attribute):
                return char.window
        return window

    @classmethod
    def find_leader_1(cls, chars: T.Iterable["Character"]) -> T.Optional[Window]:
        """
        找到一堆角色中的 1 号司机的窗口.
        """
        return cls._find_key_char_window(chars, attribute="is_leader_1")

    @classmethod
    def find_leader_2(cls, chars: T.Iterable["Character"]) -> T.Optional[Window]:
        """
        找到一堆角色中的 2 号司机的窗口.
        """
        return cls._find_key_char_window(chars, attribute="is_leader_2")

    @classmethod
    def _set_key_char_window(
        cls,
        chars: T.Iterable["Character"],
        attr: str,
        window: Window,
    ):
        """
        一个用于内部实现的方法, 用于将一堆角色的某个跟窗口相关的属性统一设定为指定的窗口.

        例如可以将所有角色的 1 号司机设为指定窗口, 除了 1 号司机本人. 这里要注意的是 1 号司机
        本人不会将自己设为一号司机. 司机本人不需要吧自己设为焦点, 而且司机可能随时要临时绑定焦点.
        """
        for char in chars:
            if char.window.label != window.label:
                setattr(char, attr, window)

    @classmethod
    def set_leader_1_window(
        cls,
        chars: T.Iterable["Character"],
        window: Window,
    ):
        """
        将所有角色的 1 号司机窗口设为指定窗口.
        """
        cls._set_key_char_window(chars, "leader_1_window", window)

    @classmethod
    def set_leader_2_window(
        cls,
        chars: T.Iterable["Character"],
        window: Window,
    ):
        """
        将所有角色的 1 号司机窗口设为指定窗口.
        """
        cls._set_key_char_window(chars, "leader_2_window", window)

    @classmethod
    def set_active(cls, chars: T.Iterable["Character"]):
        """
        将多个角色设为 active.
        """
        for char in chars:
            char.active = True
        return chars

    @classmethod
    def set_inactive(cls, chars: T.Iterable["Character"]):
        """
        将多个角色设为 inactive.
        """
        for char in chars:
            char.active = False
        return chars

    @classmethod
    def sort_chars_by_window_label(
        cls,
        chars: T.Iterable["Character"],
    ) -> T.OrderedDict[str, "Character"]:
        """
        将多个角色按照所在的窗口 label (编号) 排序.
        """
        return cls.deduplicate(sorted(chars, key=lambda char: char.window.label))

    @classmethod
    def sort_chars_by_window_title(
        cls,
        chars: T.Iterable["Character"],
    ) -> T.OrderedDict[str, "Character"]:
        """
        将多个角色按照所在的窗口 title (标题) 排序.
        """
        return cls.deduplicate(sorted(chars, key=lambda char: char.window.label))



