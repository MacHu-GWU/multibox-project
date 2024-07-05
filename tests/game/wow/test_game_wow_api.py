# -*- coding: utf-8 -*-

import multibox.game.wow.api as api


def test():
    _ = api.Account
    _ = api.T_CHARACTER
    _ = api.Character
    _ = api.Talent
    _ = api.TalentCategory
    _ = api.Window
    _ = api.LocaleEnum
    _ = api.Client
    _ = api.Icons
    _ = api.T_LABEL_LIKE
    _ = api.T_LABELS_ARG
    _ = api.TL
    _ = api.TC


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.api", preview=False)
