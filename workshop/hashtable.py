"""Implementing a dictionary with 2 lists"""
from copy import deepcopy


class HashTable:
    def __init__(self):
        """2 private empty lists"""
        # max_capacity increases to 8,16,32... when it exceeds capacity
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    @property
    def length(self):
        return self.max_capacity

    def __setitem__(self, key, value):
        """adds setting up value by key functionality"""
        # check capacity is enough
        if len([el for el in self.__keys if el is not None]) == self.max_capacity:
            self.__enlarge()
        # check if key exists in list
        try:
            index = self.__keys.index(key)
            self.__values[index] = value
            return
        except ValueError:
            index = self.get_available_index(key)
            self.__keys[index] = key
            self.__values[index] = value

    def __getitem__(self, item):
        """adds looking up value by key functionality"""
        try:
            index = self.__keys.index(item)
            return self.__values[index]
        except ValueError:
            raise KeyError('Key is not in dict!')

    def __check_index(self, index):
        """recursively check next available index(linear approach)"""
        # we start from beginning when it reaches the end to cover edge case
        if index == len(self.__keys):
            return self.__check_index(0)
        if self.__keys[index] is None:
            return index
        return self.__check_index(index + 1)

    def __enlarge(self):
        """increase lists capacity and new max capacity"""
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__values = self.__keys + [None] * self.max_capacity
        self.max_capacity *= 2

    def get_available_index(self, key):
        """validation to avoid collision of unavailable index during hashing"""
        index = self.hash(key)
        if self.__keys[index] is None:
            return index
        # we can have linear,quadratic,random approach to solve collision
        available_index = self.__check_index(index)
        return available_index

    def hash(self, key):
        """calculates on which index the value and key must be stored"""
        # index returns a number within max capacity range
        # collision problem for hashing
        index = sum([ord(char) for char in key]) % self.max_capacity
        return index

    def get(self, key, default=None):
        try:
            self.__getitem__(key)
        except KeyError:
            return default

    def __len__(self):
        return len([el for el in self.__keys if el is not None])

    def keys(self):
        return [el for el in self.__keys if el is not None]

    def values(self):
        # if someone decides to add value None it breaks
        keys = self.keys()
        values_list = []
        for key in keys:
            index = self.__keys.index(key)
            values_list.append(self.__values[index])
        return values_list

    def add(self, key, value):
        self.__setitem__(key, value)

    def items(self):
        return list(zip(self.keys(), self.values()))

    def clear(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def __repr__(self):
        to_str = []
        for key, value in self.items():
            to_str.append(f'{key}: {value}')
        return '{' + ', '.join(to_str) + '}'

    def copy(self):
        """in order to copy contents of referent types within copy of referent type"""
        return deepcopy(self)

    def pop(self, key):
        try:
            index = self.__keys.index(key)
            element = self.__values[index]
            self.__keys[index] = None
            self.__values[index] = None
            return element
        except ValueError:
            raise KeyError('Invalid key')

if __name__ == '__main__':

    table = HashTable()
    table['name'] = 'peter'
    table['age'] = 25
    table['age'] = 26
    table.add('work', 'some time')
    print(table['name'])
    print(table.get('5'))
    print(len(table))
    print(table.length)
    print(table)
    print(table.items())
    b = table['random']
    a = 5