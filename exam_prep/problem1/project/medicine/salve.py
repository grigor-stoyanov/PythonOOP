from project.medicine.medicine import Medicine


class Salve(Medicine):
    def __init__(self):
        super().__init__(health_increase=50)

    def apply(self, survivor):
        survivor.health += self.health_increase
