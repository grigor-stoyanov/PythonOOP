# adding functionality to existing code
# closely tied to solid principles
# decorators are functions who return functions
user = {"name": "Test", "is_admin": True}
user_not_admin = {"name": 'Testov', "is_admin": False}


# decorators can be a good multitool
def admin_access(ref_func):
    # wrapper can get arguments of the function which functionality we want to modify
    def wrapper(user_obj):
        # instead of returning a modified result
        # we decide weather the function is executed
        if user_obj['is_admin']:
            return ref_func(user_obj)
        raise PermissionError("only admins have access")

    return wrapper


def read_book_content(user):
    if user["is_admin"]:

        print(f"{user['name']} reads the book content")
    else:
        raise PermissionError("only admins have access")


@admin_access
def read_product_content(user):
    print(f'{user["name"]} reads the book content')


read_product_content(user)


# read_book_content(user_not_admin)

def hello_function():
    def say_hi():
        return 'Hi!'

    return say_hi


hello = hello_function()
print(hello())


# python allows access to outer scope of nested functions see number_increment.py
# usually used as validators decorators are a powerful tool
# allows modify behaviour of class/functions and extend behavior of wrapped function
# name of decorator!
def uppercase(function):
    # wrapper does the logic
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


# we want to extend this function to returnr all caps
@uppercase
# @ gets the function below as an argument and calls the decorator function
# when u call the function you are actually calling the wrapper @ does the work for you
def speak():
    return 'hello i am speaking'


print(speak())


# we can use multiple arguments in a decorator function see measure_time
def repeat(n):
    # takes argument of decorator
    def decorator(func):
        # takes reference to function being decorated
        def wraper(*args, **kwargs):
            # wrapper who executes functionality
            for _ in range(n):
                func(*args, **kwargs)

        return wraper

    return decorator


# we for loop a function with decorator
@repeat(4)
def say_hi():
    print('Hello')


say_hi()


# built in decorators
# @classmethod is a decorator that converts a method to a class method
# @abstractmethod converts an instance method into an abstract method
# @property change your class attribute to be used as methods

# classes as decorators
# we need to implement __call__ allows instances to be used as functions
class Fibonacci():
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                # we're recursively calling fib()
                self.cache[n] = self(n - 1) + self(n - 2)
        return self.cache[n]


fib = Fibonacci()
for i in range(5):
    print(fib(i))


# class func_logger:
#     _logfile = 'out.log'
#
#     # adds function reference as attributee!
#     def __init__(self, func):
#         self.func = func
#
#     # implement call
#     def __call__(self, *args):
#         log_string = self.func.__name__ + " was called"
#         with open(self._logfile, 'a') as file:
#             file.write(log_string + '\n')
#         return self.func(*args)


def func_logger(ref_func):
    def wrapper(name):
        with open('log.txt', 'a') as file:
            file.write(f'{ref_func.__name__} was called\n')
        return ref_func(name)

    return wrapper


@func_logger
def say_hi(name):
    print(f'Hi {name}')


say_hi('peter')
say_hi('john')
