"""
Show functions are actually just objects

python funcs/func_objects.py
"""

def double(number: int):
    return 2 * number


x = double
l1 = [print, x]
l1[0](l1[1](5))
