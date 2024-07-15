# -*- coding: utf-8 -*-

"""
:class:`multibox.game.wow.wlk.preset.my_mode.Mode` 定义的每一个 HotkeyNet 快捷键
都是由一个函数来生成的. 这个脚本可以遍历这些函数并且从代码中生成文档.
"""

import jinja2
from pathlib_mate import Path
from multibox.game.wow.wlk.preset.my_mode.mode import Mode

method_list = list()
counter = 0
for klass in Mode.__mro__:
    for k, v in klass.__dict__.items():
        if k.startswith("build_hk") and (not k.startswith("build_hk_group")):
            counter += 1
            meth = f"{klass.__module__}.{klass.__name__}.{k}"
            print(meth)
            method_list.append(meth)

dir_here = Path.dir_here(__file__)
p_tpl = dir_here / "index.rst.jinja2"
p_doc = dir_here / "index.rst"

tpl = jinja2.Template(p_tpl.read_text())
content = tpl.render(method_list=method_list)
p_doc.write_text(content)
