import argparse
import collections

FILE_INPUT_NAME = 'src/input_1.txt'
FILE_OUTPUT_NAME = 'src/output_4.txt'


class Uniq(object):

    def __init__(self, input_file_name='src/input.txt', output_file_name='src/output.txt'):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    def execute(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--count", action="store_true")
        parser.add_argument("-d", "--repeat", action="store_true")
        parser.add_argument("-i", "--ignore-case", action="store_true")
        parser.add_argument("-u", "--unique", action="store_true")
        args = parser.parse_args()
        output_list = self._args_handle(args.count, args.unique, args.repeat, args.ignore_case)
        self._output_file_handle(output_list)

    def _output_file_handle(self, output_list):
        if output_list:
            output_file = open(self.output_file_name, 'w+')
            for i in range(len(output_list)):
                output_file.write(output_list[i])
                if i != len(output_list) - 1:
                    output_file.write('\n')
            output_file.close()

    def _args_handle(self, count=False, unique=False, repeat=False, ignore_case=False):
        if unique and repeat:
            return []
        return self._unique_handle(unique, count, repeat, ignore_case)

    def _counter_handle(self, ignore_case=False):
        input_file_counter = collections.Counter()
        try:
            input_file = open(self.input_file_name, 'r')
            for line in input_file:
                if ignore_case:
                    input_file_counter[line.strip('\n').lower()] += 1
                else:
                    input_file_counter[line.strip('\n')] += 1
            input_file.close()
        except Exception as exception:
            print(f"Error while reading file: {exception}")
        return input_file_counter

    def _unique_handle(self, unique, count, repeat, ignore_case):
        output_dict = self._counter_handle(ignore_case)
        output_list = []
        for key, val in output_dict.items():
            if count and not unique and not repeat:
                output_list.append(str(val) + " " + key)
            elif (unique and val == 1) or (repeat and (val != 1)):
                if count:
                    output_list.append(str(val) + " " + key)
                else:
                    output_list.append(key)
        return output_list


if __name__ == "__main__":
    a = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
    a.execute()
