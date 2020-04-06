import unittest
from Homework_3 import repeat

class Test(unittest.TestCase):
    def test_repeat(self):
        kwargs1 = {'repeat': True}
        kwargs2 = {'repeat': False}
        dict_counter = {'a': 1, 'Aa': 2, 'aA': 1, 'A': 4}
        d = repeat.Repeat()

        self.assertEqual(d.execute(dict_counter, **kwargs1), {'Aa': 2, 'A': 4})
        self.assertEqual(d.execute(dict_counter, **kwargs2), {'a': 1, 'Aa': 2, 'aA': 1, 'A': 4})


if __name__ == "__main__":
    unittest.main()
