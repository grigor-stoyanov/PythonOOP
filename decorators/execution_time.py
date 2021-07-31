import time as tm


def exec_time(func):
    def wrapper(*args):
        start = tm.time()
        func(*args)
        end = tm.time()
        return end - start

    return wrapper
