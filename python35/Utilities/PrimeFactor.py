from collections import Counter
from functools import reduce


def prime_factors(x):
    factors = []
    while x % 2 == 0:
        factors.append(2)
        x /= 2
    i = 3
    while i * i <= x:
        while x % i == 0:
            x /= i
            factors.append(i)
        i += 2
    if x > 1:
        factors.append(int(x))
    return factors


def num_of_divisors(x):
    primes = prime_factors(x)
    things = Counter(primes)
    result = 1
    for i in list(things.values()):
        result *= (i + 1)
    return result


def list_divisors(num):
    if int(num) == 1:
        return
    primes = list(Counter(prime_factors(num)).items())
    nFactors = len(primes)
    f = [0] * nFactors
    while True:
        yield reduce(lambda x, y: x*y,
                     [primes[x][0]**f[x] for x in range(nFactors)], 1)
        i = 0
        while True:
            try:
                f[i] += 1
            except:
                return
            if f[i] <= primes[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nFactors:
                return


if __name__ == '__main__':
    # print num_of_divisors(28)
    print(list(list_divisors(100)))
