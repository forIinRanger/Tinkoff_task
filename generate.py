import argparse as ap
import pickle
from train import Model1

parser = ap.ArgumentParser()
parser.add_argument('--model', type=str, help='path to file')
parser.add_argument('--prefix', type=str, default=False)
parser.add_argument('--length', type=int)
args = parser.parse_args()

file_to_save_model = args.model


with open(f'{file_to_save_model}', 'rb') as f:
    model = pickle.load(f)

print(model.generate(args.prefix, args.length))
