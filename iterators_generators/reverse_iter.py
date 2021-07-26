class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start = len(self.iterable)
        self.end = 0

    def __iter__(self):
        return self
    # if we implement the next with pop it will empty the iterable like a map
    def __next__(self):
        if self.start <= self.end:
            raise StopIteration
        self.start -= 1
        return self.iterable[self.start]


for ele in reverse_iter([1, 2, 3]):
    print(ele)
