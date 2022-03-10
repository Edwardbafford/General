"""
Basic testing

pytest testing_ex/basic.py
"""

import pytest


# Functions

def double_small(n: int) -> int:
    if n > 5:
        raise ValueError
    return 2 * n


# Test Code

class TestDoubleSmall:
    def test_basic(self):
        assert double_small(2) == 4, "Input should be doubled!"

    def test_small(self):
        with pytest.raises(ValueError):
            double_small(10)
