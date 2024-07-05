# -*- coding: utf-8 -*-

"""
doc site link here ...
"""

import attrs
import functools


# ------------------------------------------------------------------------------
# 这是所有模型的基类
# ------------------------------------------------------------------------------
# 先放 @functools.total_ordering 装饰器
@functools.total_ordering
# 再放 @attrs.define 装饰器
# eq=False 表示不生成 __eq__ 方法, 因为默认会自动对所有的属性进行比较, 而我们只对选定的几个属性进行比较
# slots=False 表示不生成 __slots__ 属性, 因为我们需要 @functools.cached_property 装饰器
# 如果有 slots 则没有 __dict__ 属性则不能缓存 property
@attrs.define(eq=False, slots=False)
class BaseModel:
    @functools.cached_property
    def hash_key(self) -> str:
        """
        由用户定义的唯一标识符, 用于在集合操作中计算 hash 值,
        """
        raise NotImplementedError

    @functools.cached_property
    def sort_key(self) -> str:
        """
        由用户定义的排序标识符, 用于在排序操作中进行比较,
        """
        raise NotImplementedError

    # 在 https://www.attrs.org/en/stable/hashing.html 中明确提到了
    # 如果 eq=False 你又自己实现了 hash 方法, 那么子类会自动继承这个 hash 方法
    def __hash__(self):
        return hash(self.hash_key)

    def __eq__(self, other):
        return self.sort_key == other.sort_key

    def __gt__(self, other):
        return self.sort_key > other.sort_key


# ------------------------------------------------------------------------------
# 下面这个例子展示了如何正确定义一个子类
# ------------------------------------------------------------------------------
# @functools.total_ordering
@attrs.define(eq=False, slots=False)
class Account(BaseModel):
    username: str = attrs.field()
    password: str = attrs.field()

    @functools.cached_property
    def hash_key(self) -> str:
        return self.username

    @functools.cached_property
    def sort_key(self) -> str:
        return self.username


class TestHashableMutableModel:
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
    from multibox.tests.helper import run_unit_test

    run_unit_test(__file__)
