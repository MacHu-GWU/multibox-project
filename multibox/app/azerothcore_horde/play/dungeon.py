# -*- coding: utf-8 -*-

from ..factory.api import (
    login_char_fact,
    dungeon_active_char_fact,
    game_client_fact,
)
from ..mode import Mode, Team


class ModeFactory:
    @property
    def x5p_horde_s_abcde(self) -> Mode:
        return Mode(
            game_client=game_client_fact.resolution_1920_1080,
            # game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            team=Team(
                active_chars=dungeon_active_char_fact.x5p_s_abcde,
                login_chars=login_char_fact.s_abcde,
            ),
        )


dungeon_mode_fact = ModeFactory()
