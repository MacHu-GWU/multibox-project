# -*- coding: utf-8 -*-

"""

"""

import typing as T
import attr
from attrs_mate import AttrsClass

from .factory.game_client import GameClient
from .team import Team
from .hkn.script import HknScript
from .paths import path_azerothcore_hkn


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

    def render(self, verbose: bool = False) -> str:
        return self.hkn_script.script.render(verbose=verbose)

    def dump(self, verbose: bool = False):
        path_azerothcore_hkn.write_text(self.render(verbose=verbose))
