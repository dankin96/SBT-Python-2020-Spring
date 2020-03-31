import unittest

from uniq import Uniq

FILE_INPUT_NAME = 'src/input.txt'
FILE_OUTPUT_NAME = 'src/output.txt'


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        self.uniq.strings = "a" \
                            "a" \
                            "A" \
                            "b" \
                            "B" \
                            "c"

    def test_dictionary_filling_not_ignore_case(self):
        self.uniq._dictionary_filling(False)
        self.assertEqual(('a', 2), self.uniq.count_strings["a"])

    def test_dictionary_filling_ignore_case(self):
        self.uniq._dictionary_filling(True)
        self.assertEqual(('a', 3), self.uniq.count_strings["a"])

    def test_repeat_not_ignore_case(self):
        self.uniq._dictionary_filling(False)
        self.uniq._repeat()
        self.assertEqual({'a': ('a', 2)}, self.uniq.count_strings)

    def test_repeat_ignore_case(self):
        self.uniq._dictionary_filling(True)
        self.uniq._repeat()
        self.assertEqual({'a': ('a', 3), 'b': ('b', 2)}, self.uniq.count_strings)

    def test_unique_not_ignore_case(self):
        self.uniq._dictionary_filling(False)
        self.uniq._unique()
        self.assertEqual({'A': ('A', 1), 'B': ('B', 1), 'b': ('b', 1), 'c': ('c', 1)}, self.uniq.count_strings)

    def test_unique_ignore_case(self):
        self.uniq._dictionary_filling(True)
        self.uniq._unique()
        self.assertEqual({'c': ('c', 1)}, self.uniq.count_strings)

    def test_argparser(self):
        parsed = self.uniq.configire_argparser()
        self.assertEqual(False, parsed.__contains__("--count"), )

    def test_output_count(self):
        strings = []
        self.uniq._dictionary_filling(True)
        self.uniq._write(True, FILE_OUTPUT_NAME)
        file = open(FILE_OUTPUT_NAME)
        for line in file.readlines():
            line = line.strip()
            strings.append(line)
        self.assertEqual('3 a', strings[0])


if __name__ == '__main__':
    unittest.main()
