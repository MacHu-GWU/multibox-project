# -*- coding: utf-8 -*-

from pathlib_mate import Path
from multibox.game.wow.wlk.dataset import Dataset


def test():
    dir_here = Path.dir_here(__file__)
    dir_module = dir_here.joinpath("dataset")

    # The test excel is from
    path_excel = Dataset.locate_excel(prefix="test_dataset", dir=dir_module)
    ds = Dataset.from_excel(path_excel)

    acc = ds.get_account("Fat01")
    char = ds.get_character("ra_paladin_pve_protect")
    build_group = ds.get_build_group("r_1_to_10")
    client = ds.get_client("zhTW_1600_900")
    mode1 = ds.get_mode("alliance_r_abcde_solo_dungeon")
    mode2 = ds.get_mode("alliance_r_abcdefghij_solo_raid")

    # print(acc)  # for debug only
    # print(char)  # for debug only
    # print(build_group)  # for debug only
    # print(client)  # for debug only
    # print(mode1)  # for debug only
    # print(mode2)  # for debug only

    assert id(ds.get_account("Fat01")) != id(acc)
    assert id(ds.get_character("ra_paladin_pve_protect")) != id(char)
    assert id(ds.get_build_group("r_1_to_10")) != id(build_group)
    assert id(ds.get_client("zhTW_1600_900")) != id(client)
    assert id(ds.get_mode("alliance_r_abcde_solo_dungeon")) != id(mode1)

    # 注: 这里有个 Python 表达式优化的坑, 你如果运行下面的代码, 会发现它们居然相等
    # 这是 Python 的表达式优化的机制, 你如果把这两个返回值取出来用, 它们是不同的对象
    # 所以不用担心.
    # id(ds.get_account("rab01")) == id(ds.get_account("rab01"))

    ds.to_module(dir_module=dir_module, overwrite=True, test=True)


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.wlk.dataset", preview=False)
