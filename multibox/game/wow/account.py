# -*- coding: utf-8 -*-

"""
该模块提供了在多开时的一个魔兽世界账号的抽象.

.. seealso::

    - :class:`Account`
"""

from functools import cached_property

import attrs
from attrs_mate import AttrsClass

from multibox.utils.api import BaseSemiMutableModel


@attrs.define(eq=False, slots=False)
class Account(BaseSemiMutableModel, AttrsClass):
    """
    代表着一个 魔兽世界账号.
    """

    username: str = attrs.field()
    password: str = attrs.field()

    @cached_property
    def hash_key(self) -> str:  # pragma: no cover
        return self.username.lower()

    @cached_property
    def sort_key(self) -> str:  # pragma: no cover
        return self.username.lower()
