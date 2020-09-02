"""
Parameterize a test with various arguments

pytest testing_ex/params.py
"""

import pytest

@pytest.mark.parametrize('n', [0, 2, 4])
def test_even(n):
    assert n % 2 == 0
