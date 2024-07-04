# -*- coding: utf-8 -*-

"""
This test
"""

from multibox.game.wow.wlk.dataset import Dataset

ds = Dataset.from_excel("test_dataset.xlsx")

if __name__ == "__main__":
    from pathlib_mate import Path

    dir_here = Path.dir_here(__file__)
    ds.to_module(dir_module=dir_here, overwrite=True, test=True)
