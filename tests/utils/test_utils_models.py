# -*- coding: utf-8 -*-

import attrs
from functools import cached_property
from multibox.utils.models import BaseSemiMutableModel


# @functools.total_ordering
@attrs.define(eq=False, slots=False)
class GenericAccount(BaseSemiMutableModel):
    username: str = attrs.field()
    password: str = attrs.field()

    @cached_property
    def hash_key(self) -> str:
        return self.username

    @cached_property
    def sort_key(self) -> str:
        return self.username


@attrs.define(eq=False, slots=False)
class Account(GenericAccount):
    pass


class TestBaseSemiMutableModel:
    def test(self):
        acc1_1 = Account(username="user1", password="pass1")
        acc1_2 = Account(username="user1", password="pass1")
        acc1_3 = Account(username="user1", password="pass123")
        assert acc1_1 == acc1_2
        assert acc1_1 == acc1_3
        assert (acc1_1 < acc1_2) is False
        assert (acc1_1 < acc1_3) is False
        assert acc1_1 <= acc1_2
        assert acc1_1 <= acc1_3
        assert hash(acc1_1) == hash(acc1_2)
        assert hash(acc1_1) == hash(acc1_3)
        assert len({acc1_1, acc1_2}) == 1
        assert len({acc1_1, acc1_3}) == 1
        assert len({acc1_1}.difference({acc1_2})) == 0
        assert len({acc1_1}.difference({acc1_3})) == 0


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.utils.models", preview=False)
