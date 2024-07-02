# -*- coding: utf-8 -*-

from pathlib_mate import Path
from multibox.game.wow.wlk.dataset import Dataset

dir_here = Path.dir_here(__file__)
path_excel = dir_here.joinpath("multibox-game-wow-wotlk-azerothcore_alliance_v2.xlsx")
ds = Dataset.from_excel(path_excel)

if __name__ == "__main__":
    from pathlib_mate import Path

    dir_here = Path.dir_here(__file__)
    ds.to_module(dir_module=dir_here, overwrite=True)
