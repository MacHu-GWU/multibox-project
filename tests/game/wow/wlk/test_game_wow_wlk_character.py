# -*- coding: utf-8 -*-

import typing as T
import pytest

from ordered_set import OrderedSet
from multibox.game.wow.api import (
    Account,
    Window,
)
from multibox.game.wow.wlk.character import (
    Character,
    CharacterHelper,
    TL,
    TC,
)


def check_char_set(char_set: OrderedSet[Character], chars: T.List[Character]):
    assert [c.id for c in char_set] == [c.id for c in chars]


class TestCharacter:
    def test_set_method(self):
        """
        确保这些 set 属性的方法能够正确设置 character 的属性.
        """
        char = Character(account=Account("admin", "admin"), name="gm")
        _ = (
            char.set_tank_1()
            .set_not_tank_1()
            .set_tank_2()
            .set_not_tank_2()
            .set_tank_1_window(window=Window.new(1))
            .set_tank_2_window(window=Window.new(2))
            .set_dr_pala_1()
            .set_dr_pala_2()
            .set_leader_1_tank_1()
            .set_leader_2_tank_2()
            .set_leader_12_and_tank_12()
        )

    def test_set_operation(self):
        """
        确保 character 能够支持集合操作.
        """
        acc = Account("admin", "admin")
        c1 = Character(account=acc, name="char1")
        c2 = Character(account=acc, name="char2")
        c3 = Character(account=acc, name="char3")

        check_char_set(OrderedSet([c1, c2, c2, c3]), [c1, c2, c3])

        s1 = OrderedSet([c1, c2])
        s2 = OrderedSet([c2, c3])
        check_char_set(s1.union(s2), [c1, c2, c3])
        check_char_set(s1.intersection(s2), [c2])
        check_char_set(s1.difference(s2), [c1])


class TestCharacterHelper:
    def test_set_team_leader_and_tank(self):
        a = Character(
            account=Account(username="multi1", password=""),
            name="a",
            window=Window.new(1),
        ).set_leader_12_and_tank_12()
        b = Character(
            account=Account(username="multi2", password=""),
            name="b",
            window=Window.new(2),
        )
        chars = [a, b]

        for char in chars:
            assert char.leader_1_window is None
            assert char.leader_2_window is None
            assert char.tank_1_window is None
            assert char.tank_2_window is None

        CharacterHelper.set_team_leader_and_tank(chars)
        assert b.leader_1_window.label == "w01"
        assert b.leader_2_window.label == "w01"
        assert b.tank_1_window.label == "w01"
        assert b.tank_2_window.label == "w01"

        a = Character(
            account=Account(username="multi1", password=""),
            name="a",
            window=Window.new(1),
        )
        b = Character(
            account=Account(username="multi2", password=""),
            name="b",
            window=Window.new(2),
        )
        with pytest.raises(Exception):
            a.set_is_leader_1()
            b.set_not_leader_1()
            CharacterHelper.set_team_leader_and_tank([a, b])

        with pytest.raises(Exception):
            a.set_not_leader_2()
            b.set_is_leader_2()
            CharacterHelper.set_team_leader_and_tank([a, b])

    def test_sort_and_filter(self):
        a = Character(
            account=Account(username="multi1", password=""),
            name="a",
            window=Window.new(1),
            talent=TL.warrior_pve_protect,
        )
        b = Character(
            account=Account(username="multi2", password=""),
            name="b",
            window=Window.new(2),
            talent=TL.mage_pve_frost,
        )
        c = Character(
            account=Account(username="multi3", password=""),
            name="c",
            window=Window.new(3),
            talent=TL.priest_pve_holy,
        )
        chars = [b, c, a]

        chars_od = CharacterHelper.sort_chars_by_window_label(chars)
        assert list(chars_od.values())[0].window.label == "w01"

        chars_od = CharacterHelper.sort_chars_by_window_title(chars)
        assert list(chars_od.values())[0].window.label == "w01"

        chars_od = CharacterHelper.filter_by_talent(chars, tl=TL.warrior_pve_protect)
        assert len(chars_od) == 1
        assert list(chars_od.values())[0].talent == TL.warrior_pve_protect

        chars_od = CharacterHelper.filter_by_talent_category(chars, tc=TC.tank)
        assert len(chars_od) == 1
        assert list(chars_od.values())[0].talent == TL.warrior_pve_protect

    def test_entity_id(self):
        """
        确保每个 character 的内存中的引用都是不同的.
        """
        c1 = Character(account=Account("admin", "admin"), name="char1")
        c2 = Character(account=Account("admin", "admin"), name="char1")
        assert id(c1) != id(c2)


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.wlk.character", preview=False)
