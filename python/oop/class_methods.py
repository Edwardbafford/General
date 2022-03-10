# Class attributes and methods
class Bar:
    stuff = 0

    @classmethod
    def add_stuff(cls, value):
        cls.stuff += value
        return cls


print('Bar')
print(Bar.stuff)
Bar.add_stuff(2).add_stuff(3)
print(Bar.stuff)