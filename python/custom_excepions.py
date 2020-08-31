"""
Example with a custom exception
- Create a custom exception
- Throw and catch the exception

python custom_excepions.py
"""

import random


class LowValueException(ArithmeticError):
    """Raised when a value below a threshold is generated"""
    pass


threshold = .5
n = random.random()

try:
    if n <= threshold:
        raise LowValueException()
except LowValueException:
    print('updating n')
    n += .5
finally:
    print(n)
