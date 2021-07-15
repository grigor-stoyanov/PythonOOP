from project.animal import Animal


class Lion(Animal):
    MONEYFORCARE = 50
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Lion.MONEYFORCARE)
