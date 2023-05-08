# -*- coding: utf-8 -*-

from multibox.game.wow.character import (
    Account,
    Window,
    Character,
    CharacterHelper,
)


class TestCharacter:
    def test_set_method(self):
        window = Window.make(3)
        leader_1_window = Window.make(1)
        leader_2_window = Window.make(2)

        char1 = Character(account=Account("admin", "admin"), name="gm")
        assert char1.is_leader_1 is False
        assert char1.is_leader_2 is False

        char2 = (
            char1.set_window(window)
            .set_active()
            .set_inactive()
            .set_is_leader_1()
            .set_not_leader_1()
            .set_is_leader_2()
            .set_not_leader_2()
            .set_leader_1_window(leader_1_window)
            .set_leader_2_window(leader_2_window)
        )
        assert char1 is char2
        assert char1.id == char2.id


class TestCharacterHelper:
    def test(self):
        a = Character(
            account=Account(username="multi1", password=""),
            name="a",
            window=Window.make(1),
        ).set_is_leader_1()
        b = Character(
            account=Account(username="multi2", password=""),
            name="b",
            window=Window.make(2),
        ).set_is_leader_2()
        chars = [a, b]

        for char in chars:
            assert char.leader_1_window is None
            assert char.leader_2_window is None

        assert CharacterHelper.find_leader_1(chars).index == 1
        assert CharacterHelper.find_leader_2(chars).index == 2

        CharacterHelper.set_leader_1_window(chars, a.window)
        assert a.leader_1_window is None
        assert b.leader_1_window.index == 1

        CharacterHelper.set_leader_2_window(chars, b.window)
        assert a.leader_2_window.index == 2
        assert b.leader_2_window is None

        CharacterHelper.set_inactive(chars)
        for char in chars:
            assert char.active is False

        CharacterHelper.set_active(chars)
        for char in chars:
            assert char.active is True

        CharacterHelper.sort_chars_by_window_label(chars)
        CharacterHelper.sort_chars_by_window_title(chars)


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.character", preview=False)
