# -*- coding: utf-8 -*-

from hotkeynet.api import CAN
from multibox.game.wow.wlk.api import Window


# 以下的几个设置需要配合宏命令
# w01
TARGET_W01_RA = CAN.SHIFT_(CAN.INSERT)

# w10
TARGET_W10_RJ = CAN.SHIFT_(CAN.HOME)


target_leader_key_mapper_raid_tank = {
    Window.make(1).label: TARGET_W01_RA,
    Window.make(10).label: TARGET_W10_RJ,
}
