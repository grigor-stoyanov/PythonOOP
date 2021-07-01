# a single method should do a single task
# dividing logic in too many functions on your code is called overarchitecture
[print(el) for el in dir(__builtins__)]
# A namespace is a mapping from names to objects i.e dictionary of assigned variables in the code
# on top is the built-in namespace after comes global and local function namespace
# Scope is a region in a program where a namespace is directly accessable

# Global scope
x = 5


def foo():  # local scope
    print(x)


foo()
y = 5
# python works from inside out wiwthin the scope
nums = list(map(int, input().split()))
# it is good practice to define parameters used only in the function within it


x = 5


# in this case x is non-referent type so it will store different values in its scope
# non-referent types are boolen,float,int,string
def some_func():
    x = 6
    print(x)


some_func()
print(x)

# LEGB( Local->Enclosing->Global->Built-in 4 scopes
x = 5


def first():
    y = 6
    def second():
        # looks for y in enclosing scope
        nonlocal y
        y += 100
        print(x)
    print(y)

first()
print(y)
print(globals())
# python reads lines row by row and adds variables,functions to their respective scope
# if something is defined in a lower layer it will not be recognised in an upper unless defined
