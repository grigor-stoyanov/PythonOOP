# iterators are a class which implements iterator protocol
# __iter__() and __next__() methods allow for an object to be iterable
class A:
    def __iter__(self):
        return self

    def __next__(self):
        # next implementation has the body of a for loop condition,modification,return
        # next always returns the next value until last element
        # when it raises StopIteration
        pass


a = A()
for el in a:
    print(a)
# for cycle can iterate over any iterable and is implemented as:
iter_obj = iter()
while True:
    try:
        ele = next(iter_obj)
    except StopIteration:
        break


# Generators have the same functionality without class
# they instead use a function with the yield keyword
# a function that returns an iterator
def first_n(n):
    num = 0
    while num < n:
        # remembers the state of the function and returns on the row in the yield
        # unlike return it doesent end the function
        yield num
        num += 1


# generators can be saved in variables they return an iterator which has to be
# triggered to be executed (i.e. with a for cycle)
sum_first_n = sum(first_n(5))
print(sum_first_n)
# everytime it yields the element it returns at row 34 num += 1
for el in first_n(5):
    print(el)
# iter and next methods are automatically implemented in yield
# generators can be created using generator expressions or functions (map,reduce,filter...)
my_list = [1, 3, 56, 10]
print([x ** 2 for x in my_list])
# generator
a = (x ** 2 for x in my_list)
# <generator object>
print(a)
# only when next is called the values can be accessed
iter_a = iter(a)
while True:
    try:
        print(next(iter_a))
    except StopIteration:
        break
