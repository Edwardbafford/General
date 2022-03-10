"""
Example that uses @property to restrict access to class attributes

python oop/class_properties.py
"""

class Person:
    def __init__(self, w, h):
        self._weight = w
        self._height = h

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, w):
        if w <= 0:
            raise ValueError("weight must be greater than 0")
        self._weight = w


p1 = Person(100, 60)
p1.weight = -20
