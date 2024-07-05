# -*- coding: utf-8 -*-

import typing as T

from ..paths import dir_project_root, dir_htmlcov
from ..vendor.pytest_cov_helper import (
    run_unit_test as _run_unit_test,
    run_cov_test as _run_cov_test,
)


def run_unit_test(
    script: str,
):
    _run_unit_test(
        script=script,
        root_dir=f"{dir_project_root}",
    )


def run_cov_test(
    script: str,
    module: str,
    cov_config: T.Optional[str] = None,
    preview: bool = False,
    is_folder: bool = False,
):
    _run_cov_test(
        script=script,
        module=module,
        root_dir=f"{dir_project_root}",
        htmlcov_dir=f"{dir_htmlcov}",
        cov_config=cov_config,
        preview=preview,
        is_folder=is_folder,
    )
