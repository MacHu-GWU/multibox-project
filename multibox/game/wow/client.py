# -*- coding: utf-8 -*-

"""
该模块提供了在多开时的一个游戏客户端的抽象.

.. seealso::

    - :class:`Client`
"""

import typing as T
import enum

import attrs
from attrs_mate import AttrsClass


class LocaleEnum(str, enum.Enum):
    """
    客户端语种.
    """
    enUS = "enUS"
    zhCN = "zhCN"
    zhTW = "zhTW"
    koKR = "koKR"
    frFR = "frFR"
    ruRU = "ruRU"
    esES = "esES"
    esMX = "esMX"


@attrs.define
class Client(AttrsClass):
    """
    代表着一个魔兽世界客户端. 例如 3.3.5 的美服客户端.

    :param wow_exe_path: Window 下的 wow.exe 的路径.
    :param locale: 客户端语种.
    :param window_left_top_x: 在桌面上的窗口左上角的 x 坐标 (以下坐标的单位都是像素).
    :param window_left_top_y: 在桌面上的窗口左上角的 y 坐标.
    :param window_width: 在桌面上游戏窗口的宽度.
    :param window_height: 在桌面上游戏窗口的高度.
    :param wrong_password_pop_up_x: 当在登录界面输入了错误的密码时弹出的窗口上的确认按钮
        的 x 坐标, 多开时要点掉这个窗口再输入账号密码进行登录.
    :param wrong_password_pop_up_y: 跟上面类似.
    :param username_input_box_x: 在登录界面输入用户名的输入框的 x 坐标.
    :param username_input_box_y: 跟上面类似.
    :param log_out_button_x: 在游戏内按 ESC 键弹出的菜单中的退出按钮的 x 坐标.
    :param log_out_button_y: 跟上面类似.
    :param return_to_game_button_x: 在游戏内按 ESC 键弹出的菜单中的返回游戏按钮的 x 坐标.
    :param return_to_game_button_y: 跟上面类似.
    :param choose_char_1_x: 选择角色界面的第一个角色的 x 坐标. 所有角色的 x 坐标都是一样的,
    :param choose_char_1_y: 选择游戏界面的第一个角色的 y 坐标.
    :param choose_char_2_y: 跟上面类似.
    :param choose_char_3_y: 跟上面类似.
    :param choose_char_4_y: 跟上面类似.
    :param choose_char_5_y: 跟上面类似.
    :param choose_char_6_y: 跟上面类似.
    :param choose_char_7_y: 跟上面类似.
    :param choose_char_8_y: 跟上面类似.
    :param choose_char_9_y: 跟上面类似.
    :param choose_char_10_y: 跟上面类似.
    """

    # fmt: off
    wow_exe_path: T.Optional[str] = AttrsClass.ib_str(nullable=True, default=None)
    locale: T.Optional[str] = AttrsClass.ib_str(nullable=True, default=None)

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

    def get_choose_char_x_y(self, nth: int) -> T.Tuple[int, int]:
        """
        获取选择第 nth 个角色的坐标.
        """
        return (
            getattr(self, f"choose_char_{nth}_x"),
            getattr(self, f"choose_char_{nth}_y"),
        )
