# -*- coding: utf-8 -*-

from multibox.app.wow_wotlk.dataset import mode_fact
from multibox.game.wow.wlk.api import get_property_methods


def test():
    for property_name in get_property_methods(mode_fact):
        mode = getattr(mode_fact, property_name)
        mode.render(verbose=False)


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(
        __file__,
        "multibox.app.wow_wotlk",
        cov_config=".coveragerc-app",
        preview=False,
        is_folder=True,
    )
