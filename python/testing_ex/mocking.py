"""
Mock external dependencies

pytest testing_ex/mocking.py
"""

import pytest
from unittest.mock import MagicMock

class MockedClass:
    @staticmethod
    def mocked_func(n):
        # something external or hard to reproduce
        return n + 20

@pytest.fixture
def mock_fixture():
    thing = MockedClass()
    thing.mocked_func = MagicMock(return_value=23)
    yield thing

def test_mocking(mock_fixture):
    thing = mock_fixture
    assert thing.mocked_func(3) == 23
