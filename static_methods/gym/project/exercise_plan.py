class ExercisePlan:
    @classmethod
    def id_increment(cls):
        cls.id_count += 1
        return cls.id_count

    id_count = 0

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.id_increment()

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id, equipment_id, hours)

    @staticmethod
    def get_next_id():
        next_id = ExercisePlan.id_count + 1
        return next_id

    def __repr__(self):
        return f'Plan <{self.id}> with duration {self.duration} minutes'