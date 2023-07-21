# -*- coding: utf-8 -*-

"""
Reference:

- https://pngquant.org/
"""

from pathlib_mate import Path

path_pngquant = Path("/opt/homebrew/bin/pngquant")

"""
/opt/homebrew/bin/pngquant 256 --quality=10-10 /Users/sanhehu/Documents/GitHub/multibox-project/docs/source/02-Projects/AzerothCore/src/*.png
"""
def compress_image(
    dir_src: Path,
    dir_dst: Path,
):
    for p in dir_src.select_image():
        if p.basename.endswith("-fs8.png"):
            p.remove()
    args = [
        f"{path_pngquant}",
        f"256",
        "--quality=10-10",
        f"{dir_src}/*.png",
    ]
    cmd = " ".join(args)
    print("run the following command to compress image:")
    print(cmd)
    input("Press ENTER to continue: ")
    dir_dst.mkdir_if_not_exists()
    for p in dir_src.select_image():
        if p.basename.endswith("-fs8.png"):
            new_p = dir_dst.joinpath(p.basename.replace("-fs8.png", ".png"))
            p.moveto(new_p)

dir_src = Path.dir_here(__file__).joinpath("src")
dir_dst = Path.dir_here(__file__).joinpath("dst")
compress_image(dir_src, dir_dst)