from typing import List


class Smartphone:
    def __init__(self, memory: int, apps=None, is_on=False):
        self.memory = memory
        if not apps:
            self.apps: List[str] = []
        self.is_on: bool = is_on

    def power(self):
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app: str, memory: int):
        if self.memory >= memory:
            if self.is_on:
                self.apps.append(app)
                self.memory = memory
                return f'Installing {app}'
            else:
                return f'Turn on your phone to install {app}'
        return f'Not enough memory to install {app}'

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'


smartphone = Smartphone(100)
print(smartphone.install('Facebook', 60))
smartphone.power()
print(smartphone.install('Facebook', 60))
print(smartphone.install('Messenger', 20))
print(smartphone.install('Instagram', 40))
print(smartphone.status())
