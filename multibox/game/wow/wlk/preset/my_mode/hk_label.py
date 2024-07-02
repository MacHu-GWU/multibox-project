# -*- coding: utf-8 -*-

import typing as T

from hotkeynet import api as hk

if T.TYPE_CHECKING: # pragma: no cover
    from .mode import Mode


class HotkeyLabelMixin:
    def build_labels(self: "Mode"):
        self.labels: T.List[hk.Label] = [
            hk.Label.make(name=window.label, window=window.title)
            for window, _ in self.login_window_and_account_pairs
        ]
        self.n_labels: int = len(self.labels)

    def build_label_mixin(self):
        self.build_labels()
