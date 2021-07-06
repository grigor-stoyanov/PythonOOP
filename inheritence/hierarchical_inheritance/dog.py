from animal import Animal


class Dog(Animal):
    def bark(self):
        return 'barking'

d = Dog()
print(d.eat())
print(d.bark())