class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.start = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start -= 1
        if self.start < 0:
            raise StopIteration
        return self.start


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
