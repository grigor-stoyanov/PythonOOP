from project.dough import empty_string_pro, sub_zero_pro


class Topping:
    def __init__(self, topping_type: str, weight: int):
        self.topping_type = topping_type
        self.weight = weight

    topping_type = empty_string_pro('topping_type')
    weight = sub_zero_pro('weight')