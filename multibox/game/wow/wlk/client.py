# -*- coding: utf-8 -*-

import typing as T

import attrs
from attrs_mate import AttrsClass

from ...wow import api as wow


@attrs.define
class Client(wow.Client):
    """
    在 WOTLK 版本的客户端. 有具体的设置. 例如窗口的位置, 输入框的位置等等.
    """

    # fmt: off
    pass_item_button_x: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    pass_item_button_1_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    pass_item_button_2_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    pass_item_button_3_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    pass_item_button_4_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    rdf_confirm_role_accept_button_x: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    rdf_confirm_role_accept_button_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    rdf_enter_dungeon_button_x: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    rdf_enter_dungeon_button_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    # fmt: on
