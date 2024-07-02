# -*- coding: utf-8 -*-

import attrs
from attrs_mate import AttrsClass


@attrs.define
class Account(AttrsClass):
    """
    代表着一个 魔兽世界账号.
    """

    username: str = attrs.field()
    password: str = attrs.field()
