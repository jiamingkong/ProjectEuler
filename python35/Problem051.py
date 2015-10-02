# someone else's code, this question is a poorly-worded puzzle.

import time
import sys
start = time.time()

sieve = []


def gen_primes(n):
    """ Returns  a list of primes < n """
    global sieve
    sieve = [1] * (n >> 1)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i >> 1]:
            sieve[i * i >> 1::i] = [0] * int(((n - i * i - 1) / (i << 1) + 1))
    return [2] + [(i << 1) + 1 for i in range(1, n >> 1) if sieve[i]]


def is_prime(n):
    global sieve
    return n == 2 or sieve[n >> 1]

limit = 1000000
primes = gen_primes(limit)

for i in primes:
    s = str(i)
    for j in '012':
        if j in s and s.count(j) in (3, 6, 9):
            counter = 1
            for k in range(int(j) + 1, 10):
                if is_prime(int(s.replace(j, str(k)))):
                    counter += 1
                    if counter == 8:
                        print(i)
                        print(time.time() - start)
                        sys.exit(0)
