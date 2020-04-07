import argparse

FILE_INPUT_NAME = 'src/input_1.txt'
FILE_OUTPUT_NAME = 'src/output_1.txt'


class Uniq(object):
    list_of_word = []
    dict_of_word = {}

    def __init__(self, input_path='src/input.txt', output_path='src/output.txt'):
        self.input_path = input_path
        self.output_path = output_path

    def _getLine(self):
        words = []
        try:
            with open(self.input_path, "r") as input_file:
                words = input_file.read().split('\n')
        except Exception as e:
            print("getLine --- ошибка получения строки из файла")
            print(e)
        return words

    def _countOfWords(self, list_of_word, i=False):
        dict_of_word = {}
        for w in list_of_word:
            if i:
                dict_of_word[w.lower()] = dict_of_word.get(w.lower(), 0) + 1
            else:
                dict_of_word[w] = dict_of_word.get(w, 0) + 1
        return dict_of_word

    def _switchCaseFilter(self, dictionary, repeat=False, unique=False, count=False):
        list_of_word = []
        if repeat and unique:
            return []
        for i in dictionary:
            s = ''
            if repeat:
                if dictionary[i] < 2:
                    continue
            if unique:
                if dictionary[i] > 1:
                    continue
            if count:
                s += str(dictionary[i]) + ' '
            s += str(i)
            list_of_word.append(s)
        return list_of_word

    def _wordPrinter(self, list_of_word):
        try:
            with open(self.output_path, "w+") as output_file:
                for s in list_of_word[:-1]:
                    output_file.write(s + '\n')
                output_file.write(list_of_word.pop())
        except Exception as e:
            print("wordPrinter --- ошибка печати слов. Проверь FILE_INPUT_NAME/FILE_OUTPUT_NAME")
            print(e)

    def go(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--count', help='число повторов в начале каждой строки', action="store_true")
        parser.add_argument('-d', '--repeat', help='только повторяющиеся строки', action="store_true")
        parser.add_argument('-i', '--ignore-case', help='игнорировать регистр при сравнении', action="store_true")
        parser.add_argument('-u', '--unique', help='только неповторяющиеся строки', action="store_true")
        args = parser.parse_args()
        list_of_word = self._getLine()
        dict_of_word = self._countOfWords(list_of_word, args.ignore_case)
        list_of_word = self._switchCaseFilter(dict_of_word, args.repeat, args.unique, args.count)
        self._wordPrinter(list_of_word)


if __name__ == "__main__":
    constants = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
    constants.go()
