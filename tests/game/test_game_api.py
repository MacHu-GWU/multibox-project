# -*- coding: utf-8 -*-


def test():
    from multibox.game import api

    _ = api.T_LABEL_LIKE
    _ = api.T_LABELS_ARG
    _ = api.Window


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.api", preview=False)
