"""
Configurable decorator example

run_n_time(n) returns a specially configured decorator
"""

from functools import wraps

def run_n_times(n: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


if __name__ == '__main__':
    @run_n_times(3)
    def test_3():
        print('3')

    @run_n_times(5)
    def test_5():
        print('5')

    test_3()
    test_5()