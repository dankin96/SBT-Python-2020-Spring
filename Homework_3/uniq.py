import argparse

FILE_INPUT_NAME = 'src/input.txt'
FILE_OUTPUT_NAME = 'src/output.txt'


class Uniq(object):
    strings = []
    count_strings = {}
    input_file = ""
    output_file = ""

    def __init__(self, input_file, output_file):
        self.strings = []
        self.count_strings = {}
        self.input_file = input_file
        self.output_file = output_file

    def _dictionary_filling(self, ignore_case):
        for string in self.strings:
            if ignore_case:
                string_lower = string.lower()
                if string_lower not in self.count_strings:
                    self.count_strings[string_lower] = (string, 0)
                self.count_strings[string_lower] = (
                    self.count_strings.get(string_lower)[0],
                    self.count_strings.get(string_lower)[1] + 1)
            else:
                if string not in self.count_strings:
                    self.count_strings[string] = (string, 0)
                self.count_strings[string] =\
                    (self.count_strings.get(string)[0],
                     self.count_strings.get(string)[1] + 1)
        return

    def _repeat(self):
        for string_pair in list(self.count_strings):
            if self.count_strings[string_pair][1] == 1:
                del self.count_strings[string_pair]
        return

    def _unique(self):
        for string_pair in list(self.count_strings):
            if self.count_strings[string_pair][1] != 1:
                del self.count_strings[string_pair]
        return

    def _read(self, filename):
        file = open(filename)
        for line in file.readlines():
            line = line.strip()
            self.strings.append(line)

    def main(self):
        self._read(self.input_file)
        ignore_case = False
        count = False
        args = self._configire_argparser()
        if args.ignore_case:
            ignore_case = True
        self._dictionary_filling(ignore_case)
        if args.repeat:
            self._repeat()
        if args.unique:
            self._unique()
        if args.count:
            count = True
        self._write(count, self.output_file)

    def _write(self, count, filename):
        file = open(filename, 'w')
        if count:
            for key in self.count_strings:
                file.write(str(self.count_strings[key][1]) + " " +
                           str(self.count_strings[key][0]) + '\n')
        else:
            for key in self.count_strings:
                file.write(str(self.count_strings[key][0]) + '\n')

    @staticmethod
    def configire_argparser():
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--count", action='store_true',
                            help="print the number of repetitions "
                                 "at the beginning of each line")
        parser.add_argument("-d", "--repeat", action='store_true',
                            help="print only repeated lines")
        parser.add_argument("-i", "--ignore_case", action='store_true',
                            help="ignore case when comparing")
        parser.add_argument("-u", "--unique", action='store_true',
                            help="print only non-repeating lines")
        return parser.parse_args()


if __name__ == "__main__":
    uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
    uniq.main()
