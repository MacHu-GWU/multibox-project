# -*- coding: utf-8 -*-

"""
该模块提供了在多开时的一个游戏角色的抽象.

.. seealso::

    - :class:`Character`
"""

import typing as T
from functools import cached_property

import attrs
from attrs_mate import AttrsClass
from multibox.utils.api import BaseSemiMutableModel

from .account import Account
from .window import Window


@attrs.define(eq=False, slots=False)
class Character(BaseSemiMutableModel, AttrsClass):
    """
    代表着一个正在进行的 Character (游戏角色). 这个概念和平时我们提到的游戏中的一个 Character
    普通. 这里的 Character 是指在玩该角色的时候使用了具体的一套天赋, 在这个玩法中这个角色
    扮演的是多开里的 Leader 还是 Follower 的角色等. 例如, 哪怕是同一套天赋下, 但是在不同的玩法中
    一个扮演的是领队, 一个扮演的是跟随者, 这也算是两个不同的 Character. 再举例, 哪怕是
    同一套天赋下, 都是跟随者, 但是一个它跟随的 leader 是 1 号司机, 另一个是 2 号司机, 这也算是
    两个不同的 Character.

    这个类里没有包含任何与职业, 天赋有关的设定. 因为该模块是所有 WoW 版本通用的, 不同版本
    的职业, 天赋是不同的. 这些特定版本才有的信息会在特定版本的 API 里定义.

    .. seealso::

        - :mod:`multibox.game.wow.wlk`
        - :mod:`multibox.game.wow.mop`

    这里有一些重要概念, 建议先看一下这些概念的定义:

    - :ref:`wow-active-character`
    - :ref:`wow-leader`

    下面的属性是 Character 的核心属性, 不会变化.

    :param account: 与该游戏角色所绑定的账号密码信息.
    :param name: 游戏角色名.

    下面的属性在不同的玩法中可能会变化.

    :param window: 该角色所在的游戏窗口.
    :param nth_char: 在人物选择界面位于第几个人物, 从 1 开始计数.
    :param is_active: 这个人物是否是 Active Character.
    :param is_leader_1: 该角色本身是否为 1 号司机.
    :param is_leader_2: 该角色本身是否为 2 号司机.
    :param leader_1: 在该角色的的视角下, 它所跟随的 1 号司机的 :class:`Character` 对象.
        有了这个对象, 我们在做一些需要先选中 1 号司机的操作时, 例如设定司机为焦点, 就可以
        通过这个对象来获取 1 号司机的信息.
    :param leader_2: 在该角色的的视角下, 它所跟随的 1 号司机的 :class:`Character` 对象.

    **设计思路**

    一次多开游戏我们定义为一个 Mode (一个游戏模式), 这个 Mode 会有一个 Active Character
    的集合. 在多开脚本中我们会需要知道哪些角色是坦克, 哪些角色是治疗, 或者说那个角色是扮演主坦,
    哪个角色是副坦, 从而可以智能的定义我们的多开逻辑. 在代码实现的角度看, 我们有两种方法.

    1. 在顶层的 Mode 中设计一些属性, 告诉我们哪个角色扮演主坦, 哪个角色扮演副坦.
    2. 在 Character 对象中设计一个属性, is_tank1, is_tank2, 其值是一个 boolean 对象.

    个人认为第二种方式更好. 因为玩魔兽玩的就是角色, 从角色的视角出发更符合人类直觉. 而且
    扁平化的枚举所有用到的人物, 以及它们扮演的不同角色, 这样的代码更容易读和编辑.

    **注意事项**

    :attr:`Character.leader_1` 和 :attr:`Character.leader_2` 是要跟 HotkeyNet 脚本,
    以及宏命令配合使用的. 这个属性能让多开脚本知道当前的 leader 是谁, 但是从 follower 的角度,
    如果要跟 leader 互动, 还是要借助宏命令. 我们需要知道为了跟某个 leader 互动, 应该按哪个
    快捷键 (上面绑定了宏命令). 而这个 leader 到宏命令按键的映射关系则是在 Mode (游戏模式)
    中定义的.
    """

    account: Account = AttrsClass.ib_generic(Account, nullable=True, default=None)
    name: str = AttrsClass.ib_str(nullable=True, default=None)
    window: Window = AttrsClass.ib_generic(Window, nullable=True, default=None)
    nth_char: int = AttrsClass.ib_int(nullable=True, default=1)
    is_active: bool = AttrsClass.ib_bool(nullable=True, default=True)
    is_leader_1: bool = AttrsClass.ib_bool(nullable=True, default=False)
    is_leader_2: bool = AttrsClass.ib_bool(nullable=True, default=False)
    leader_1: T.Optional["Character"] = attrs.field(default=None)
    leader_2: T.Optional["Character"] = attrs.field(default=None)

    @cached_property
    def hash_key(self) -> str:
        return "{}_{}".format(
            str(self.account.username.lower()).zfill(32),
            str(self.name.lower()).zfill(32),
        )

    @cached_property
    def sort_key(self) -> str:
        return self.name.lower()

    @classmethod
    def find_xyz(
        cls,
        chars: T.Iterable["T_CHARACTER"],
        field: str,
        is_active: bool = True,
    ) -> T.Optional["T_CHARACTER"]:
        """
        一个用于内部实现的方法, 从一堆 Character 当中找到那个扮演某个特定队伍角色的人所在的
        Character. 例如找到谁是一堆角色中的 1 号司机. 如果一个队伍里有多个人被设为 1 号司机,
        那么就将自然顺序遇到的第一个 Character 定为 1 号司机. 如果没有找到则返回 None.
        大多数情况不会遇到有多个人满足条件的情况, 因为在创建这个集合的时候我们就已经经过了去重.
        """
        for char in chars:
            if getattr(char, field):
                if is_active:
                    if char.is_active:
                        return char
                else:
                    return char
        return None


T_CHARACTER = T.TypeVar("T_CHARACTER", bound=Character)
