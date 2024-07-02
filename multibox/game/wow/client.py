# -*- coding: utf-8 -*-

import typing as T

import attrs
from attrs_mate import AttrsClass


@attrs.define
class Client(AttrsClass):
    """
    代表着一个魔兽世界客户端. 例如 3.3.5 的美服客户端.
    """

    # fmt: off
    window_left_top_x: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    window_left_top_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    window_width: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    window_height: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    wrong_password_pop_up_x: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    wrong_password_pop_up_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    username_input_box_x: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    username_input_box_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    log_out_button_x: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    log_out_button_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    return_to_game_button_x: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    return_to_game_button_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_1_x: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_1_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_2_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_3_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_4_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_5_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_6_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_7_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_8_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_9_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    choose_char_10_y: T.Optional[int] = AttrsClass.ib_int(nullable=True, default=None)
    # fmt: on
