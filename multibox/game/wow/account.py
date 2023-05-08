# -*- coding: utf-8 -*-

import typing as T
import attr
from attrs_mate import AttrsClass

from superjson import json
from pathlib_mate import Path


@attr.s
class Account(AttrsClass):
    """
    代表着一个 魔兽世界账号.
    """

    username: str = attr.ib()
    password: str = attr.ib()


@attr.s
class AccountLoader(AttrsClass):
    """
    用来从数据文件中加载账号信息.
    """
    path: Path = AttrsClass.ib_generic(Path)
    data: T.Dict[str, str] = AttrsClass.ib_dict(factory=dict)

    def __attrs_post_init__(self):
        self.data = json.loads(self.path.read_text(), ignore_comments=True)

    def load(self, username: str) -> Account:
        return Account(username=username, password=self.data[username])
