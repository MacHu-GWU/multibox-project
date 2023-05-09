# -*- coding: utf-8 -*-

from multibox.app.azerothcore.factory.character import (
    login_char_fact,
    dungeon_active_char_fact,
)
from multibox.app.azerothcore.factory.game_client import game_client_fact
from multibox.app.azerothcore.mode.base import Mode, Team


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
