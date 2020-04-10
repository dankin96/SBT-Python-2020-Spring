from unittest import mock

from Homework_3.uniq import Uniq

FILE_INPUT_NAME = 'src/input.txt'
FILE_OUTPUT_NAME = 'src/output.txt'


def test_result_no_args():
    with mock.patch('sys.argv', ['']):
        assert Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME).do_uniq() == "ab\na\nabc\nAbc\n"


def test_result_count():
    my_args = ['', '-c']
    with mock.patch('sys.argv', my_args):
        assert Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME).do_uniq() == "3 ab\n1 a\n2 abc\n1 Abc\n"


def test_result_repeat():
    my_args = ['', '-d']
    with mock.patch('sys.argv', my_args):
        assert Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME).do_uniq() == "ab\nabc\n"


def test_result_ignore_case():
    my_args = ['', '-i']
    with mock.patch('sys.argv', my_args):
        assert Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME).do_uniq() == "ab\na\nabc\n"


def test_result_unique():
    my_args = ['', '-u']
    with mock.patch('sys.argv', my_args):
        assert Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME).do_uniq() == "a\nAbc\n"


def test_result_repeat_unique():
    my_args = ['', '-d', '-u']
    with mock.patch('sys.argv', my_args):
        assert Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME).do_uniq() == ""
