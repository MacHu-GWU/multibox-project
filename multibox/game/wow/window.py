# -*- coding: utf-8 -*-

import typing as T

import attrs
from attrs_mate import AttrsClass

T_LABEL_LIKE = T.Union[str, int]  # 类似于 window label 的数据类型
T_LABELS_ARG = T.Union[
    T_LABEL_LIKE, T.List[T_LABEL_LIKE]
]  # 类似于 windows label 的列表的数据类型


@attrs.define
class Window(AttrsClass):
    """
    代表着一个 魔兽世界 客户端窗口.

    每个窗口有一个整数作为编号, 从 1 开始. 如果编号是 1, 那么游戏窗口名为 ``WoW01``,
    label 为 ``w01``.

    :param title: Windows 里的窗口上面的 Title
    :param label: HotkeyNet 脚本里定义的 Label
    """

    title: str = attrs.field()
    label: str = attrs.field()

    @classmethod
    def make_label(cls, index: int) -> str:
        return f"w{str(index).zfill(2)}"

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

    @classmethod
    def to_labels(cls, labels: T_LABELS_ARG) -> T.List[str]:
        """
        把 label-liked 参数转化成字符串形式的 labels. 可供 ``hotkeynet.SendLabel(to=...)``
        API 使用.

        - 如果输入不是 list, 则转化成 list.
        - 如果 list 里的元素是 int, 则转化成 "w01", "w02" 这种形式.
        - 如果 list 里的元素是 str, 则不做处理, 默认已经是 "w01", "w02" 这种形式了.

        :param lbs: int, str, or list of int, list of str.
        """
        if isinstance(labels, list) is False:
            labels = [labels]
        new_labels = list()
        for index in labels:
            if isinstance(index, int):
                new_labels.append(cls.make_label(index))
            else:
                new_labels.append(index)
        return new_labels
