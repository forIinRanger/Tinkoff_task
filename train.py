import argparse as ap
import sys
import os.path

# cd C:\Users\Пользователь\PycharmProjects\Tinkoff
# считываем передаваемые аргументы из командной строки и переносим их в нашу программу
parser = ap.ArgumentParser()
parser.add_argument('--input_dir', type=str, default='stdin')
parser.add_argument('--model', type=str)
args = parser.parse_args()

file_to_save_model = args.model
data = []
if args.input_dir != 'stdin':
    dir_with_texts = args.input_dir
    for name in os.listdir(f'{dir_with_texts}'):
        with open(fr'{dir_with_texts}\{name}', 'r') as f:
            data.append(f.read())
else:
    data = [i for i in sys.stdin.readlines()]
