import argparse
from collections import Counter

FILE_INPUT_NAME = 'src/input_1.txt'
FILE_OUTPUT_NAME = 'src/output_1.txt'


class Uniq(object):

    def __init__(self, input_file_name='src/input.txt', output_file_name='src/output.txt'):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--count", action="store_true")
        parser.add_argument("-d", "--repeat", action="store_true")
        parser.add_argument("-i", "--ignore_case", action="store_true")
        parser.add_argument("-u", "--unique", action="store_true")
        args = parser.parse_args()
        Uniq.unical(FILE_INPUT_NAME, args)


    def reader(self):
        with open(self) as f:
            perem = f.read().split()
        f.close()
        return perem

    def unical(self, args):
        data = Uniq.reader(self)
        outputData = []
        if args.count == args.repeat == args.ignore_case == args.unique == False:
            for i in range(len(data)):
                if data[i] in outputData:
                    continue
                else:
                    outputData.append(data[i])
        elif (args.count == 1) and (args.repeat == args.ignore_case == args.unique == 0):
            c = Counter(data)
            for i in range(len(list(c.keys()))):
                outputData.append(str(list(c.values())[i]) + ' ' + str(list(c.keys())[i]))
        elif (args.repeat == 1) and (args.count == args.ignore_case == args.unique == 0):
            c = Counter(data)
            for i in range(len(list(c.keys()))):
                if list(c.values())[i] > 1:
                    outputData.append(list(c.keys())[i])
        elif (args.ignore_case == 1) and (args.count == args.repeat == args.unique == 0):
            lower_case_data = [data[i].lower() for i in range(len(data))]
            for i in range(len(lower_case_data)):
                if lower_case_data[i] in outputData:
                    continue
                else:
                    outputData.append(lower_case_data[i])
        elif (args.count == args.repeat == args.ignore_case == 0) and (args.unique == 1):
            c = Counter(data)
            for i in range(len(list(c.keys()))):
                if list(c.values())[i] == 1:
                    outputData.append(list(c.keys())[i])
        elif (args.count == args.repeat == 1) and (args.ignore_case == args.unique == 0):
            c = Counter(data)
            for i in range(len(list(c.keys()))):
                if list(c.values())[i] > 1:
                    outputData.append(str(list(c.values())[i]) + ' ' + str(list(c.keys())[i]))
        elif (args.repeat == args.ignore_case == 1) and (args.count == args.unique == 0):
            lower_case_data = [data[i].lower() for i in range(len(data))]
            c = Counter(lower_case_data)
            for i in range(len(list(c.keys()))):
                if list(c.values())[i] > 1:
                    outputData.append(list(c.keys())[i])
        elif (args.count == args.repeat == 0) and (args.ignore_case == args.unique == 1):
            lower_case_data = [data[i].lower() for i in range(len(data))]
            c = Counter(lower_case_data)
            for i in range(len(list(c.keys()))):
                if list(c.values())[i] == 1:
                    outputData.append(list(c.keys())[i])
        elif (args.count == args.ignore_case == 1) and (args.repeat == args.unique == 0):
            lower_case_data = [data[i].lower() for i in range(len(data))]
            c = Counter(lower_case_data)
            for i in range(len(list(c.keys()))):
                outputData.append(str(list(c.values())[i]) + ' ' + str(list(c.keys())[i]))
        elif (args.count == args.repeat == args.ignore_case == 1) and (args.unique == 0):
            lower_case_data = [data[i].lower() for i in range(len(data))]
            c = Counter(lower_case_data)
            for i in range(len(list(c.keys()))):
                if list(c.values())[i] > 1:
                    outputData.append(str(list(c.values())[i]) + ' ' + str(list(c.keys())[i]))
        elif (args.count == args.ignore_case == args.unique == 1) and (args.repeat == 0):
            lower_case_data = [data[i].lower() for i in range(len(data))]
            c = Counter(lower_case_data)
            for i in range(len(list(c.keys()))):
                if list(c.values())[i] == 1:
                    outputData.append(str(list(c.values())[i]) + ' ' + str(list(c.keys())[i]))
        Uniq.writer(self, outputData)


    def writer(self, outputData):
        with open(FILE_OUTPUT_NAME, 'w') as f:
            for index in outputData:
                f.write(index + '\n')
        f.close()


if __name__ == "__main__":
    a = Uniq()
    a.run()


