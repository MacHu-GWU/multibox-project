# -*- coding: utf-8 -*-


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(
        __file__,
        "multibox.app.wow_wotlk",
        cov_config=".coveragerc-app",
        preview=False,
        is_folder=True,
    )
