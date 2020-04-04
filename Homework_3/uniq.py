FILE_INPUT_NAME = 'src/input_1.txt'
FILE_OUTPUT_NAME = 'src/output_11.txt'

import argparse


class Uniq(object):
	word_list = []
	word_dict = {}

	def __init__(self, input_path='src/input.txt', output_path='src/output.txt'):
		self.input_path = input_path
		self.output_path = output_path

	def _countWords(self, word_list, i=False):
		word_dict = {}
		for word in word_list:
			if i:
				word_dict[word.lower()] = word_dict.get(word.lower(), 0) + 1
			else:
				word_dict[word] = word_dict.get(word, 0) + 1

		return word_dict

	def _filter(self, dict, count=False, repeat=False, unique=False):
		final = []
		if unique and repeat:
			return []
		for i in dict:
			s = ''
			if repeat:
				if dict[i] < 2:
					continue
			if unique:
				if dict[i] > 1:
					continue
			if count:
				s += str(dict[i]) + ' '
			s += str(i)
			final.append(s)
		return final

	def _getlines(self):
		words=[]
		try:
			with open(self.input_path, "r") as input_file:
				words = input_file.read().split('\n')
		except Exception as e:
			print("something went wrong")
			print(e)
		return words

	def _printWords(self, final):
		try:
			with open(self.output_path, "w+") as output_file:
				for s in final[:-1]:
					output_file.write(s+'\n')
				output_file.write(final.pop())
		except Exception as e:
			print("something went wrong")
			print(e)

	def run(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('-c', '--count', help='count words', action="store_true", default=False)
		parser.add_argument('-i', '--ignore-case', help='ignore letter case', action="store_true", default=False)
		parser.add_argument('-d', '--repeat', help='show repeat strings', action="store_true", default=False)
		parser.add_argument('-u', '--unique', help='show unique strings', action="store_true", default=False)
		args = parser.parse_args()
		word_list = self._getlines()
		word_dict = self._countWords(word_list, args.ignore_case)
		word_list = self._filter(word_dict, args.count, args.repeat, args.unique)
		self._printWords(word_list)


if __name__ == "__main__":
	uniq = Uniq(FILE_INPUT_NAME, FILE_OUTPUT_NAME)
	uniq.run()
