from math import log10
import csv


def pair_represent(base, power):
    '''
    log_e (x&y) = y * log_e (x), or use log_10 for smaller number just for more fun.
    instead of preserving the millions of digits that will fuck up any memory, I am preserving a float for every pair.
    '''
    return power * log10(base)


def main():
    number_repr = []
    with open('p099_base_exp.txt', "r") as f:
        reader = csv.reader(f)
        for a, b in reader:
            number_repr.append(pair_represent(int(a), int(b)))

    max_index = number_repr.index(max(number_repr)) + 1
    return max_index

if __name__ == '__main__':
    print(main())
