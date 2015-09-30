from Utilities.PrimeGenerator import PrimeGenerator, is_prime
from itertools import permutations


def find_permute(number):
    for i in permutations(list(str(number))):
        _n = int(''.join(i))
        if _n > 1000:
            yield _n


def collector(gen):
    return sorted(list(gen))


def main():
    for i in PrimeGenerator(under=9999):
        if i < 1488:
            continue
        else:
            counter = 0
            candidate = collector(find_permute(i))
            for j in candidate:
                if j != i and is_prime(j) and is_prime(2 * j-i) and (2 * j - i) in candidate:
                    return i, j, 2 * j - i


if __name__ == '__main__':
    print(main())
