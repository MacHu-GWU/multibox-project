.. _code-structure:

Code Structure
==============================================================================


Overview
------------------------------------------------------------------------------
本仓库包含了我玩的所有游戏所使用的多开脚本的源代码. 我玩的游戏不止一个, 每一个游戏又有不同的版本, 例如, 魔兽世界就有好几部资料片, 每部资料片的设置都是不同的. 在每部资料片中在不同的服务器上玩的设置也不同. 哪些代码可以被复用, 哪些代码需要单独列出来, 实际情况相当复杂. 本文主要讲解了本项目的代码文件目录结构, 如何保持代码结构清晰, 易于维护.


multibox Source Code Structure
------------------------------------------------------------------------------
`multibox <https://github.com/MacHu-GWU/multibox-project/tree/app/azerothecore_horde_refactor/multibox>`_ 目录是项目的 Python 源代码. 它实现了各种游戏的多开功能. 之所以我们用一个 Python 库来解决所有游戏的多开问题是因为多开的本质就是多个窗口的键盘鼠标同步. 这在不同的游戏中是差不太多的, 特别是 MMORPG 网游中有 90% 的逻辑是相同的.

源代码中对于不同游戏的实现是分层的.

例如, **第一层** 是 `multibox/game/ <https://github.com/MacHu-GWU/multibox-project/tree/app/azerothecore_horde_refactor/multibox/game>`_, 也就是不同的游戏. 该目录下的 ``.py`` 模块是对所有游戏通用的工具. 而该目录下的每个子目录则是一个具体的游戏, 例如 `multibox/game/wow/ <https://github.com/MacHu-GWU/multibox-project/tree/app/azerothecore_horde_refactor/multibox/game/wow>`_ 就是魔兽世界.

**第二层** 是某个具体的游戏, 例如 `multibox/game/wow/ <https://github.com/MacHu-GWU/multibox-project/tree/app/azerothecore_horde_refactor/multibox/game/wow>`_ 就是魔兽世界. 该目录下的 ``.py`` 模块是对所有版本通用的工具. 例如对于魔兽世界来说都一定有账号, 所以我们就有 `account.py <https://github.com/MacHu-GWU/multibox-project/blob/app/azerothecore_horde_refactor/multibox/game/wow/account.py>`_, 以及一定有角色, 所以我们就有 `character.py <https://github.com/MacHu-GWU/multibox-project/blob/app/azerothecore_horde_refactor/multibox/game/wow/account.py>`_. 这一层通用的模块都会被汇总到 `api.py <https://github.com/MacHu-GWU/multibox-project/blob/app/azerothecore_horde_refactor/multibox/game/wow/api.py>`_ 中供其他模块 import. 例如魔兽世界某个具体版本的源码中就会从这个 ``api.py`` 中导入一些工具.

**第三层** 是一个游戏下面具体的版本, 例如 `multibox/game/wow/wlk/ <https://github.com/MacHu-GWU/multibox-project/tree/app/azerothecore_horde_refactor/multibox/game/wow/wtk>`_ 就是魔兽世界巫妖王之怒. 该目录下的 ``.py`` 模块是对该特定版本有效的工具. 又例如 `multibox/game/wow/wlk/talent.py <https://github.com/MacHu-GWU/multibox-project/blob/app/azerothecore_horde_refactor/multibox/game/wow/wlk/talent.py>`_ 枚举了魔兽世界巫妖王之怒版本中的所有天赋. 又例如 `multibox/game/wow/wlk/act/ <https://github.com/MacHu-GWU/multibox-project/tree/app/azerothecore_horde_refactor/multibox/game/wow/wlk/act>`_ 枚举了巫妖王之怒版本中的所有职业的所有技能.

**第四层** 则是我自己最习惯, 最喜欢的一种代码架构和预设. 包含键位设定, 快捷键和技能的逻辑对应关系等. 例如 `preset <https://github.com/MacHu-GWU/multibox-project/tree/app/azerothecore_horde_refactor/multibox/game/wow/wlk/preset>`_ 中有我最习惯的快捷键和键位设置, 以及多开的操作逻辑定义.

总结下来, 代码结构如下::

    multibox/
    multibox/game/ # 第一层, 所有游戏
    multibox/game/{game1}/
    multibox/game/{game2}/
    ...
    multibox/game/{common_modules}.py
    ...

    multibox/game/wow # 第二层, 某个具体的游戏, 例如魔兽世界
    multibox/game/wow/{expansion1}/ # 资料片 1, 例如经典旧世
    multibox/game/wow/{expansion2}/
    ...
    multibox/game/wow/{common_modules}.py
    multibox/game/wow/account.py # 游戏账号管理
    multibox/game/wow/character.py # 游戏角色管理
    multibox/game/wow/talent.py # 游戏天赋管理
    ...

    multibox/game/wow/wotlk # 第三层, 某个具体的游戏的具体版本, 例如魔兽世界巫妖王之怒版本
    multibox/game/wow/wotlk/talent.py # 巫妖王之怒天赋
    multibox/game/wow/wotlk/client.py # 巫妖王之怒客户端
    multibox/game/wow/wotlk/mode.py # 巫妖王之怒多开的常见模式
    multibox/game/wow/wotlk/act/ # 巫妖王之怒技能按键绑定
    ...

    multibox/game/wow/wotlk/preset/ # 第四层, 我玩巫妖王之怒版本多开时最习惯的设置
    multibox/game/wow/wotlk/preset/my_act/ # 我习惯的技能按键和宏
    multibox/game/wow/wotlk/preset/my_mode/ # 我习惯的多开模式
    ...

在这个项目中, 我们称层数较低的模块为 "底层模块", 因为它更加通用, 离最终的业务比较远. 而层数较高的模块为 **顶层模块**.


Public API Pattern
------------------------------------------------------------------------------
在每一层模块中一般都会有一个 ``api.py`` 模块. 任何这个模块之外的地方要使用这个模块中的代码 (单元测试除外), 都需要从这个 ``api.py`` 中导入类和函数. 它能确保 public API 的稳定.

另外在我们这个项目中, 底层的模块只会被比它更 **顶层** 的模块 import. 比如 WLK 模块就会用到 WOW 模块中的 API, 但反过来不会.

例如 `multibox.game.api.py <https://github.com/MacHu-GWU/multibox-project/blob/dev/refactor/multibox/game/api.py>`_ 模块就会在 `multibox/game/wow/... <https://github.com/MacHu-GWU/multibox-project/tree/dev/refactor/multibox/game/wow>`_ 中被频繁 import. 由于 game 的模块不会 import 任何顶层模块中的 API, 所以在 wow 中 import game 的时候就可以用完整的路径, 而不会出现循环 import 的问题. 例如: ``import multibox.game.api as game``.


App Code Structure
------------------------------------------------------------------------------
``multibox`` 本身是一个库, 是一个工具. 最终你还是要决定对这个工具进行配置才能真正进行多开游戏. 例如你需要指定多开快捷键. 一个 Application 指的是我用 ``multibox`` 库来在某个游戏中玩多开的具体配置.

每做一个新 App 就会在 `multibox/app/ <https://github.com/MacHu-GWU/multibox-project/tree/dev/refactor-work-on-character/multibox/app>`_ 目录下新建一个文件夹, 并将 app 的源代码以及配置放在里面. 例如 `mltibox/app/wow_wotlk/ <https://github.com/MacHu-GWU/multibox-project/tree/dev/refactor-work-on-character/multibox/app/wow_wotlk>`_ 就是我在魔兽世界巫妖王之怒里多开的 App.
