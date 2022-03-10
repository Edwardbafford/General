# Chain-able Methods
class Foo:
    def __init__(self):
        self.stuff = 0

    def add_stuff(self, value):
        self.stuff += value

    def add_stuff_chain(self, value):
        self.stuff += value
        return self


f1 = Foo()
for i in [1, 2, 3]:
    f1.add_stuff(i)
print('Foo 1')
print(f1.stuff)

f2 = Foo()
f2.add_stuff_chain(1).add_stuff_chain(2).add_stuff_chain(3)
print('Foo 2')
print(f2.stuff)
