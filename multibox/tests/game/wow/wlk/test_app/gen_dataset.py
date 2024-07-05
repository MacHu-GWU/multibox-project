# -*- coding: utf-8 -*-

"""
This test
"""

from pathlib_mate import Path
from multibox.game.wow.wlk.dataset import Dataset

dir_here = Path.dir_here(__file__)
path_excel = Dataset.locate_excel(prefix="test_dataset", dir=dir_here)
ds = Dataset.from_excel(path_excel)

if __name__ == "__main__":
    from pathlib_mate import Path

    dir_here = Path.dir_here(__file__)
    ds.to_module(dir_module=dir_here, overwrite=True, test=True, verbose=False)
