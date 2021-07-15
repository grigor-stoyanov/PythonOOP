from collections import defaultdict


class Shop:
    def __init__(self, name, type, capacity):
        self.capacity = capacity
        self.type = type
        self.name = name
        self.items = defaultdict(lambda: 0)

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.capacity > 0:
            self.items[item_name] += 1
            self.capacity -= 1
            return f'added {item_name} to the shop'
        return 'not enough capacity'

    def remove_item(self, item_name, amount):
        if item_name in self.items:
            self.items[item_name] -= amount
            self.capacity += amount
            return f'{amount} {item_name} removed from the shop'
        return f'cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type}' \
               f'with capacity {self.capacity}'


fresh_shop = Shop('Fresh Shop', 'Fruit and Veg', 50)
small_shop = Shop.small_shop('Fashion Boutique', 'Clothes')
print(fresh_shop)
print(small_shop)
print(fresh_shop.add_item('Bananas'))
print(fresh_shop.remove_item('Tomatoes', 2))
print(small_shop.add_item('Jeans'))
print(small_shop.add_item('Jeans'))
print(small_shop.remove_item('Jeans', 2))
