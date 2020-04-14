import unittest

from Homework_3.uniq import Uniq

FILE_INPUT_NAME = 'src/input_3.txt'
FILE_OUTPUT_NAME = 'src/output_3_my.txt'


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)

    def test_repeat_not_ignore_case(self):
        self.uniq.read(False, self.uniq.input_file)
        self.uniq.repeat()
        self.assertEqual({'ab': 3, 'abc': 2}, self.uniq.strings_dict)

    def test_repeat_ignore_case(self):
        self.uniq.read(True, self.uniq.input_file)
        self.uniq.repeat()
        self.assertEqual({'ab': 4, 'a': 2, 'abc': 2, 'a3': 2},
                         self.uniq.strings_dict)

    def test_unique_not_ignore_case(self):
        self.uniq.read(False, self.uniq.input_file)
        self.uniq.unique()
        self.assertEqual({'AB': 1, 'a': 1, 'A': 1, 'A3': 1, 'a3': 1, '1': 1},
                         self.uniq.strings_dict)

    def test_unique_ignore_case(self):
        self.uniq.read(True, self.uniq.input_file)
        self.uniq.unique()
        self.assertEqual({'1': 1}, self.uniq.strings_dict)

    def test_output_file_count_ignore_case(self):
        strings = []
        self.uniq.read(True, self.uniq.input_file)
        self.uniq.write(True, FILE_OUTPUT_NAME)
        file = open(FILE_OUTPUT_NAME)
        for line in file.readlines():
            line = line.strip()
            strings.append(line)
        self.assertEqual('4 ab', strings[0])
        file.close()


if __name__ == '__main__':
    unittest.main()
