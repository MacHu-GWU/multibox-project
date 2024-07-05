# -*- coding: utf-8 -*-

import attrs
from ...game import api as game


@attrs.define(eq=False, slots=False)
class Window(game.Window):
    """
    代表着一个 魔兽世界 客户端窗口.

    .. seealso::

        :class:`multibox.game.window.Window`
    """

    @classmethod
    def make_title(cls, index: int) -> str:
        return cls.index_to_text(index=index, prefix="WoW", zfill=2)

    @classmethod
    def make_label(cls, index: int) -> str:
        return cls.index_to_text(index=index, prefix="w", zfill=2)
