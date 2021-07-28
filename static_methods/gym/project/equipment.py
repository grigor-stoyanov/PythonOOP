class Equipment:
    __id_count = 0

    def __init__(self, name):
        Equipment.__id_count += 1
        self.name = name
        self._id = Equipment.__id_count

    @property
    def id(self):
        return Equipment.__id_count

    @id.setter
    def id(self, value):
        value = Equipment.__id_count
        return value

    def __repr__(self):
        return f'<{id}>  {self.name}'

    @property
    def id(self):
        return Equipment.__id_count

    @id.setter
    def id(self, value):
        return Equipment.__id_count
    @staticmethod
    def get_next_id():
        return Equipment.__id_count + 1
