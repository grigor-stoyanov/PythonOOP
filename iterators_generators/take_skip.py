class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start_count = 0
        self.start = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_count >= self.count:
            raise StopIteration
        self.start_count += 1
        self.start += self.step
        return self.start

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
numbers = take_skip(10, 5)
for number in numbers:
    print(number)

