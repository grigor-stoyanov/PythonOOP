class custom_range:
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __iter__(self):
        # always self because it iterates over self
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        return self.start


for el in custom_range(1, 10):
    print(el)
