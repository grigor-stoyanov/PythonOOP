class Car:
    # self defines the attributes of the class for the current instance
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f'This is {self.name} {self.model} with engine {self.engine}'


audi = Car('Audi', 'R7', 'VW15')
print(audi.get_info())
bmw = Car('bmw', 'x5', 'VW14')