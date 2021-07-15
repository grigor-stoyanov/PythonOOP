import re
import os
from anytree import Node, PostOrderIter


def camel_case_split(name):
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', name)


product = Node("Product")
food = Node("Food", parent=product)
beverage = Node("Beverage", parent=product)
hot_beverage = Node("HotBeverage", parent=beverage)
cold_beverage = Node("ColdBeverage", parent=beverage)
coffee = Node("Coffee", parent=hot_beverage)
tea = Node("Tea", parent=hot_beverage)
main_dish = Node("MainDish", parent=food)
salmon = Node("Salmon", parent=main_dish)
dessert = Node("Dessert", parent=food)
cake = Node("Cake", parent=dessert)
starter = Node("Starter", parent=food)
soup = Node("Soup", parent=starter)
fork = []
current_dir = os.path.dirname(os.path.abspath(__file__))
for node in PostOrderIter(product):
    file_name = '_'.join(camel_case_split(node.name)).lower()
    file_ancestor ='_'.join(camel_case_split(node.ancestors[-1].name)).lower()
    fork.append(node.name)
    with open(os.path.join(current_dir, 'food', file_name+'.py'), 'w+') as file:
        content = f'from project.food.{file_ancestor} import {node.ancestors[-1].name}\n' \
                  f'\nclass {node.name}({node.ancestors[-1].name}):\n' \
                  f'    def __init(self,name,price):\n' \
                  f'        super().__init(name,price)'
        file.write(content)
    if node.name == 'Food':
        break
for node in PostOrderIter(product,filter_=lambda n: n.name not in fork):
    with open(os.path.join(current_dir, 'beverage', file_name+'.py'), 'w+') as file:
        file_name = '_'.join(camel_case_split(node.name)).lower()
        file_ancestor = '_'.join(camel_case_split(node.ancestors[-1].name)).lower()
        content = f'from project.beverage.{file_ancestor} import {node.ancestors[-1].name}\n' \
                  f'\nclass {node.name}({node.ancestors[-1].name}):\n' \
                  f'    def __init(self,name,price):\n' \
                  f'        super().__init(name,price)'
        file.write(content)
    if node.name == 'Beverage':
        break