from Utilities.PrimeGenerator import is_prime
from math import sqrt


def verify(number):
    result = False
    for i in xrange(1, int(sqrt(number / 2))+1):
        if is_prime(number - i * i * 2):
            result = True
            break
    return result


def gen_odd_composite():
    n = 1
    while True:
        c = 2 * n + 1
        if not is_prime(c):
            yield c

        n += 1


def main():
    for i in gen_odd_composite():
        if not verify(i):
            print(i)
            break


if __name__ == '__main__':
    # print verify(25)
    main()
