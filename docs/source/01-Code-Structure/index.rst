Code Structure
==============================================================================


Overview
------------------------------------------------------------------------------
本仓库包含了我玩的所有游戏所使用的多开脚本的源代码. 我玩的游戏不止一个, 每一个游戏又有不同的版本, 例如魔兽世界就有好几部资料片, 每部资料片的设置都是不同的. 在每部资料片中在不同的服务器上玩的设置也不同. 哪些代码可以被复用, 哪些代码需要单独列出来, 实际情况相当复杂. 本文主要讲解了本项目的代码文件目录结构, 如何保持代码结构清晰, 易于维护.


Structure
------------------------------------------------------------------------------
项目根目录有两个文件夹, app 是用来保存最终用来生成 Hotkeynet 脚本的 Python 代码的. 一个 app 指的是我在具体的游戏, 具体的版本, 具体的服务器上的具体设置. 每个 app 之间相互独立. 而 multibox 则是 Python 源码, 需要 import 后再使用.::

    /app
    /multibox

Multibox 目录下有两个重要文件夹 app 和 game. app 是用来保存归属于每个具体的 app 的相关模块. 而 game 则是用来根据游戏, 版本进行层级归类, 将某个游戏或某个版本下常用的公共模块放在这里.

    /multibox/app
    /multibox/game

我们先来看 game 目录, 它的目录结构是 ``/multibox/game/${game_name}/${game_version}``::

    /multibox/game
    /multibox/game/wow 魔兽世界游戏通用的模块
    /multibox/game/wow/wlk 只跟魔兽世界巫妖王之怒相关的模块
    /multibox/game/wow/mop 只跟魔兽世界熊猫人之谜相关的模块

我们再来看 app 目录, 下面有几个子目录::

    /multibox/app/azerothcore # 魔兽世界 巫妖王之怒版本 azerothcore 服务器
    /multibox/app/warmane # 魔兽世界 巫妖王之怒版本 warmane 服务器
    /multibox/app/tauri # 魔兽世界 熊猫人之谜 tarui 服务器

最后我们回过头来看根目录下的 app 目录, 里面的结构跟 ``/multibox/app`` 类似::

    /app/azerothcore # 魔兽世界 巫妖王之怒版本 azerothcore 服务器
    /app/warmane # 魔兽世界 巫妖王之怒版本 warmane 服务器
    /app/tauri # 魔兽世界 熊猫人之谜 tarui 服务器
