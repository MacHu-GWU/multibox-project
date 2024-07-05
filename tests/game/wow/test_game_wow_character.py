# -*- coding: utf-8 -*-

from ordered_set import OrderedSet
from multibox.game.wow.character import Account, Character


class TestCharacter:
    def test_find_xyz(self):
        acc = Account("admin", "admin")
        char1 = Character(account=acc, name="char1", is_leader_1=True)
        char2 = Character(account=acc, name="char1")
        char3 = Character(account=acc, name="char1")
        chars = OrderedSet([char1, char2, char3])
        assert Character.find_xyz(chars, field="is_leader_1") is char1
        assert Character.find_xyz(chars, field="is_leader_2") is None


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.character", preview=False)
