from copy import deepcopy

class CustomList:
    def __init__(self,*args) -> None:
        self.__values = list(args)

    def append(self,value):
        self.__values.append(value)
    
    def remove(self,index):
        try:
            return self.__values.pop(index)
            
        except IndexError:
            raise IndexError('Invalid index')

    def get(self,index):
        return self.__values[index]

    def extend(self,iterable):
        try:
            self.__values.extend(iterable)

        except TypeError:
            self.__values.append(iterable)

        return deepcopy(self.__values)

    def insert(self,index,value):
        if index >= len(self.__values) or index < 0:
            raise IndexError('Invalid index')
        self.__values.insert(index,value)
        return self.__values
    
    def pop(self):
        return self.__values.pop()
    
    def clear(self):
        self.__values.clear()

    def index(self,value):
        return self.__values.index(value)

    def count(self,value):
        return self.__values.count(value)
    
    def reverse(self):
        return list(reversed(self.__values))

    def copy(self):
        return deepcopy(self)
    
    def size(self):
        return len(self.__values)
    
    def add_first(self,value):
        self.__values.insert(0,value)

    def dictionize(self):
        return {ele[0]:ele[1] for ele in zip(self.__values[::2],self.__values[1::2]+[' '])}
    
    def move(self,amount):
        if amount > len(self.__values):
            raise Exception('You\'re trying to move more elements than the list contains')
        self.__values = self.__values[amount:] +self.__values[:amount]
        return self.__values
    
    def sum(self):
        sum = 0
        for ele in self.__values:
            try:
                sum += ele
            except TypeError:
                try:
                    ele_sum = 0
                    for i in ele:
                        ele_sum += i
                    sum += ele_sum
                except TypeError:
                    try:
                        sum += len(ele)
                    except TypeError:
                        raise Exception(f'{ele.__class__.__name__} object doesent have length')
        return sum
    
    def overbound(self):
        max = float('-inf')
        for i,ele in enumerate(self.__values):
            try:
                if ele > max:
                    max = ele
                    max_index = i
            except TypeError:
                try:
                    if len(ele) > max:
                        max = len(ele)
                        max_index = i
                except TypeError:
                    raise Exception(f'{ele.__class__.__name__} object doesent have a value')
        return max_index
   
    def underbound(self):
        min = float('inf')
        for i,ele in enumerate(self.__values):
            try:
                if ele < min:
                    min = ele
                    min_index = i
            except TypeError:
                try:
                    if len(ele) < min:
                        min = len(ele)
                        min_index = i
                except TypeError:
                    raise Exception(f'{ele.__class__.__name__} object doesent have a value')
        return min_index