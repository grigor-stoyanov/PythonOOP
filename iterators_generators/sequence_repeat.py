class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if len(self.sequence) > self.number:
            raise StopIteration
        if self.number <= self.i:
            raise StopIteration
        return self.sequence[self.i % len(self.sequence)]


result = sequence_repeat('abc', 2)
for item in result:
    print(item, end='')
