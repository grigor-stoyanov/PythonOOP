class Subscription:
    @classmethod
    def id_increment(cls):
        cls.id_count += 1
        return cls.id_count
    id_count = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.exercise_id = exercise_id
        self.trainer_id = trainer_id
        self.customer_id = customer_id
        self.date = date
        self.id = Subscription.id_increment()

    def __repr__(self):
        return f'Subscription <{self.id}> on {self.date}'

    @staticmethod
    def get_next_id():
        next_id = Subscription.id_count + 1
        return next_id
