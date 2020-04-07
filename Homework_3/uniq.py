FILE_INPUT_NAME = 'src/input.txt'
FILE_OUTPUT_NAME = 'src/output.txt'


class Uniq(object):

    def __init__(self, input_file, output_file, attributes):
        self.input_file = input_file
        self.output_file = output_file
        self.take_attributes(attributes)

    @property
    def count(self):
        return self.count

    @count.setter
    def count(self, value):
        self.count = value

    @property
    def repeat(self):
        return self.repeat

    @repeat.setter
    def repeat(self, value):
        self.repeat = value

    @property
    def ignore_case(self):
        return self.ignore_case

    @ignore_case.setter
    def ignore_case(self, value):
        self.ignore_case = value

    @property
    def unique(self):
        return self.unique

    @unique.setter
    def unique(self, value):
        self.unique = value

    @property
    def input_file(self):
        return self.input_file

    @input_file.setter
    def input_file(self, value):
        self.input_file = value

    @property
    def output_file(self):
        return self.output_file

    @output_file.setter
    def output_file(self, value):
        self.output_file = value

    @property
    def content(self):
        return self.content

    @content.setter
    def content(self, value):
        with open(value) as f:
            self.content = f.readlines()

    @property
    def attributes(self):
        return self.attributes

    @attributes.setter
    def attributes(self):
        self.attributes = 0

    """def take_attribute(self, value):
        self.count = value.count
        self.repeat = value.repeat
        self.ignore_case = value.ignore_case
        self.unique = value.unique
    """

    def do_uniq_count(self):

    def do_uniq_repeat(self):

    def do_uniq_ignore_case(self):

    def do_uniq_unique(self):

    def do_uniq(self):
        for a in self.attributes:
            #self.take_attribute(a)
            if a.count:
                self.do_uniq_count()
            if a.repeat:
                self.do_uniq_repeat()
            if a.ignore_case:
                self.do_uniq_ignore_case()
            if a.unique:
                self.do_uniq_unique()

if __name__ == "__main__":
    # your code
