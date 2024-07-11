# -*- coding: utf-8 -*-

"""
:class:`multibox.game.wow.wlk.preset.my_mode.Mode` 定义的每一个 HotkeyNet 快捷键
都是由一个函数来生成的. 这个脚本可以遍历这些函数并且从代码中生成文档.
"""

from multibox.game.wow.wlk.preset.my_mode.mode import Mode

counter = 0
for klass in Mode.__mro__:
    for k, v in klass.__dict__.items():
        if k.startswith("build_hk") and (not k.startswith("build_hk_group")):
            counter += 1
            print(f"{klass.__module__}.{klass.__name__}.{k}")

print(counter)
