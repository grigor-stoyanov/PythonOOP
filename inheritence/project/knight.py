from project.hero import Hero


class Knight(Hero):
    def __init__(self, name, level):
        super().__init__(name, level)

    def __str__(self):
        return super().__str__()
