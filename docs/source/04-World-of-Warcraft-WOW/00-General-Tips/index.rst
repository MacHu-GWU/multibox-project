World of Warcraft General Tips
==============================================================================

``watch -n 5 free -m`` 命令可以查看内存使用量


.. _wow-active-character:

Active Character
------------------------------------------------------------------------------
Active Character 是在多开中的一个重要概念. 例如你在一场游戏中定义了 5 个人物, 但是跑地图打怪用到的是 1, 2, 3 号 3 个人物. 而 4, 5 号人物只是用来登录小号, 倒东西, 挂拍卖行, 聊天, 查看工会频道消息等, 并不参与跑地图打怪. 这时 1, 2, 3 就是 Active Character, 而其他人不是. 在此情况下多开脚本的行为是这样的:

1. 启动游戏时启动所有窗口.
2. 批量输入账号密码登录时, 只登录 3 个人物.
3. 按 1234 操作的时候只操作 3 个人物.
4. 使用单个窗口登录时, 可以选择全部的 5 个人物进行登录.
5. 可以用切换单个窗口快捷键切换到 5 个人物之一的窗口.
6. 用 Round robin 切换窗口时, 只在 3 个人物之间切换.

这样适合于专注于玩几个人物, 但保留快速登录其他人物的能力. 比如登录小号聊天, 倒东西等.


.. _wow-leader:

Leader
------------------------------------------------------------------------------
在多开游戏中, Leader 就是司机, 也是玩家操作的主要人物, 其他角色一般都会将这个司机角色设为焦点, 并在移动中跟随这个 Leader, 以及跟着打怪.

在有些场景下, 是会需要多个 Leader 的. 例如有些战斗中你需要将团队分为两个小队分头行动. 在这种情况下, 你需要明确制定团队中哪个角色是 leader1, 哪个角色是 leader2, 以及从每个角色的视角出发, 它们的 leader 是谁. 例如你有 1-10, 10 个角色, 其中 1 号和 6 号分别是两个 leader tank. 然后从 1 号角色的视角出发, 它的 leader 不存在. 从 2-4 号的视角出发, 它们的 leader 是 1 号. 6-10 号角色同理.

:class:`~multibox.game.wow.character.Character` 类是一个多开游戏中所使用的角色的抽象. 其中有这么几个属性跟 leader 相关:

- ``is_leader_1``: 在团队中, 这个角色是不是 leader 1?
- ``leader_1``: 从自己的视角出发, leader 1 是谁?
- ``is_leader_2``: 在团队中, 这个角色是不是 leader 2?
- ``leader_2``: 从自己的视角出发, leader 2 是谁?

这里要特别特别注意, (``is_leader_1`` + ``leader_1``) 和 (``is_leader_2`` + ``leader_2``) 是两套完全独立, 不同的模式. 玩家可以用多开脚本在两套模式中切换以应付复杂的战斗. 举例说明. 跟前面类似, 我们的团队有 10 个角色, 其中 1 号和 6 号分别是两个 leader tank. 2-4 和 7-10 是两个小队的成员. 在模式 1 下, 1 号和 6 号都是 leader1, 只不过在这个模式下, 1 号是 leader1_1, 6 号是 leader1_2. 这跟``is_leader_2``, ``leader_2`` 毫无关系. 一定不要把模式 1 下的 6 号所扮演的 leader1_2 和 ``leader2`` 搞混淆了, 因为 ``leader2`` 只是在模式 2 下才有意义.


Icon
------------------------------------------------------------------------------
在多开时我们会用到一些游戏中的 ICON, 使得多开的自动化按钮更加直观. 这里我们把一些常用的 ICON 图片放在了 `multibox/game/wow/icons/ <https://github.com/MacHu-GWU/multibox-project/tree/dev/refactor-work-on-character/multibox/game/wow/icons>`_ 目录下, 并提供了一个枚举模块 `multibox/game/wow/icons.py <https://github.com/MacHu-GWU/multibox-project/blob/dev/refactor-work-on-character/multibox/game/wow/icons.py>`_ 以便之后引用.

此外, 还有一个脚本 `compress_icon.py <https://github.com/MacHu-GWU/multibox-project/blob/dev/refactor-work-on-character/docs/source/04-World-of-Warcraft-WOW/00-General-Tips/compress_icon.py>`_ 也非常有用, 它能批量在不怎么牺牲图片质量的情况下, 大大减少 ICON 图片的体积.

.. dropdown:: compress_icon.py

    .. literalinclude:: ./compress_icon.py
       :language: python
       :linenos:
