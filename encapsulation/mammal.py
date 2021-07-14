class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, type, sound):
        self.sound = sound
        self.type = type
        self.name = name

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


mammal = Mammal('Dog','Domestic','Type')
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())