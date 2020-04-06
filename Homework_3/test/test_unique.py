import unittest
from Homework_3 import unique

class Test(unittest.TestCase):
    def test_unique(self):
        kwargs1 = {'unique': True}
        kwargs2 = {'unique': False}
        dict_counter = {'a': 1, 'Aa': 2, 'aA': 1, 'A': 4}
        u = unique.Unique()

        self.assertEqual(u.execute(dict_counter, **kwargs1), {'a': 1, 'aA': 1})
        self.assertEqual(u.execute(dict_counter, **kwargs2), {'a': 1, 'Aa': 2, 'aA': 1, 'A': 4})


if __name__ == "__main__":
    unittest.main()