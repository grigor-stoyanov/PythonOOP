class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__workers_capacity = workers_capacity
        self.__animal_capacity = animal_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget - price >= 0:
            self.__budget -= price
            self.animals.append(animal)
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif len(self.animals) < self.__animal_capacity and self.__budget - price < 0:
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        salaries = sum(map(lambda worker: worker.salary, self.workers))
        if salaries <= self.__budget:
            self.__budget -= sum(salaries)
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        animals_cost = [animal.money_for_care for animal in self.animals]
        if sum(animals_cost) <= self.__budget:
            self.__budget -= sum(animals_cost)
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [lion for lion in self.animals if lion.__class__.__name__ == 'Lion']
        tigers = [tiger for tiger in self.animals if tiger.__class__.__name__ == 'Tiger']
        cheetahs = [cheetah for cheetah in self.animals if cheetah.__class__.__name__ == 'Cheetah']
        # for animal in self.animals:
        # if type(animal) == Lion:
        #   lions_info.append(animal.__repr__())
        #   ...
        return f'You have {len(self.animals)} animals\n' \
               f'----- {len(lions)} Lions:\n' \
               f'{chr(10).join([lion.__repr__() for lion in lions])}\n' \
               f'----- {len(tigers)} Tigers:\n' \
               f'{chr(10).join([tiger.__repr__() for tiger in tigers])}\n' \
               f'----- {len(cheetahs)} Cheetahs:\n' \
               f'{chr(10).join([cheetah.__repr__() for cheetah in cheetahs])}'

    def workers_status(self):
        keepers = [keeper for keeper in self.workers if keeper.__class__.__name__ == 'Keeper']
        caretakers = [caretaker for caretaker in self.workers if caretaker.__class__.__name__ == 'Caretaker']
        vets = [vet for vet in self.workers if vet.__class__.__name__ == 'Vet']
        return f'You have {len(self.workers)} workers\n' \
               f'----- {len(keepers)} Keepers:\n' \
               f'{chr(10).join([keeper.__repr__() for keeper in keepers])}\n' \
               f'----- {len(caretakers)} Caretakers:\n' \
               f'{chr(10).join([caretaker.__repr__() for caretaker in caretakers])}\n' \
               f'----- {len(vets)} Vets:\n' \
               f'{chr(10).join([vet.__repr__() for vet in vets])}'
