# -*- coding: utf-8 -*-

from pathlib_mate import Path
from multibox.game.wow.wlk.dataset import Dataset


def test():
    dir_here = Path.dir_here(__file__)
    dir_module = dir_here.joinpath("tmp")
    ds = Dataset.from_excel(dir_here.joinpath("test_dataset.xlsx"))
    ds.to_module(dir_module=dir_module, overwrite=True)


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.wlk.dataset", preview=False)
