import unittest
from collections import Counter

from Homework_3 import ignore_case

class Test(unittest.TestCase):
    def test_ignore_case(self):
        kwargs1 = {'ignore_case': True}
        kwargs2 = {'ignore_case': False}
        clean_lines = ["a", "Aa", "aA", "A"]
        i = ignore_case.IgnoreCase()

        self.assertEqual(i.execute(clean_lines, **kwargs2), Counter({'a': 1, 'Aa': 1, 'aA': 1, 'A': 1}))
        self.assertEqual(i.execute(clean_lines, **kwargs1), Counter({'a': 2, 'Aa': 2}))


if __name__ == "__main__":
    unittest.main()
