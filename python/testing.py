import pytest

"""
Pytest Examples

pytest testing.py
"""

def test_add():
    assert 1 + 2 == 3

@pytest.mark.parametrize('n', [0, 2, 4])
def test_even(n):
    assert n % 2 == 0
