"""
Example context manager function

python funcs/context_managers.py
"""

from contextlib import contextmanager

@contextmanager
def custom_context(number: int):
    print('setup')
    try:
        yield 2 * number
    finally:
        print('tear down')


with custom_context(5) as doubled:
    print(doubled)
