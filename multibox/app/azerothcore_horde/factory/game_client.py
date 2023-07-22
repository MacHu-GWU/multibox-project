# -*- coding: utf-8 -*-

"""
该模块枚举了我们可能会用到的魔兽世界客户端程序的配置.
"""


import attr
from attrs_mate import AttrsClass
from superjson import json
from pathlib_mate import Path
from multibox.game.wow.wlk import coordinator
from multibox.game.wow.wlk.game_client import GameClient

from ..paths import path_azerothcore_horde_config_json


@attr.s
class GameClientFactory(AttrsClass):
    """
    用于生成不同分辨率下 GameClient 配置的实例的工厂类.

    Example::

        >>> game_client_fact = GameClientFactory.from_config_file()
        >>> game_client_fact.resolution_1920_1080
        >>> game_client_fact.resolution_1600_900
        >>> game_client_fact.resolution_1176_664

    :param wow_exe_path: 魔兽世界客户端启动器的绝对路径.
    :param locale: 客户端的语言版本.
    """

    wow_exe_path: str = attr.ib(default=None)
    locale: str = attr.ib(default=None)

    @classmethod
    def from_config_file(
        cls,
        path: Path = path_azerothcore_horde_config_json,
    ) -> "GameClientFactory":
        config_data = json.load(path.abspath, verbose=False, ignore_comments=True)
        return cls(**config_data)

    def _use_resolution(self, resolution: str) -> "GameClient":
        """
        一个工厂函数. 根据游戏分辨率的不同, 生成不同的 GameClient 实例.

        例如, 如果 resolution 参数为 "1920_1080", 则会生成一个基于以下配置的设置:

        - window_left_top_x_at_1920_1080 = 120
        - window_left_top_y_at_1920_1080 = 0
        - window_width_at_1920_1080 = 1800
        - window_height_at_1920_1080 = 1012
        - ...
        """
        game_client = GameClient(
            wow_exe_path=self.wow_exe_path,
            locale=self.locale,
        )
        keyword = f"_at_{resolution}"
        for attr in coordinator.__dict__:
            if keyword in attr:
                setattr(
                    game_client,
                    attr.replace(keyword, ""),
                    getattr(coordinator, attr),
                )
        return game_client

    @property
    def resolution_1920_1080(self):
        return self._use_resolution("1920_1080")

    @property
    def resolution_1600_900(self):
        return self._use_resolution("1600_900")

    @property
    def resolution_1176_664(self):
        return self._use_resolution("1176_664")


game_client_fact = GameClientFactory.from_config_file()
