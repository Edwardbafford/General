"""
Handling expected failures

pytest testing_ex/failures.py
"""

import pytest

@pytest.mark.xfail
def test_failures():
    assert 1 == 2
