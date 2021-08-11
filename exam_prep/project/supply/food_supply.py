from project.supply.supply import Supply


class FoodSupply(Supply):
    def __init__(self):
        super().__init__(needs_increase=20)

    def apply(self, survivor):
        survivor.needs += self.needs_increase
