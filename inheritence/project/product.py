class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int):
        self.quantity -= quantity if self.quantity - quantity >= 0 else 0

    def increase(self, quantity: int):
        self.quantity += quantity
