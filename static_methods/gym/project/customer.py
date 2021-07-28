class Customer:
    __id_count = 0

    def __init__(self, name, address, email):
        # Customer.__id_count += 1
        self.name = name
        self.address = address
        self.email = email
        self._id = Customer.__id_count

    @property
    def id(self):
        return self.__id_count

    @id.setter
    def id(self, value):
        Customer.__id_count = value
        return Customer.__id_count



    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}' \
               f'; Email: {self.email}'

    @staticmethod
    def get_next_id():
        return Customer.__id_count + 1
