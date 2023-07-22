# -*- coding: utf-8 -*-

"""
Todo: doc string here
"""

import typing as T
import attr
from attrs_mate import AttrsClass

from hotkeynet.api import (
    KeyMaker,
    SendLabel,
)
from multibox.game.wow.wlk.api import (
    Account,
    Character,
    CharacterHelper,
    Window,
    Talent as TL,
    TalentCategory as TC,
)
from .factory.api import act

if T.TYPE_CHECKING:
    from multibox.app.azerothcore.play import Mode


@attr.s
class Team(AttrsClass):
    """
    定义了你要使用哪些游戏角色. 包括了:

    1. 使用哪些账号.
    2. 使用哪些角色.
    3. 每个角色在哪个窗口中.
    4. 它们分别是什么天赋, 扮演团队中的什么角色.

    :param active_chars: 指定要使用哪些角色进行游戏, 这些角色是要进入游戏的, 并且多开
        按键将会对这些角色生效.
    :param login_chars: 指定要登录哪些角色. 要进行游戏的角色自动会被视为能用多开按键登录.
        但是在游戏中按下多开按键时候不一定会对这些角色生效, 有可能只是用来上号倒东西的.
        最终要被登录的角色是 active_chars 和 login_chars 的并集. 如果 login_chars
        和 active_chars 的设置有冲突, 则以 active_chars 为准.
    """

    active_chars: T.List[Character] = attr.ib(factory=list)
    login_chars: T.List[Character] = attr.ib(factory=list)
    mode: T.Optional["Mode"] = attr.ib(default=None)

    def _ensure_no_duplicate_window(self, chars: T.List[Character]):
        if len(chars) != len({char.window.label for char in chars}):
            for char in chars:
                print(char.window.label, char.account.username)
            raise ValueError(
                f"Character list {chars} cannot has duplicate window label!"
            )

    @active_chars.validator
    def validate_active_chars(self, attribute, value):
        self._ensure_no_duplicate_window(value)

    @login_chars.validator
    def validate_login_chars(self, attribute, value):
        self._ensure_no_duplicate_window(value)

    def __attrs_post_init__(self):
        # 所有关于 characters 列表的定义
        self.active_chars = list(
            CharacterHelper.sort_chars_by_window_label(self.active_chars).values()
        )
        self.login_chars = list(
            CharacterHelper.sort_chars_by_window_label(self.login_chars).values()
        )

    @property
    def login_window_and_account_pairs(self) -> T.List[T.Tuple[Window, Account]]:
        """
        根据 active_chars 和 login_chars 中的定义, 获得所有被定义的 character
        背后所对应的 Window 和 Account 键值对 并返回, 这里的 Window 和 Account 将要被用于
        自动登录, 并且它们经过基于窗口去重的.
        """
        window_and_account_pairs: T.List[T.Tuple[Window, Account]] = list()
        label_set: T.Set[str] = set()
        for char in self.active_chars:
            if char.window.label not in label_set:
                window_and_account_pairs.append((char.window, char.account))
                label_set.add(char.window.label)
        for char in self.login_chars:
            if char.window.label not in label_set:
                window_and_account_pairs.append((char.window, char.account))
                label_set.add(char.window.label)
        window_and_account_pairs = list(
            sorted(window_and_account_pairs, key=lambda x: x[0])
        )
        return window_and_account_pairs

    @property
    def lbs_all(self) -> T.List[str]:
        """
        返回所有要进行游戏的人物角色所对应的游戏窗口的 label.

        在多开热键定义中, 常用于那些对所有角色生效的按键. 比如 1234, 前进后退等.
        """
        return [char.window.label for char in self.active_chars]

    def lbs_by_tl(self, tl: TL) -> T.List[str]:
        """
        返回所有要进行游戏的人物角色中, 匹配某个具体天赋的角色所对应的游戏窗口的 label.

        在多开热键定义中, 常用于根据天赋筛选部分角色.
        """
        return [
            char.window.label
            for char in CharacterHelper.filter_by_talent(
                chars=self.active_chars,
                tl=tl,
            ).values()
        ]

    def lbs_by_tc(self, tc: TC) -> T.List[str]:
        """
        返回所有要进行游戏的人物角色中, 匹配某个天赋分组的角色所对应的游戏窗口的 label.

        在多开热键定义中, 常用于根据天赋筛选部分角色.
        """
        return [
            char.window.label
            for char in CharacterHelper.filter_by_talent_category(
                chars=self.active_chars,
                tc=tc,
            ).values()
        ]

    @property
    def lbs_tank1(self) -> T.List[str]:
        return [char.window.label for char in self.active_chars if char.is_tank_1]

    @property
    def lbs_tank2(self) -> T.List[str]:
        return [char.window.label for char in self.active_chars if char.is_tank_2]

    @property
    def target_leader_1(self) -> KeyMaker:
        return act.target_leader_key_mapper[
            CharacterHelper.find_leader_1(self.active_chars).label
        ]

    @property
    def target_leader_2(self) -> KeyMaker:
        return act.target_leader_key_mapper[
            CharacterHelper.find_leader_2(self.active_chars).label
        ]

    @property
    def lbs_dr_pala1(self) -> T.List[str]:
        return [char.window.label for char in self.active_chars if char.is_dr_pala_1]

    @property
    def lbs_dr_pala2(self) -> T.List[str]:
        return [char.window.label for char in self.active_chars if char.is_dr_pala_2]

    def remove_inactive_labels(self, label_list: T.List[str]) -> None:
        """
        给定一个 label 的列表, 从中删除那些不存在相对应的 active character 的 label.

        在多开热键定义中, 你可能在 Hotkey 按键中定义了一大批 label, 但是不同的游戏模式下
        你启用的队伍里不见得有这些 label, 所以我们希望将这些 label 移除. 该技巧适合定义
        一个较为通用的键位逻辑, 然后用该函数删除那些不可能有意义的 SendLabel 事件.

        注意, 该函数会修改原有的 label_list, 而不是返回一个新的列表. 因为这个函数的应用场景
        一般是用来修改已经被定义好的 SendLabel 中的 label, 而不是用来生成一个新的 SendLabel.
        """
        all_labels = set(self.lbs_all)
        for label in list(label_list):
            if label not in all_labels:
                label_list.remove(label)

    def remove_tank_labels(self, label_list: T.List[str]) -> None:
        """
        给定一个 label 的列表, 从中删除那些属于坦克角色的 label.

        有时候我们希望全团进行一些动作, 但唯独坦克职业不动.

        注意, 该函数会修改原有的 label_list, 而不是返回一个新的列表. 因为这个函数的应用场景
        一般是用来修改已经被定义好的 SendLabel 中的 label, 而不是用来生成一个新的 SendLabel.
        """
        all_tank_labels = [
            char.window.label
            for char in self.active_chars
            if char.is_tank_1 or char.is_tank_2
        ]
        for label in list(label_list):
            if label in all_tank_labels:
                label_list.remove(label)

    def build_send_label_by_tc(
        self,
        tc: TC,
        funcs: T.Iterable[T.Callable],
    ) -> SendLabel:
        """
        根据天赋组对角色进行筛选, 并生成 SendLabel 对象.
        """
        with SendLabel(
            id=tc.name,
            to=self.lbs_by_tc(tc),
        ) as send_label:
            for func in funcs:
                func()
            return send_label
