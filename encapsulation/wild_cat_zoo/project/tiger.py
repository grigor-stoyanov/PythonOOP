from project.animals.animal import Animal


class Tiger(Animal):
    MONEYFORCARE = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Tiger.MONEYFORCARE)
