class Trainer:
    @classmethod
    def id_increment(cls):
        cls.id_count += 1
        return cls.id_count

    id_count = 0

    def __init__(self, name):
        self.name = name
        self.id = Trainer.id_increment()

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'

    @staticmethod
    def get_next_id():
        next_id = Trainer.id_count + 1
        return next_id
