"""
Closure example

Closures can be used to configure a function

python funcs/closure_example.py
"""

def outer_func(number: int):
    a = 2 * number

    def inner_func():
        return a

    return inner_func


f1 = outer_func(5)
print(f1())
print(f1.__closure__[0].cell_contents)
