from unittest.mock import patch
from uniq import Uniq
import os


def test_empty_output_on_empty_input():
    run_test(inp('empty'), outp('empty'))


def test_empty_output_on_controversial_args():
    run_test(inp('simple'), outp('empty'), ['-d', '-u'])


def test_no_duplicates():
    run_test(inp('simple'), outp('simple'))


def test_with_count():
    run_test(inp('simple'), outp('simple_with_count'), ['-c'])


def test_lowercase():
    run_test(inp('lowercase'), outp('lowercase'), ['-i'])


def test_repeat():
    run_test(inp('simple'), outp('repeat'), ['-d'])


def test_empty_output_with_repeat_true_and_no_repeated_in_input():
    run_test(inp("no_repeated"), outp('empty'), ['-d'])


def test_unique():
    run_test(inp('simple'), outp('unique'), ['-u'])


def test_empty_output_with_unique_true_and_no_unique_in_input():
    run_test(inp("no_unique"), outp('empty'), ['-u'])


def run_test(input_path, output_path, args=None):
    tmp_dir = "./tmp.txt"
    args = [''] + args if args is not None else ['']

    try:
        with patch('sys.argv', args):
            Uniq(input_path, tmp_dir).run()

        with open(output_path, 'r') as f:
            expected = [line.rstrip() for line in f.readlines()]
        with open(tmp_dir, 'r') as f:
            actual = [line.rstrip() for line in f.readlines()]

        assert actual == expected

    finally:
        if os.path.exists(tmp_dir):
            os.remove(tmp_dir)


def resource(string):
    return 'src/{}.txt'.format(string)


def inp(string):
    return resource('{}_input'.format(string))


def outp(string):
    return resource('{}_output'.format(string))
