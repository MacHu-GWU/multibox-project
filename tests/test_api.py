# -*- coding: utf-8 -*-


def test():
    from multibox import api


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.api", preview=False)
