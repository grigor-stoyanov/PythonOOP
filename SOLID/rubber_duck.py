from abc import ABC, abstractmethod


# duck didn't have any initial functionality to pass on to its children
class Duck(ABC):
    # every duck can quack so method should be in the abstract class
    @staticmethod
    @abstractmethod
    def quack():
        return "Squeek"
    # not every duck can walk so we can't put it here
    # @staticmethod
    # def walk():
    #     pass


# rubber duck wont work if substituted for duck
class RubberDuck(Duck):
    # @staticmethod
    # def quack():
    #     return "Squeek"

    @staticmethod
    def walk():
        """Rubber duck can walk only if you move it"""
        raise Exception('I cannot walk by myself')
    # according to interface aggregation this should not exist
    # @staticmethod
    # def fly():
    #     """Rubber duck can fly only if you throw it"""
    #     raise Exception('I cannot fly by myself')


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    # @staticmethod
    # def quack():
    #     return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


class LiveDuck(Duck):
    def eat(self):
        pass


class StatickDuck(Duck):
    def stay_still(self):
        pass

# interface segregation client should not depend on methods it does not use
class GreenDuck(LiveDuck):
    pass
