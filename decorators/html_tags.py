def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f'<{tag}>{func(*args)}</{tag}>'

        return wrapper

    return decorator


# test second zero
import unittest

class TagsTests(unittest.TestCase):
    def test_zero_second(self):
        @tags('h1')
        def to_upper(text):
            return text.upper()
        self.assertEqual(to_upper('hello'), '<h1>HELLO</h1>')

if __name__ == '__main__':
    unittest.main()