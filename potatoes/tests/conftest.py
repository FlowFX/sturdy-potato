"""Fixture and other pytest options."""

import pytest


def pytest_addoption(parser):
    """pytest commandline option to run slow tests.

    cf. http://doc.pytest.org/en/latest/example/simple.html\
    #control-skipping-of-tests-according-to-command-line-option
    """
    parser.addoption("--runslow", action="store_true",
        help="run slow tests")