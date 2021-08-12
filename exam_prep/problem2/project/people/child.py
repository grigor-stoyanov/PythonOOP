from typing import Tuple

from project.appliances.appliance import DAYS_IN_MONTH


class Child:
    def __init__(self, food_cost: int, *toys_cost: Tuple[float]):
        self.cost = food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        return self.cost * DAYS_IN_MONTH
