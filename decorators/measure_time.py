from time import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(end - start)
        return result

    return wrapper()


@measure_time
def some_func(a, b, c, d=5, e=6):
    start = time()
    end = time()
    print(end - start)
