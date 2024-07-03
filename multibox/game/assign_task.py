# -*- coding: utf-8 -*-

"""
这是一个用来动态给角色分配任务的脚本.

拿魔兽世界巫妖王之怒来举例. 团队里假设有 奶德, 奶萨, 神牧, 戒律牧, 奶骑一共 5 个治疗.
团队里有 2 个坦克. 还有 18 个 DPS. 那么我怎么定义一套规则给这些治疗分配任务呢?
这里的难点是这套逻辑在团队成员发生变化的时候也要有效果. 比如团队里如果只有奶德, 奶萨和 1 个坦克
的时候, 至少要确保坦克有一个治疗在照顾.

这个模块提供了一个数据结构,
"""

import typing as T


class AssignTask:
    def __init__(
        self,
        groups: T.List[T.Any],
    ):
        self.groups = groups

    def remove(self, item: T.Any):
        for group in self.groups:
            try:
                group.remove(item)
            except ValueError:
                pass
