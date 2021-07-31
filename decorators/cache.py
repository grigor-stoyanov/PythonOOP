def cache(func):
    log = {}
    def wrapper(n):
        if n in log:
            return log[n]
        else:
            log[n] = func(n)
            return log[n]
    wrapper.log = log
    return wrapper




# test first zero
import unittest


class CacheTests(unittest.TestCase):
    def test_zero_first(self):
        @cache
        def fibonacci(n):
            if n < 2:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        fibonacci(3)
        self.assertEqual(fibonacci.log, {1: 1, 0: 0, 2: 1, 3: 2})


if __name__ == '__main__':
    unittest.main()