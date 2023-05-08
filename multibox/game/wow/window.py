# -*- coding: utf-8 -*-


import attr
from attrs_mate import AttrsClass


@attr.s
class Window(AttrsClass):
    """
    代表着一个 魔兽世界 客户端窗口.

    每个窗口有一个整数作为编号, 从 1 开始. 如果编号是 1, 那么游戏窗口名为 ``WoW01``,
    label 为 ``w01``.

    :param title: Windows 里的窗口上面的 Title
    :param label: HotkeyNet 脚本里定义的 Label
    """

    title: str = attr.ib()
    label: str = attr.ib()

    @classmethod
    def make(cls, index: int) -> "Window":
        return cls(
            title=f"WoW{str(index).zfill(2)}",
            label=f"w{str(index).zfill(2)}",
        )

    @property
    def index(self) -> int:
        """
        integer index of the window.
        """
        return int(self.label[1:])
