import argparse as ap
import pickle
import numpy as np
import re


class Model:
    def __init__(self):
        self.vocabulary = {}
        self.res = []

    def fit(self, words):
        for i in range(len(words) - 1):
            try:
                self.vocabulary[re.search(r'[а-яА-ЯёЁ]+', words[i])[0]].append(words[i + 1])
            except KeyError:
                self.vocabulary[re.search(r'[а-яА-ЯёЁ]+', words[i])[0]] = [words[i + 1]]

    def generate(self, prefix, length: int):
        if not prefix:
            prefix = np.random.choice([i for i in self.vocabulary.keys()])
        self.res.append(prefix.capitalize())
        for i in range(length - 1):
            try:
                next_word = np.random.choice([i for i in self.vocabulary[prefix]])
            except KeyError:
                next_word = np.random.choice([i for i in self.vocabulary.keys()])
            prefix = re.search(r'[а-яА-ЯёЁ]+', next_word)[0]
            self.res.append(next_word)
        for i in range(len(self.res)):
            if '.' in self.res[i - 1]:
                self.res[i] = self.res[i].capitalize()
        self.res[-1] = re.search(r'[а-яА-ЯёЁ]+', self.res[-1])[0]
        return ' '.join(self.res)+'.'


parser = ap.ArgumentParser()
parser.add_argument('--model', type=str, help='path to file')
parser.add_argument('--prefix', type=str, default=False)
parser.add_argument('--length', type=int)
args = parser.parse_args()

file_to_save_model = args.model

with open(f'{file_to_save_model}', 'rb') as f:
    model = pickle.load(f)

print(model.generate(args.prefix, args.length))
