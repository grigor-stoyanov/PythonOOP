from abc import ABC, abstractmethod


class Chair:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Table:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Sofa:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair('victorian Chair')

    def create_table(self):
        return Table('victorian Table')

    def create_sofa(self):
        return Sofa('victorian sofa')


class ArtFactory(AbstractFactory):
    def create_chair(self):
        return Chair('art Chair')

    def create_table(self):
        return Table('art Table')

    def create_sofa(self):
        return Sofa('art sofa')


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair('modern Chair')

    def create_table(self):
        return Table('modern Table')

    def create_sofa(self):
        return Sofa('modern sofa')


def get_factory(style):
    if style == 'victorian':
        return VictorianFactory()
    elif style == 'Art':
        return ArtFactory()
    elif style == 'modern':
        return ModernFactory()


# allows easier extensibility without changing client code

if __name__ == '__main__':
    client_style = input()
    factory = get_factory(client_style)
    print(factory.create_chair())
