from argparse import Namespace
from copy import copy
from uniq import Uniq
import os

default_args = Namespace(
    count=False,
    repeat=False,
    ignore_case=False,
    unique=False
)


def test_empty_output_on_empty_input():
    run_test(inp('empty'), outp('empty'), default_args)


def test_empty_output_on_controversial_args():
    args = copy(default_args)
    args.repeat = True
    args.unique = True
    run_test(inp('simple'), outp('empty'), args)


def test_no_duplicates():
    run_test(inp('simple'), outp('simple'), default_args)


def test_with_count():
    args = copy(default_args)
    args.count = True
    run_test(inp('simple'), outp('simple_with_count'), args)


def test_lowercase():
    args = copy(default_args)
    args.ignore_case = True
    run_test(inp('lowercase'), outp('lowercase'), args)


def test_repeat():
    args = copy(default_args)
    args.repeat = True
    run_test(inp('simple'), outp('repeat'), args)


def test_empty_output_with_repeat_true_and_no_repeated_in_input():
    args = copy(default_args)
    args.repeat = True
    run_test(inp("no_repeated"), outp('empty'), args)


def test_unique():
    args = copy(default_args)
    args.unique = True
    run_test(inp('simple'), outp('unique'), args)


def test_empty_output_with_unique_true_and_no_unique_in_input():
    args = copy(default_args)
    args.unique = True
    run_test(inp("no_unique"), outp('empty'), args)


def run_test(input_path, output_path, args):
    tmp_dir = "./tmp.txt"

    try:
        Uniq(input_path, tmp_dir, args).run()

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
