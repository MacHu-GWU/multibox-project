# -*- coding: utf-8 -*-

"""
doc site link here ...
"""

import attrs
import functools


@functools.total_ordering
@attrs.define(eq=False, slots=False)
class BaseSemiMutableModel:
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
