def double(number: int) -> int:
    return 2 * number


# pytest type_hints.py will throw an error
print(double('abc'))

help(double)
