from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food = list(map(lambda x: isinstance(x, FoodSupply), self.supplies))
        if food:
            return food
        raise IndexError('There are no food supplies left!')

    @property
    def water(self):
        water = list(map(lambda x: isinstance(x, WaterSupply), self.supplies))
        if water:
            return water
        raise IndexError('There are no water supplies left!')

    @property
    def salves(self):
        salves = list(map(lambda x: isinstance(x, Salve), self.medicine))
        if salves:
            return salves
        raise IndexError('There are no salves left!')

    @property
    def painkillers(self):
        painkillers = list(map(lambda x: isinstance(x, Painkiller), self.medicine))
        if painkillers:
            return painkillers
        raise IndexError('There are no painkillers left!')

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            meds = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
            meds.apply(survivor)
            self.medicine.remove(meds)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            supply = [s for s in self.supplies if s.__class__.__name__ == sustenance_type][-1]
            supply.apply(survivor)
            self.supplies.remove(supply)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor,'water')
            self.sustain(survivor,'food')
