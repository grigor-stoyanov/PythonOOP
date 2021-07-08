from typing import List, Optional


class Vet:
    animals = []
    space = 5

    def __init__(self, name: str, animals: Optional[List[str]] = None):
        if animals:
            self.animals = animals
        self.animals = []
        self.name = name

    def register_animal(self, name: str) -> str:
        if Vet.space > 0:
            Vet.animals.append(name)
            self.animals.append(name)
            Vet.space -= 1
            return f"{name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal):
        if animal in Vet.animals:
            Vet.animals.remove(animal)
            self.animals.remove(animal)
            Vet.space += 1
            return f"{animal} unregistered successfully"
        return f"{animal} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


peter = Vet("Peter")
print(peter.register_animal('doggy'))
print(peter.register_animal('doggy'))
print(peter.register_animal('doggy'))
print(peter.register_animal('doggy'))
print(peter.register_animal('doggy'))
print(peter.register_animal('doggy'))
