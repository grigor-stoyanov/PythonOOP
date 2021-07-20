from itertools import count


class Equipment:
    id_count = count().__next__

    def __init__(self, name):
        self.name = name
        self.id = 1 + Equipment.id_count()

    def __repr__(self):
        return f'Equipment <{self.id}>  {self.name}'

    @staticmethod
    def get_next_id():
        next_id = Equipment.id_count + 1
        return next_id
