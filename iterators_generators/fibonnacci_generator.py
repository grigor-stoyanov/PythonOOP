def fibonacci():
    n1, n2 = 0, 1
    yield n1
    yield n1 + n2
    while True:
        n1 = n1 + n2
        yield n1
        n2 = n1 + n2
        yield n2


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


from functools import lru_cache


def fibonacci():
    i = 0
    while True:
        yield fib_n(i)
        i += 1


@lru_cache(maxsize=1000)
def fib_n(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_n(n - 1) + fib_n(n - 2)


generator = fibonacci()
for i in range(124):
    print(next(generator))
