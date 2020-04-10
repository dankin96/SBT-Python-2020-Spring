import argparse

FILE_INPUT_NAME = 'src/input_3.txt'
FILE_OUTPUT_NAME = 'src/output.txt'


class Uniq(object):

    def __init__(self, input_file, output_file, attributes):
        self.input_file = input_file
        self.output_file = output_file
        self._attributes = attributes
        self.content = input_file

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = dict()
        with open(value) as f:
            for line in f:
                line = line.replace("\n", "")
                if self.attributes.ignore_case:
                    if line.lower() in self.content:
                        self._content[line.lower()] += 1
                    else:
                        self._content[line.lower()] = 1
                else:
                    if line in self.content:
                        self._content[line] += 1
                    else:
                        self._content[line] = 1

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    def write_file(self, value):
        with open(self.output_file, 'w') as f:
            f.write(value)

    def do_uniq(self):
        print(self.content)
        res = ""
        if self.attributes.repeat and self.attributes.unique:
            self.write_file(res)
            return res
        if self.attributes.count:
            if self.attributes.repeat:
                for key in self.content:
                    if self.content[key] > 1:
                        res += str(self.content[key]) + " " + key + "\n"
            elif self.attributes.unique:
                for key in self.content:
                    if self.content[key] == 1:
                        res += str(self.content[key]) + " " + key + "\n"
            else:
                for key, value in self.content.items():
                    res += str(value) + " " + key + "\n"
        else:
            if self.attributes.repeat:
                for key in self.content:
                    if self.content[key] > 1:
                        res += key + "\n"
            elif self.attributes.unique:
                for key in self.content:
                    if self.content[key] == 1:
                        res += key + "\n"
            else:
                for key in self.content.keys():
                    res += key + "\n"
        self.write_file(res)
        return res


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("-c",
                           "--count",
                           help="выводить число повторов в начале строки",
                           action="store_true")
    my_parser.add_argument("-d",
                           "--repeat",
                           help="выводить только повторяющиеся строки",
                           action="store_true")
    my_parser.add_argument("-i",
                           "--ignore-case",
                           help="игнорировать регистр при сравнении",
                           action="store_true")
    my_parser.add_argument("-u",
                           "--unique",
                           help="выводить только неповторяющиеся строки",
                           action="store_true")
    args = my_parser.parse_args()
    result = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME, args).do_uniq()
    print("Result: ")
    print(result)
