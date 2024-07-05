# -*- coding: utf-8 -*-

"""
该模块提供了在多开时的一个游戏窗口的抽象.
"""

import typing as T
from functools import cached_property


import attrs
from attrs_mate import AttrsClass

from ..utils.models import BaseSemiMutableModel

# 类似于 window label 的数据类型
T_LABEL_LIKE = T.Union[str, int]
# 类似于 windows label 的列表的数据类型
T_LABELS_ARG = T.Union[T_LABEL_LIKE, T.List[T_LABEL_LIKE]]


@attrs.define(eq=False, slots=False)
class Window(BaseSemiMutableModel):
    """
    代表着一个游戏客户端窗口. 一个窗口必须要有一个唯一的 Title, 也就是 Windows 里的窗口
    上面的 Title. 用于 HotkeyNet 来识别并切换窗口. 同时, 一个窗口必须要有一个唯一的 Label,
    也就是 HotkeyNet 脚本用来定义将键盘和鼠标按键发送到哪里的 Label.

    通常在多开时, 我们会开 N 个窗口, 这些窗口的 Title 和 Label 一般由窗口序号加一个前缀构成.
    为了便于排序, 我们一般会在数字前面补 0 用于应付多于 10 个窗口的情况. 例如魔兽世界多开的
    窗口 Title 一般是 WoW01, WoW02, ...; 而 Label 则是 w01, w02, ...;

    :param title: Windows 里的窗口上面的 Title.
    :param label: HotkeyNet 脚本里定义的 Label.
    :param index: 窗口的序号. 从 1 开始.
    """

    index: int = AttrsClass.ib_int()
    title: str = AttrsClass.ib_str()
    label: str = AttrsClass.ib_str()

    @cached_property
    def hash_key(self) -> str:  # pragma: no cover
        return self.label

    @cached_property
    def sort_key(self) -> str:  # pragma: no cover
        return self.label

    @classmethod
    def index_to_text(
        cls,
        index: int,
        prefix: str,
        zfill: int = 2,
    ) -> str:
        return f"{prefix}{str(index).zfill(zfill)}"

    @classmethod
    def make_title(cls, index: int) -> str:  # pragma: no cover
        """
        和 :meth:`index_to_text` 类似, 但这个方法预定义了 title 的 ``prefix`` 和 ``zfill``.
        """
        raise NotImplementedError

    @classmethod
    def make_label(cls, index: int) -> str:  # pragma: no cover
        """
        和 :meth:`index_to_text` 类似, 但这个方法预定义了 label 的 ``prefix`` 和 ``zfill``.
        """
        raise NotImplementedError

    @classmethod
    def new(cls, index: int):
        """
        生成一个新的窗口的工厂函数. 和 ``make`` 项比, 这个方法更为底层.
        """
        return cls(
            index=index,
            title=cls.make_title(index),
            label=cls.make_label(index=index),
        )

    @classmethod
    def to_labels(cls, labels: T_LABELS_ARG) -> T.List[str]:
        """
        把类似于 label 的参数转化成字符串形式的 label list,
        供 ``hotkeynet.SendLabel(to=...)`` API 使用. 业务逻辑如下.

        - 如果输入不是 list, 则转化成 list.
        - 如果 list 里的元素是 int, 则转化成 "w01", "w02" 这种形式.
        - 如果 list 里的元素是 str, 则不做处理, 默认已经是 "w01", "w02" 这种形式了.

        Example:

            # let's say
            # title_prefix = "WoW"
            # label_prefix = "w"
            # zfill = 2
            >>> Window.to_labels(1)
            ["w01"]
            >>> Window.to_labels("w01")
            ["w01"]
            >>> Window.to_labels([1, "w01"])
            ["w01", "w01"]

        :param lbs: int, str, or list of int, list of str.
        """
        if isinstance(labels, list):
            _labels = labels
        else:
            _labels = [labels]

        new_labels = list()
        for label_like in _labels:
            if isinstance(label_like, int):
                new_labels.append(cls.make_label(label_like))
            else:
                new_labels.append(label_like)
        return new_labels
