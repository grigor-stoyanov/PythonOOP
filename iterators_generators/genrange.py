def genrange(start, end):
    current_num = start
    while current_num <= end:
        yield current_num
        current_num += 1


print(list(genrange(1, 10)))
