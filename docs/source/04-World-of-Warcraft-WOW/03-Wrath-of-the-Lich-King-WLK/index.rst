Wrath of the Lich King (WLK)
==============================================================================


.. _wow-wlk-dataset:

Dataset
------------------------------------------------------------------------------
在我设计这个软件的初期, 我只有 5 个游戏角色. 但到了后来, 我已经同时在玩 2 个不同的服务器, 共计约 100 多个满级角色, 而且这些角色还分布在联盟部落. 而每一个玩法都是这 100 多个角色进行排列组合. 我大约有 100 多种不同的玩法 (小队副本, 团队副本, 野外, PvP, 练级, 战场, 刷金币, 做任务). 你可以想象, 在不同的玩法下的多开快捷键设置也会有所差异. 所以要想用尽量简单的方式支持这么多游戏角色, 这么多玩法, 就一定要在代码层有所涉及.

Dataset 则是管理着这一切的核心设计. 一个 Dataset 本质上就是一个 Google Sheet (或 Excel) 中, 记录了所有的服务器, 账号, 角色, 天赋, 组队, 玩法的相关数据. 这里是我用来做单元测试的一个示例 `Google Sheet <https://docs.google.com/spreadsheets/d/1gMWItF6I6e6iYZ7wBdqaN_ENjJu8XSc1-7RFmSmGnSc/edit?gid=180066775#gid=180066775>`_ (里面的账号密码角色都是虚构的). 这个 Google Sheet 维护着玩多开时涉及到的所有相关数据.

- **account** 表枚举了所有的账号密码. 在一键打开多个游戏客户端登录的脚本中会用到这些信息.
- **character** 表枚举了所有账号下的游戏角色. 其中 nth_char 可以用来鼠标定位选择对应的角色登录.
- **build** 表枚举了所有可供多开的具体的游戏角色的设置, 其中最重要的是指定每个角色的天赋. 多开脚本会智能的根据角色的天赋来生成对应的快捷键设置. 例如多开脚本中有一个逻辑是按 2 键让所有的 DPS 攻击当前司机角色的目标, 同时治疗职业随机治疗全团. 这个天赋数据就能让脚本智能的发现哪些角色是 DPS, 哪些角色是治疗.
- **build_group** 表把你一个多开玩法中用到的所有角色分到一个组里, 并且定义了在这个玩法下谁是 1 号司机, 谁是 2 号司机, 谁是主坦克, 谁是副坦克等等.
- **client** 表枚举了所有可能用到的游戏客户端. 你在不同的服务器上玩可能会使用不同的客户端. 里面定义了在特定玩法下客户端的分辨率, 以及对应分辨率下各种系统按键的坐标 (例如 roll 物品的按钮坐标).
- **target_key_mapping** 表定义了在不同玩法下选择某个角色时对应的宏按钮的快捷键, 主要是用来设置焦点目标. 详情请参考 :class:`~multibox.game.wow.wlk.mode.Mode`.
- **mode** 表枚举了所有你想要支持的玩法. 而你需要为每个玩法指定用哪个 client, 哪个 build group, 以及用哪个 target_key_mapping.

有了这个表, 我只需要编写号用比较智能化的方式 (根据团队成员不同天赋的构成自动生成) 生成多开脚本的代码, 以后无论我增加了多少个角色, 多少个玩法, 我都只需要简单的在表格中进行简单的编辑, 就能直接开始玩了. 这种设计能大大增加多开脚本的可维护性, 可扩展性, 可读性.

Reference:

- 把表格数据转换为 Python 内存中的数据的模块: https://github.com/MacHu-GWU/multibox-project/blob/app/azerothecore_horde_refactor/multibox/game/wow/wlk/dataset.py
- 把表格数据转化为 Python 枚举模块的脚本例子: https://github.com/MacHu-GWU/multibox-project/blob/main/multibox/tests/game/wow/wlk/test_app/gen_dataset.py
- 一个自动生成的 Python 枚举模块的例子: https://github.com/MacHu-GWU/multibox-project/blob/main/multibox/tests/game/wow/wlk/test_app/dataset.py


Action Key
------------------------------------------------------------------------------
在多开脚本中, 我们经常会定义 "按下什么键", "会起到什么作用" (例如打怪), 为了起到这个作用游戏中的角色需要按哪个动作条上的按钮. 而些键盘上的按键码 1, 2, 3, a, b, c 如果出现在代码中是非常不推荐的代码风格. 时间一长, 你根本不会记得这些按键码对应的逻辑功能.

一个比较推荐的方式是给所有按键码一个变量. 变量名就对应着游戏中的技能名或者描述了你的目的. 而值则是对应的按键码. 这样你的多开脚本中就只是引用这些技能名, 而不是直接引用按键码. 这样你的代码可读性会大大增加. 并且如果你打字出现了错误, 由于按键码的本质是是 Python 变量, 程序会直接报错并引导你找到错误的位置.

`multibox/game/wow/wlk/act <https://github.com/MacHu-GWU/multibox-project/tree/main/multibox/game/wow/wlk/act>`_ 模块定义了魔兽世界巫妖王之怒版本中所有的技能按键的变量, 但是变量的值都是 ``None``. 你可以基于这个模块填写你自己习惯的技能按键.

而我自己习惯的技能按键则在 `multibox/game/wow/wlk/preset/my_act <https://github.com/MacHu-GWU/multibox-project/tree/main/multibox/game/wow/wlk/preset/my_act>`_ 模块中定义了.


Generate HotkeyNet Script
------------------------------------------------------------------------------
我的多开主力工具是 HotkeyNet. 在 :ref:`wow-wlk-dataset` 一章中我说了, 我只需要定义我的玩法需要用到哪些角色, 以及谁是司机, 我就能一键自动生成多开脚本. 这里面的核心技术是在 `multibox/game/wow/wlk/preset/my_mode <https://github.com/MacHu-GWU/multibox-project/tree/main/multibox/game/wow/wlk/preset/my_mode>`_ 模块中用 Python 定义了生成多开脚本的逻辑. 里面所有的 HotkeyNet 的快捷键都是动态生成的.

例如 :meth:`multibox.game.wow.wlk.preset.my_mode.hk_group_03_act_1_to_12.HotkeyGroup03Act1To12Mixin.build_hk_1_heal_tank` 这一段代码实现了我按 1 的时候多开逻辑. 我的常规逻辑是, 按 1 坦克就正常打怪, DPS 跟着坦克输出, 治疗职业则治疗坦克. 但有的时候团队里不止一个坦克, 也不止一个治疗, 这时候不同的治疗可能就需要分别照顾不同的坦克了. 我需要实现无需修改代码, 只需要指定团队成员, 就能自动生成对应的逻辑. 在源代码中你可以看到我们会对团队成员进行分析, 看看有几个治疗. 给这些治疗分配任务时优先分配人治疗主坦克, 然后是副坦克, 然后才是刷团血. 如果团队中没有副坦克, 则副坦克的治疗就会被分配到刷团血. 我们其他的多开按键都是这样实现的. 还有很多例子比如说根据团队中的职业分配轮流打断链, 这里就不再冗述了.

最后, 我只需要维护一个我玩多开的 `Google Sheet <https://docs.google.com/spreadsheets/d/19m889kimzCkbfoc2Q2YOcwN5eYX3Gfja392ns2N6KBQ/edit?gid=180066775#gid=180066775>`_ (这个里面的数据都是真实的, 所有就不放出来了). 每次修改数据后只要将其保存为 ``.xlsx`` 文件, 然后运行一次 `multibox/app/wow_wotlk/gen_dataset.py <https://github.com/MacHu-GWU/multibox-project/blob/main/multibox/app/wow_wotlk/gen_dataset.py>`_ 脚本更新 Python 代码, 然后最后在 `app/wow_wotlk/genereate_script.py <https://github.com/MacHu-GWU/multibox-project/blob/main/app/wow_wotlk/genereate_script.py>`_ 选择我要玩哪个玩法并运行既可生成最终的 hotkeynet 脚本, 一般我只需要点一下 reload 按钮就能开始玩了.
