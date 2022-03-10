"""
Custom decorator example

Decorators adjust the function they are decorating by returning a "wrapper" function which is configured with
the decorated function

python funcs/decorators/basic_example.py
"""

# Decorator
def double_args(func):
    def wrapper(number: int):
        return func(2 * number)
    return wrapper

# Decorated Functions
@double_args
def double(number: int):
    return 2 * number

@double_args
def square(number: int):
    return number ** 2


# double_args(double)(3)
print(double(3))

# double_args(square)(3)
print(square(3))
