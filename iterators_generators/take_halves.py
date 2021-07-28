def solution():
    def integers():
        count = 1
        while True:
            yield count
            count += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        # j = 0
        # for i in seq:
        for i in range(n):
            result.append(next(seq))
            # j += 1
            # result.append(i)
            # if j >= n:
            #     break
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
