import unittest

from Homework_3.uniq import Uniq

FILE_INPUT_NAME = 'src/input_test.txt'
FILE_OUTPUT_NAME = 'src/output_test.txt'


class UniqTest(unittest.TestCase):

    def test_ignore_case_only(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = []
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(False, False, False, True)
        self.assertEqual(test_result, test_output_list)

    def test_count_only(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = ['3 ab', '1 A', '1 BBB', '1 bbb', '1 a', '2 abc', '1 c']
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(False, True, False, False)
        self.assertEqual(test_result, test_output_list)

    def test_count_ignore_case(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = ['3 ab', '2 a', '2 bbb', '2 abc', '1 c']
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(False, True, False, True)
        self.assertEqual(test_result, test_output_list)

    def test_count_unique(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = ['1 A', '1 BBB', '1 bbb', '1 a', '1 c']
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(True, True, False, False)
        self.assertEqual(test_result, test_output_list)

    def test_count_unique_ignore_case(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = ['1 c']
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(True, True, False, True)
        self.assertEqual(test_result, test_output_list)

    def test_count_repeat(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = ['3 ab', '2 abc']
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(False, True, True, False)
        self.assertEqual(test_result, test_output_list)

    def test_count_repeat_ignore_case(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = ['3 ab', '2 a', '2 bbb', '2 abc']
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(False, True, True, True)
        self.assertEqual(test_result, test_output_list)

    def test_repeat_only(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = ['ab', 'abc']
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(False, False, True, False)
        self.assertEqual(test_result, test_output_list)

    def test_repeat_ignore_case(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = ['ab', 'a', 'bbb', 'abc']
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(False, False, True, True)
        self.assertEqual(test_result, test_output_list)

    def test_unique_only(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = ['A', 'BBB', 'bbb', 'a', 'c']
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(True, False, False, False)
        self.assertEqual(test_result, test_output_list)

    def test_unique_ignore_case(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = ['c']
        # unique, count, repeat, ignore_case
        test_output_list = a._unique_handle(True, False, False, True)
        self.assertEqual(test_result, test_output_list)

    def test_unique_repeat_all_cases(self):
        a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
        test_result = []
        # count, unique, repeat, ignore_case
        test_output_list = a._args_handle(False, True, True, False)
        self.assertEqual(test_result, test_output_list)
        test_output_list = a._args_handle(True, True, True, False)
        self.assertEqual(test_result, test_output_list)
        test_output_list = a._args_handle(False, True, True, True)
        self.assertEqual(test_result, test_output_list)
        test_output_list = a._args_handle(True, True, True, True)
        self.assertEqual(test_result, test_output_list)
