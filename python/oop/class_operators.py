"""
Overload built-in class operators to fine tune standard behaviors

python oop/class_operators.py
"""

class Customer:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return 'Customer: ' + str(self.id)


c1 = Customer(2)
c2 = Customer(2)
c3 = Customer(4)

print(c1 == c2)
print(c2 == c3)
print(c1)