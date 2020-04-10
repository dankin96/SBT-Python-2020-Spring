#!/usr/bin/env python
# coding: utf-8

import sys
import re

FILE_INPUT_NAME = 'src/input.txt'
FILE_OUTPUT_NAME = 'src/output.txt'


class Uniq(object):
    def __init__(self):
        return

    def word_count(self, file, i):
        words = dict()
        f = open(file, 'r')
        for lineS in f:
            lineS = lineS.strip(" \t\n")
            if i is None:
                line = lineS
            else:
                line = lineS.lower()
            if words.get(line) is None:
                words[line] = 1
            else:
                words[line] += 1
        f.close()
        return words

    def print_in_file(self, f, c, num, word, last):
        enter = ""
        if not last:
            enter = "\n"

        out = ""
        if c:
            out = str(num) + " " + word
            f.write(str(num) + " " + word + enter)
        else:
            out = word
            f.write(word + enter)
        return out

    def print_word(self, file, words, c, d, u):
        f = open(file, 'w')
        out_text = ""
        i = 0
        last = False
        if u is not None and d is not None:
            f.close()
            return
        for word in words:
            i += 1
            if i == len(words):
                last = True
            num = words[word]
            if (d and num > 1) or (u and num == 1) or (u is None and d is None):
                out_text = out_text + self.print_in_file(f, c, num, word, last) + "\n"
                continue
        f.close()
        return out_text

    def recognize_params(self, parameters):
        c = None
        d = None
        i = None
        u = None
        error = None
        for parameter in parameters:
            if parameter == "-c":
                c = True
                continue
            if parameter == "-d":
                d = True
                continue
            if parameter == "-i":
                i = True
                continue
            if parameter == "-u":
                u = True
                continue
            print(parameter)
            error = True
        return c, d, i, u, error

    def uniq(self, input_file, output_file, parameters):
        c, d, i, u, error = self.recognize_params(parameters)
        if error:
            print("Error arguments")
            return ""
        words = self.word_count(input_file, i)
        out = self.print_word(output_file, words, c, d, u)
        return out


if __name__ == "__main__":
    params = []
    param_name = False
    for param in sys.argv:
        if param_name is False and param == "uniq.py":
            param_name = True
            continue
        params.append(param)
    uniq = Uniq()
    uniq.uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME, params)
