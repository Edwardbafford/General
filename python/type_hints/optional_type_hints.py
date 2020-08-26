from typing import Optional


def double(number: Optional[int] = None) -> Optional[int]:
    if number is not None:
        return 2 * number
    else:
        return None


print(double())
print(double(3))

help(double)
