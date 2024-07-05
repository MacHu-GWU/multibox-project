# -*- coding: utf-8 -*-

"""
Google Sheet: https://docs.google.com/spreadsheets/d/19m889kimzCkbfoc2Q2YOcwN5eYX3Gfja392ns2N6KBQ/edit?gid=361925634#gid=361925634
"""

from pathlib_mate import Path
from multibox.game.wow.wlk.dataset import Dataset

dir_here = Path.dir_here(__file__)
path_excel = Dataset.locate_excel(prefix="multibox-game-wow-wotlk")
ds = Dataset.from_excel(path_excel)

if __name__ == "__main__":
    from pathlib_mate import Path

    dir_here = Path.dir_here(__file__)
    ds.to_module(
        dir_module=dir_here,
        import_mode="from multibox.game.wow.wlk.preset.my_mode.api import Mode",
        overwrite=True,
        test=True,
    )
