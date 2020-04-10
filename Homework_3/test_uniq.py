from uniq import Uniq
import pytest

def compare_answers(file1, file2):
    count1 = len(open(file1).readlines())
    count2 = len(open(file1).readlines())

    if count1 != count2:
        return False

    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    equality = True

    for lineF1 in f1:
        lineF2 = f2.readline()

        lineF1 = lineF1.strip(" \t\n")
        lineF2 = lineF2.strip(" \t\n")

        if lineF1 != lineF2:
            equality = False
    f1.close()
    f2.close()
    return equality


# content of test_class.py
class TestUniq:

    def test_work_1(self):
        FILE_INPUT_NAME = 'test/input_test_1.txt'
        FILE_OUTPUT_NAME = 'test/output_test_1.txt'
        FILE_ANSWER_NAME = 'test/answer_test_1.txt'
        params = ["-c"]
        uniq = Uniq()
        uniq.uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME, params)
        assert (True == compare_answers(FILE_OUTPUT_NAME, FILE_ANSWER_NAME))

    def test_work_2(self):
        FILE_INPUT_NAME = 'test/input_test_2.txt'
        FILE_OUTPUT_NAME = 'test/output_test_2.txt'
        FILE_ANSWER_NAME = 'test/answer_test_2.txt'
        params = ["-d"]
        uniq = Uniq()
        uniq.uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME, params)
        assert (True == compare_answers(FILE_OUTPUT_NAME, FILE_ANSWER_NAME))

    def test_work_3(self):
        FILE_INPUT_NAME = 'test/input_test_3.txt'
        FILE_OUTPUT_NAME = 'test/output_test_3.txt'
        FILE_ANSWER_NAME = 'test/answer_test_3.txt'
        params = [""]
        uniq = Uniq()
        uniq.uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME, params)
        assert (True == compare_answers(FILE_OUTPUT_NAME, FILE_ANSWER_NAME))

    def test_work_4(self):
        FILE_INPUT_NAME = 'test/input_test_4.txt'
        FILE_OUTPUT_NAME = 'test/output_test_4.txt'
        FILE_ANSWER_NAME = 'test/answer_test_4.txt'
        params = ["-u", "-d"]
        uniq = Uniq()
        uniq.uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME, params)
        assert (True == compare_answers(FILE_OUTPUT_NAME, FILE_ANSWER_NAME))

    def test_work_5(self):
        FILE_INPUT_NAME = 'test/input_test_5.txt'
        FILE_OUTPUT_NAME = 'test/output_test_5.txt'
        FILE_ANSWER_NAME = 'test/answer_test_5.txt'
        params = ["-i", "-c"]
        uniq = Uniq()
        uniq.uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME, params)
        assert (True == compare_answers(FILE_OUTPUT_NAME, FILE_ANSWER_NAME))

    def test_work_6(self):
        FILE_INPUT_NAME = 'test/input_test_6.txt'
        FILE_OUTPUT_NAME = 'test/output_test_6.txt'
        FILE_ANSWER_NAME = 'test/answer_test_6.txt'
        params = ["-i", "-c", "-u"]
        uniq = Uniq()
        uniq.uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME, params)
        assert (True == compare_answers(FILE_OUTPUT_NAME, FILE_ANSWER_NAME))
