import unittest
from Homework_3 import count

class Test(unittest.TestCase):

    def test_count(self):
        dict_counter = {"A": 1}
        c = count.Count()
        kwargs1 = {'count': True}
        kwargs2 = {'count': False}

        self.assertEqual(c.execute(dict_counter, **kwargs1), "1 A")
        self.assertEqual(c.execute(dict_counter, **kwargs2), "A")


if __name__ == "__main__":
    unittest.main()