# -*- coding: utf-8 -*-

"""
该模块枚举了我们可能会用到的魔兽世界客户端程序的配置.
"""

from multibox.game.wow.wlk import coordinator
from multibox.game.wow.wlk.game_client import GameClient

from multibox.app.azerothcore.config import config


class GameClientFactory:
    """
    用于生成不同分辨率下 GameClient 配置的实例的工厂类.

    Example::

        >>> game_client_fact = GameClientFactory()
        >>> game_client_fact.resolution_1920_1080
        >>> game_client_fact.resolution_1600_900
        >>> game_client_fact.resolution_1176_664
    """

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
            wow_exe_path=config.wow_exe_path,
            locale=config.locale,
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


game_client_fact = GameClientFactory()
