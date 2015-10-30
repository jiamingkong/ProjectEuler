from Utilities.PrimeFactor import list_divisors
from Utilities.PrimeGenerator import is_prime, PrimeGenerator
from math import sqrt
import pdb

LIMIT = 1001

TAGGER = []
PRIMES = []


def tag_primes(limit):
    global TAGGER
    global PRIMES
    TAGGER = [False for x in range(limit + 1)]
    for i in range(2, int(sqrt(limit)) + 1):
        if not TAGGER[i]:
            j = i * i
            while j < limit + 1:
                TAGGER[j] = True
                j += i

    for i in range(2, limit + 1):
        if not TAGGER[i]:
            PRIMES.append(i)


def main():
    tag_primes(LIMIT)
    n = len(PRIMES)
    result = 0
    pdb.set_trace()
    for i in range(0, n):
        k = PRIMES[i] - 1
        f = False
        for j in range(1, int(sqrt(k))+1):
            if (k % j == 0 and PRIMES[int(j + (k / j))]):
                f = True
                break

        if not f:
            result += k

    return result

if __name__ == '__main__':
    print(main())