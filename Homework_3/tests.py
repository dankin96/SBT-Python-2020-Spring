import unittest

from uniq import Uniq

FILE_INPUT_NAME = 'src/input.txt'
FILE_OUTPUT_NAME = 'src/output.txt'


class MyTests(unittest.TestCase):

    def testReadEmptyFile(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        with open(uniq.input_path, "w+") as input_file:
            input_file.write("")
        self.assertEqual([], uniq._getlines())

    def testReadNotEmptyFile(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        with open(uniq.input_path, "w+") as input_file:
            input_file.write('A\n')
            input_file.write("A\n")
            input_file.write("A")
        self.assertEqual(["A", "A", "A"], uniq._getlines())

    def testPrintEmptyStringInFile(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        uniq._printWords([''])
        with open(FILE_OUTPUT_NAME, "r") as input_file:
            words = input_file.read().split('\n')
        self.assertEqual([''], words)

    def testPrintNotEmtyString(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        uniq._printWords(['a', 'b', 'c'])
        with open(FILE_OUTPUT_NAME, "r") as input_file:
            words = input_file.read().split('\n')
        self.assertEqual(['a', 'b', 'c'], words)

    def testCountWithOneStringWithoutIgnore(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual({'a': 3}, uniq._countWords(['a', 'a', 'a']))

    def testCountWithtIgnore(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual({'a': 3}, uniq._countWords(['a', 'a', 'a'], True))

    def testCountWithoutIgnoreAndUPletter(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual({'A': 1, 'a': 2}, uniq._countWords(['A', 'a', 'a']))

    def testCountWithIgnoreAndUPletter(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual({'a': 3}, uniq._countWords(['A', 'a', 'a'], True))

    def testCountWithoutArgs(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['A', 'a'], uniq._filter({'A': 1, 'a': 2}))

    def testCountWithCount(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['1 A', '2 a'], uniq._filter({'A': 1, 'a': 2}, count=True))

    def testCountWithUnique(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['A'], uniq._filter({'A': 1, 'a': 2}, unique=True))

    def testCountWithRepeat(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['a'], uniq._filter({'A': 1, 'a': 2}, repeat=True))

    def testCountWithRepeatUnique(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual([], uniq._filter({'A': 1, 'a': 2}, unique=True, repeat=True))

    def testCountWithRepeatUnique(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['2 a'], uniq._filter({'A': 1, 'a': 2}, count=True, repeat=True))

    def testCountWithRepeatUnique(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['1 A'], uniq._filter({'A': 1, 'a': 2}, count=True, unique=True))

if __name__ == '__main__':
    unittest.main()
