# -*- coding: utf-8 -*-

from multibox.game.wow.api import Account
from multibox.game.wow.wlk.character import Character, TL, TC


class TestCharacter:
    def test_filter_by_talent_and_talent_category(self):
        acc = Account("admin", "admin")

        a = Character(account=acc, name="a", talent=TL.warrior_pve_protect)
        b = Character(account=acc, name="b", talent=TL.mage_pve_frost)
        c = Character(account=acc, name="c", talent=TL.priest_pve_holy)
        chars = [b, a, c]

        chars_od = Character.filter_by_talent(chars, tl=TL.warrior_pve_protect)
        assert len(chars_od) == 1
        assert chars_od[0].talent == TL.warrior_pve_protect

        chars_od = Character.filter_by_talent_category(chars, tc=TC.tank)
        assert len(chars_od) == 1
        assert chars_od[0].talent == TL.warrior_pve_protect

        chars_od = Character.filter_by_talent_category(chars, tc=TC.all)
        assert chars_od[0] is b
        assert chars_od[1] is a
        assert chars_od[2] is c


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.wlk.character", preview=False)
