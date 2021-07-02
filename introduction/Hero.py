class Hero:
    # the constructor(init arguments can be different)
    def __init__(self, name_, health_):
        self.name = name_
        self.health = health_

    def defend(self, amount):
        self.health -= amount
        if self.health > 0:
            return
        else:
            self.health = 0
            return f'{self.name} was defeated'

    def heal(self, amount):
        self.health += amount
        return
