# -*- coding: utf-8 -*-

"""
:class:`multibox.game.wow.wlk.preset.my_mode.Mode` 定义的每一个 HotkeyNet 快捷键
都是由一个函数来生成的. 这个脚本可以遍历这些函数并且从代码中生成文档.
"""

from multibox.game.wow.wlk.preset.my_mode.mode import Mode

for klass in Mode.__mro__:
    for k, v in klass.__dict__.items():
        print(klass.__name__)
        # if k.startswith("build_hk"):
        #     print(f"{klass.__module__}.{klass.__name__}.{k}")
# for k, v in Mode.__dict__.items():
#     print(k, v)