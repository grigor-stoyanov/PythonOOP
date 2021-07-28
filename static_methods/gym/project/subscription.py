class Subscription:
    __id_count = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        Subscription.__id_count += 1
        self.exercise_id = exercise_id
        self.trainer_id = trainer_id
        self.customer_id = customer_id
        self.date = date
        self._id = Subscription.__id_count
    @property
    def id(self):
        return Subscription.__id_count

    @id.setter
    def id(self, value):
        value = Subscription.__id_count
        return value

    def __repr__(self):
        return f'Subscription <{self.id}> on {self.date}'

    @staticmethod
    def get_next_id():
        return Subscription.__id_count + 1
