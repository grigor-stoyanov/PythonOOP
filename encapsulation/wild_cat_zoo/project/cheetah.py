from project.animals.animal import Animal


class Cheetah(Animal):
    MONEYFORCARE = 60
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Cheetah.MONEYFORCARE)
