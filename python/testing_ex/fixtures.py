"""
Setup and teardown code before a test

pytest testing_ex/fixtures.py
"""

import pytest

@pytest.fixture
def fixture_ex():
    # setup
    n = 5 ** 2
    yield n
    # teardown
    n = 0

def test_fixture(fixture_ex):
    n = fixture_ex
    assert n == 5 ** 2
