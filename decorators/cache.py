# def cache(func):
#     # TODO: Implement
#
#
# @cache
def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))
# fibonacci(3)
# print(fibonacci.log)
# fibonacci(4)
# print(fibonacci.log)
