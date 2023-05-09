# -*- coding: utf-8 -*-

"""

"""

import typing as T
import attr
from attrs_mate import AttrsClass

from multibox.app.azerothcore.factory.game_client import GameClient
from multibox.app.azerothcore.mode.team import Team
from multibox.app.azerothcore.mode.hkn.script import HknScript


@attr.s
class Mode(AttrsClass):
    """
    :game_client:
    :team:
    :script:
    """

    game_client: T.Optional[GameClient] = attr.ib(default=None)
    team: T.Optional["Team"] = attr.ib(default=None)
    hkn_script: T.Optional["HknScript"] = attr.ib(default=None)

    def __attrs_post_init__(self):
        self.hkn_script = HknScript(mode=self)
