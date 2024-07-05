# -*- coding: utf-8 -*-

import multibox.game.wow.wlk.api as api


def test():
    _ = api.T_LABEL_LIKE
    _ = api.T_LABELS_ARG
    _ = api.Window
    _ = api.Account
    _ = api.LocaleEnum
    _ = api.Character
    _ = api.Talent
    _ = api.TalentCategory
    _ = api.Client
    _ = api.Mode
    _ = api.Dataset
    _ = api.get_property_methods
    _ = api.TL
    _ = api.TC


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.wlk.api", preview=False)
