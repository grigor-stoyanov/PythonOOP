# generator solution
def squares(n):
    current_num = 1
    while current_num <= n:
        yield current_num ** 2


for el in squares(5):
    print(el)
print(list(squares(5)))

# iterator solution
class Squares:
    def __init__(self, end):
        self.end = end
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        return self.start ** 2
