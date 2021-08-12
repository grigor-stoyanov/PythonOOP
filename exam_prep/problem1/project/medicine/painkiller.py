from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    def __init__(self):
        super().__init__(health_increase=20)

    def apply(self, survivor):
        survivor.health += self.health_increase
