DAYS_IN_MONTH = 30


class Appliance:
    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * DAYS_IN_MONTH
