# design patterns are always used to resolve a problem
# they are at least 20 patterns
# too much design patterns lead to over architecture
# they add layers of abstraction in order to reach flexibility
# abstraction,encapsulation,separation of concirns,coupling and cohesion,separation of interface
# by using a template solution
# creation: initialisation and config of objects
# structural: way to assemble objects to implement new functionality
# behavioural: deal with dynamic interactions between classes
# Singleton pattern: ensure 1 instance for 1 module
# see first_demo_abstract_factory.py
from abc import ABC, abstractmethod

import structlog

if __name__ == '__main__':
    # struct log has built in sigleton
    logger = structlog.get_logger()
    # logger will stay the same if imported in different modules
    logger.msg('greeted', whom='world', more_than_a_string=[1, 2, 3])


# factory pattern:
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class HtmlButton(Button):
    def __init__(self):
        pass

    def click(self):
        print('clicked dom is updated')
        return f'{self.__class__.__name__} clicked'


class WindowsButton(Button):
    def click(self):
        return f'{self.__class__.__name__} clicked'


os = 'windows'


def get_button():
    if os == 'windows':
        return WindowsButton()
    elif os == 'Web':
        return HtmlButton()


# abstract factory see abstract factory.py
# structural patterns: e.g. decorator pattern - add functionality
# fascade pattern - simplify interface
class Cook:
    def prepared_dish(self):
        self.cutter = Cutter()
        self.cutter.cutVegetables()
        self.boiler = Boiler()
        self.boiller.boilVegetables()


# we allow the user to prepare the dish only trough cooking interface without having to know
# the process of preparing it
class Cutter:
    def cutVegetables(self):
        return 'cutting'


class Boiler:
    def boilVegetables(self):
        return 'boiling'


if __name__ == '__main__':
    cook = Cook()
    cook.prepared_dish()


# Behavioral pattern consirned with interaction between objects:
# Command pattern
class RuleResult:
    def __init__(self, is_valid, comments):
        self.is_valid = is_valid
        self.comments = comments


class Rule(ABC):
    @abstractmethod
    def apply(self):
        pass


class HeadersRule(Rule):
    def apply(self, file):
        if self.file.headers == ['ABC', 'asd']:
            return RuleResult(True, {})
        return RuleResult(False, {'missing headers': set(['ABC', 'asd']).difference(self.file.headers)})


class Rule2(Rule):
    def apply(self):
        return RuleResult(False, {'something wrong': 'asd...'})


class RuleEngine:
    def __init__(self, path_to_file, file):
        self.path = path_to_file
        self.original_file = file

    def start(self,rules):
        analysis = []
        for rule in rules:
            analysis.append(rule.apply())
        return analysis


rules = (HeadersRule, Rule2)

if __name__ == '__main__':
    rule_engine = RuleEngine('asd','some_csv')
    # calling start allows us to check the rules for formatting the given file
    # applies the rules with a delay until start is called
    result = rule_engine.start(rules)