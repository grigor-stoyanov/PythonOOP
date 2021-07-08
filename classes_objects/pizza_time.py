class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict, ordered=False):
        self.ingredients = ingredients
        self.price = price
        self.name = name
        self.ordered = ordered

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float) -> None:
        if not self.ordered:
            self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
            self.price += quantity * price_per_ingredient
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float) -> None:
        if not self.ordered:
            r = self.ingredients.get(ingredient,
                                     f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!")
            if isinstance(r, str):
                return r
            elif r < quantity:
                return f"Please check again the desired quantity of {ingredient}!"
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= quantity * price_per_ingredient
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with " \
               f"{', '.join([f'{key}: {value}' for key, value in self.ingredients.items()])}" \
               f" and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
