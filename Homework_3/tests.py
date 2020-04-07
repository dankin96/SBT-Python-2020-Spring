import unittest
from uniq import Uniq

FILE_INPUT_NAME = 'src/empty.txt'
FILE_OUTPUT_NAME = 'src/outputReady.txt'


class MyTests(unittest.TestCase):

    def readNotEmptyFileTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        with open(uniq.input_path, "w+") as input_file:
            input_file.write('Eugene\n')
            input_file.write("Eugene\n")
            input_file.write("Eugene")
        self.assertEqual(["Eugene", "Eugene", "Eugene"], uniq._getLine())

    def printEmptyStringInFileTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        uniq._wordPrinter([''])
        with open(FILE_OUTPUT_NAME, "r") as input_file:
            words = input_file.read().split('\n')
        self.assertEqual([''], words)

    def printNotEmtyStringTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        uniq._wordPrinter(['Eugene', 'SBT', '2020'])
        with open(FILE_OUTPUT_NAME, "r") as input_file:
            words = input_file.read().split('\n')
        self.assertEqual(['Eugene', 'SBT', '2020'], words)

    def countWithOneStrWithoutIgnoreTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual({'a': 3}, uniq._countOfWords(['a', 'a', 'a']))

    def countWithIgnoreTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual({'a': 3}, uniq._countOfWords(['a', 'a', 'a'], True))

    def countWithoutIgnoreAndUpperLettersTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual({'Eugene': 1, 'eugene': 2}, uniq._countOfWords(['Eugene', 'eugene', 'eugene']))

    def countWithIgnoreAndUpperLettersTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual({'a': 3}, uniq._countOfWords(['Eugene', 'eugene', 'eugene'], True))

    def countWithoutArgsTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['Q', 'q'], uniq._switchCaseFilter({'Q': 1, 'q': 2}))

    def countWithNumbersTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['1 Q', '2 q'], uniq._switchCaseFilter({'Q': 1, 'q': 2}, count=True))

    def countWithRepeatTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['z'], uniq._switchCaseFilter({'Z': 1, 'z': 2}, repeat=True))

    def countWithUniqueTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['X'], uniq._switchCaseFilter({'X': 1, 'x': 2}, unique=True))

    def countWithRepeatAndUniqueTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual([], uniq._switchCaseFilter({'S': 1, 's': 2}, unique=True, repeat=True))

    def countWithRepeatAndUniqueWithNumbersTest(self):
        uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.assertEqual(['2 d'], uniq._switchCaseFilter({'D': 1, 'd': 2}, count=True, repeat=True))


if __name__ == '__main__':
    unittest.main()
