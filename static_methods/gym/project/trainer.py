class Trainer:
    __id_count = 0

    def __init__(self, name):
        Trainer.__id_count += 1
        self.name = name
        self._id = Trainer.__id_count
    @property
    def id(self):
        return Trainer.__id_count

    @id.setter
    def id(self, value):
        value = Trainer.__id_count
        return value

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'

    @staticmethod
    def get_next_id():
        return Trainer.__id_count + 1
