class Customer:
    @classmethod
    def id_increment(cls):
        cls.id_count += 1
        return cls.id_count

    id_count = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id_increment()

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}' \
               f'; Email: {self.email}'

    @staticmethod
    def get_next_id():
        next_id = self.id + 1
        return next_id
