"""Smoke test: the shared package installs and imports."""

import dl_course


def test_package_exposes_version() -> None:
    assert dl_course.__version__ == "0.1.0"
