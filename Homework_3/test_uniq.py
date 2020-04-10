import pytest

from Homework_3.uniq import Uniq

FILE_INPUT_NAME = 'src/input.txt'
FILE_OUTPUT_NAME = 'src/output.txt'


def test_result_no_args():
    assert Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME).do_uniq() == "AB\nab\na\nA\nabc\nA3\na3\n1"


# def test_content():
#     self.fail()
#
#
# def test_attributes():
#     self.fail()
#
#
# def test_attributes():
#     self.fail()
#
#
# def test_do_uniq():
#     self.fail()
