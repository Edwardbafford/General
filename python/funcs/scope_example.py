"""
Examples of how scope and functions are related

python funcs/scope_example.py
"""

a = 0

def scope_func():
    global a
    a += 1
    b = 0

    def inner_scope_func():
        global a
        a += 1
        nonlocal b
        b += 1
        c = 0
        print(list)  # built-in
        print(a)  # global
        print(b)  # nonlocal
        print(c)  # local

    inner_scope_func()


scope_func()
