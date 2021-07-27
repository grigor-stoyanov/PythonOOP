def fibonacci():
    n1, n2 = 0, 1
    yield n1
    yield n1 + n2
    while True:
        n1 = n1 + n2
        yield n1
        n2 = n1 + n2
        yield n2


generator = fibonacci()
for i in range(124):
    print(next(generator))
