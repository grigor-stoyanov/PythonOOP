from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number=table_number, capacity=capacity)

    @property
    def table_number(self):
        return self._table_number

    @table_number.setter
    def table_number(self, value):
        if not 1 <= value <= 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self._table_number = value

