# -*- coding: utf-8 -*-

from multibox.game.wow.wlk.talent import TC
from multibox.game.wow.wlk.dataset import Dataset, get_property_methods
from multibox.paths import dir_project_root


def test():
    dir_test_app = dir_project_root.joinpath(
        "multibox",
        "tests",
        "game",
        "wow",
        "wlk",
        "test_app",
    )

    # The test excel is from
    path_excel = Dataset.locate_excel(prefix="test_dataset", dir=dir_test_app)
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

    ds.to_module(dir_module=dir_test_app, overwrite=True, test=True, verbose=False)

    from multibox.tests.game.wow.wlk.test_app.dataset import mode_fact

    for method_name in get_property_methods(mode_fact):
        mode = getattr(mode_fact, method_name)
        _ = mode.active_chars
        _ = mode.login_window_and_account_pairs
        _ = mode.lbs_all
        _ = mode.get_lbs_by_tl
        _ = mode.get_lbs_by_tc
        _ = mode.lb_tank1
        _ = mode.lb_tank2
        _ = mode.lb_dr_pala1
        _ = mode.lb_dr_pala2
        _ = mode.lbs_leader1
        _ = mode.lbs_leader2
        _ = mode.lbs_leader
        _ = mode.lbs_non_leader
        _ = mode.lbs_tank
        _ = mode.lbs_non_tank
        _ = mode.lbs_healer
        _ = mode.lbs_druid_resto
        _ = mode.lbs_shaman_resto
        _ = mode.lbs_priest_holy
        _ = mode.lbs_priest_disco
        _ = mode.lbs_paladin_holy
        _ = mode.build_send_label_by_tc(tc=TC.all, funcs=[lambda: None])
        _ = mode.build_send_label_by_tc(tc=TC.pvp, funcs=[lambda: None])

    mode = mode_fact.alliance_r_abcdefghij_solo_raid
    _ = mode.target_tank_1_key_maker
    _ = mode.target_tank_2_key_maker


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.wlk.dataset", preview=False)
