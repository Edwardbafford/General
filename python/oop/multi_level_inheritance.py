class Animal:
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight


class Cat(Animal):
    def __init__(self, size, weight):
        super().__init__(size, weight)

    @staticmethod
    def meow():
        print('Meow!')


class Lion(Cat):
    def __init__(self):
        super().__init__(4, 800)


lion = Lion()
print(lion.size)
print(lion.weight)
help(lion)
