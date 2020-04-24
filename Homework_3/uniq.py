import argparse
from collections import OrderedDict

FILE_INPUT_NAME = 'src/input.txt'
FILE_OUTPUT_NAME = 'src/output.txt'


class Uniq:
    def __init__(self, input_path, output_path, args):
        self.input_path = input_path
        self.output_path = output_path
        self._args = args

    def _read_lines(self):
        try:
            with open(self.input_path, "r") as f:
                return [line.rstrip() for line in f.readlines()]
        except Exception as e:
            print("Failed to read input cause:")
            print(e)

    def _write_output(self, lines):
        try:
            with open(self.output_path, "w") as f:
                f.write("\n".join(lines))
        except Exception as e:
            print("Failed to write output cause:")
            print(e)

    def _check_contradictory_arguments(self, lines):
        return [] if self._args.repeat and self._args.unique else lines

    def _to_lowercase(self, lines):
        return [line.lower() for line in lines] \
            if self._args.ignore_case else lines

    @staticmethod
    def _process_lines(lines):
        line_dict = OrderedDict()

        for line in lines:
            line_dict.setdefault(line, 0)
            line_dict[line] += 1

        return line_dict

    def _get_output_lines(self, line_dict):
        def default_filter(line):
            return True

        def default_mapper(line):
            return line[0]

        mapper = default_mapper
        _filter = default_filter

        if self._args.count:
            def with_count_mapper(value):
                return "{} {}".format(value[1], value[0])

            mapper = with_count_mapper

        elif self._args.repeat:
            def repeated_filter(value):
                return value[1] > 1

            _filter = repeated_filter

        elif self._args.unique:
            def unique_filter(value):
                return value[1] == 1

            _filter = unique_filter

        return self._build_output(line_dict, _filter, mapper)

    @staticmethod
    def _build_output(line_dict, _filter, mapper):
        filtered = list(filter(_filter, line_dict.items()))
        return list(map(mapper, filtered))

    def run(self):
        lines = self._read_lines()
        lines = self._check_contradictory_arguments(lines)
        lines = self._to_lowercase(lines)

        line_dict = self._process_lines(lines)
        output_lines = self._get_output_lines(line_dict)
        self._write_output(output_lines)


class UniqArgumentParser:
    @classmethod
    def parse_args(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--count", action="store_true",
                            help="print counts for each line")
        parser.add_argument("-d", "--repeat", action="store_true",
                            help="write only repeated lines")
        parser.add_argument("-i", "--ignore-case", action="store_true",
                            help="ignore case when comparing")
        parser.add_argument("-u", "--unique", action="store_true",
                            help="write only unique lines")
        return parser.parse_args()


if __name__ == "__main__":
    Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME, UniqArgumentParser.parse_args()) \
        .run()
