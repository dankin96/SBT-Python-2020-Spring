import argparse

FILE_INPUT_NAME = 'src/input_3.txt'
FILE_OUTPUT_NAME = 'src/output_3_my.txt'


class Uniq(object):
    strings_dict = {}
    input_file = ""
    output_file = ""

    def __init__(self, input_file, output_file):
        self.strings_dict = {}
        self.input_file = input_file
        self.output_file = output_file

    @staticmethod
    def configure_argparser():
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--count", action='store_true',
                            help="print the number of repetitions at "
                                 "the beginning of each line")
        parser.add_argument("-d", "--repeat", action='store_true',
                            help="print only repeated lines")
        parser.add_argument("-i", "--ignore_case", action='store_true',
                            help="ignore case during comparing")
        parser.add_argument("-u", "--unique", action='store_true',
                            help="print only non-repeating lines")
        return parser.parse_args()

    def read(self, ignore_case, filename):
        file = open(filename)
        for line in file.readlines():
            string = line.strip()

            if ignore_case:
                string = string.lower()

            if string not in self.strings_dict:
                self.strings_dict[string] = 0

            self.strings_dict[string] = self.strings_dict.get(string) + 1
            file.close()

    def repeat(self):
        for string in list(self.strings_dict):
            if self.strings_dict[string] == 1:
                del self.strings_dict[string]

    def unique(self):
        for string in list(self.strings_dict):
            if self.strings_dict[string] != 1:
                del self.strings_dict[string]

    def write(self, count, filename):
        file = open(filename, 'w')
        if count:
            for string in self.strings_dict:
                file.write(str(self.strings_dict[string]) +
                           " " + string + '\n')
        else:
            for string in self.strings_dict:
                file.write(string + '\n')
        file.close()

    def main(self):
        ignore_case = False
        count = False
        args = Uniq.configure_argparser()
        if args.ignore_case:
            ignore_case = True
        if args.count:
            count = True
        self.read(ignore_case, self.input_file)
        if args.repeat:
            self.repeat()
        if args.unique:
            self.unique()
        self.write(count, self.output_file)


if __name__ == "__main__":
    uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
    uniq.main()
