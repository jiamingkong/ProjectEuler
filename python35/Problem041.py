from itertools import permutations
from Utilities.PrimeGenerator import is_prime

def generator(n):
    num_list = list(map(str, list(range(1, n + 1))))
    for i in permutations(num_list, n):
        yield int("".join(i))


def main():
    max_found = -1
    for n in range(3, 10):
        for j in generator(n):
            if is_prime(j) and j > max_found:
                max_found = j
    print("Finally..", max_found)


if __name__ == '__main__':
    main()