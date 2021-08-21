from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self._name = value

    def add_food(self, food_type: str, name: str, price: float):
        food_menu_names = [food.name for food in self.food_menu]
        if name in food_menu_names:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == 'Cake':
            self.food_menu.append(Cake(name, price))
            return f"Added {name} ({food_type}) to the food menu"
        elif food_type == 'Bread':
            self.food_menu.append(Bread(name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        drink_menu_names = [drink.name for drink in self.drinks_menu]
        if name in drink_menu_names:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == 'Tea':
            self.drinks_menu.append(Tea(name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"
        elif drink_type == 'Water':
            self.drinks_menu.append(Water(name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table_repository_numbers = [table.table_number for table in self.tables_repository]
        if table_number in table_repository_numbers:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == 'OutsideTable':
            self.tables_repository.append(OutsideTable(table_number, capacity))
            return f"Added table number {table_number} in the bakery"
        elif table_type == 'InsideTable':
            self.tables_repository.append(InsideTable(table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        if table_number not in [table.table_number for table in self.tables_repository]:
            return f"Could not find table {table_number}"
        table = [ele for ele in self.tables_repository if ele.table_number == table_number][0]
        food_not_in_menu = []
        for food_name in args:
            for food in self.food_menu:
                if food.name == food_name:
                    table.order_food(food)
        for food_name in args:
            if food_name not in [food.name for food in table.food_orders]:
                food_not_in_menu.append(food_name)
        food_order_info = '\n'.join(map(str,table.food_orders))
        food_not_in_menu_info = '\n'.join(food_not_in_menu)
        return f"Table {table_number} ordered:\n" \
               f"{food_order_info}\n" \
               f"{self.name} does not have in the menu:\n" \
               f"{food_not_in_menu_info}"

    def order_drink(self, table_number, *args):
        if table_number not in [table.table_number for table in self.tables_repository]:
            return f"Could not find table {table_number}"
        table = [ele for ele in self.tables_repository if ele.table_number == table_number][0]
        drinks_not_in_menu = []
        for drink_name in args:
            for drink in self.drinks_menu:
                if drink.name == drink_name:
                    table.order_drink(drink)
        for drink_name in args:
            if drink_name not in [drink.name for drink in table.drink_orders]:
                drinks_not_in_menu.append(drink_name)
        drink_order_info = '\n'.join(map(str,table.drink_orders))
        drinks_not_in_menu_info = '\n'.join(drinks_not_in_menu)
        return f"Table {table_number} ordered:\n" \
               f"{drink_order_info}\n" \
               f"{self.name} does not have in the menu:\n" \
               f"{drinks_not_in_menu_info}"

    def leave_table(self, table_number: int):
        table = [ele for ele in self.tables_repository if ele.table_number == table_number][0]
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {table_bill:0.2f}"

    def get_free_tables_info(self):
        tables_info = []
        for table in self.tables_repository:
            tables_info.append(table.free_table_info)
        return '\n'.join(tables_info)

    def get_total_income(self):
        return f'Total income: {self.total_income:0.2f}lv'

bakery = Bakery('test')
bakery.add_food('Cake','margarita',20)
bakery.add_food('Bread','burek',1.50)
bakery.add_drink('Tea','peppermint',40,'agg')
bakery.add_drink('Water','gornabanya',50,'acc')
bakery.add_table('OutsideTable',51,20)
bakery.add_table('OutsideTable',52,25)
bakery.add_table('InsideTable',1,30)
bakery.add_table('InsideTable',2,15)
print(bakery.reserve_table(31))
print(bakery.reserve_table(15))
print(bakery.reserve_table(21))
print(bakery.order_food(4,'sphagetti','meatballs'))
print(bakery.order_drink(3,'sphagetti','meatballs'))
print(bakery.order_food(51,'burek','margarita'))
print(bakery.order_drink(51,'gornabanya','peppermint'))
