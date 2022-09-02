import argparse as ap
import sys
import os.path
import re
import numpy as np
import pickle

# cd C:\Users\Пользователь\PycharmProjects\Tinkoff
# считываем передаваемые аргументы из командной строки и переносим их в нашу программу
parser = ap.ArgumentParser()
parser.add_argument('--input_dir', type=str, default='stdin', help='path of texts')
parser.add_argument('--model', type=str, help='path to file')
args = parser.parse_args()

file_to_save_model = args.model

# add texts to list from docs
texts = []
if args.input_dir != 'stdin':
    for name in os.listdir(f'{args.input_dir}'):
        with open(fr'{args.input_dir}\{name}', 'r', encoding='UTF-8') as f:
            texts.append(f.read())
else:
    texts = [i for i in sys.stdin.readlines()]

sorte = []
for i in texts:
    sorte += [x.lower() for x in re.findall(r'[а-яА-ЯёЁ]+', i)]


class Model:
    def __init__(self):
        self.vocabulary = {}
        self.res = []

    def fit(self, words):
        for i in range(len(words) - 1):
            try:
                self.vocabulary[words[i]].append(words[i + 1])
            except KeyError:
                self.vocabulary[words[i]] = [words[i + 1]]

    def generate(self, prefix, length: int):
        if not prefix:
            prefix = np.random.choice([i for i in self.vocabulary.keys()])
        self.res.append(prefix)
        for i in range(length - 1):
            try:
                next_word = np.random.choice([i for i in self.vocabulary[prefix]])
            except KeyError:
                next_word = np.random.choice([i for i in self.vocabulary.keys()])
            prefix = next_word
            self.res.append(next_word)
        return ' '.join(self.res)


model = Model()
model.fit(sorte)
print(model.vocabulary)
with open(f'{file_to_save_model}', 'wb') as f:
    pickle.dump(model, f)


