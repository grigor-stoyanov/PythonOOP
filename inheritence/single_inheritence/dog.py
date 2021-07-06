from animal import Animal

# single inheritence
class Dog(Animal):
    def bark(self):
        return 'barking'

d = Dog()
print(d.eat())
print(d.bark())