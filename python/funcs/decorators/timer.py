"""
python funcs/decorators/timer.py
"""

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('{}: {}s'.format(func.__name__, (end - start)))
        return result

    return wrapper


if __name__ == '__main__':
    @timer
    def test(sleep: int, a: int, b: int) -> int:
        """
        Sleep then add :)
        :param sleep: How long to sleep
        :param a: Term A
        :param b: Term B
        :return: A + B
        """
        time.sleep(sleep)
        return a + b


    help(test)
    print(test(2, 1, 2))
