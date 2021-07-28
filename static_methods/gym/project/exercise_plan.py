class ExercisePlan:
    __id_count = 0

    def __init__(self, trainer_id, equipment_id, duration):
        ExercisePlan.__id_count += 1
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self._id = ExercisePlan.__id_count

    @property
    def id(self):
        return ExercisePlan.__id_count

    @id.setter
    def id(self, value):
        value = ExercisePlan.__id_count
        return value
    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id, equipment_id, hours * 60)

    @staticmethod
    def get_next_id():
        return ExercisePlan.__id_count + 1

    def __repr__(self):
        return f'Plan <{self.id}> with duration {self.duration} minutes'
