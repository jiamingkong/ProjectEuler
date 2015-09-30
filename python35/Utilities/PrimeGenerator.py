import math
from .gcd import gcd

def PrimeGenerator(count = None, under = None):
    D = {}
    q = 2
    c = 0
    if count is None:
        test = lambda c, q: True
    else:
        test = lambda c, q: c < count
    if under is not None:
        test = lambda c, q: q <= under

    while test(c,q):
        if q not in D:
            yield q
            c+= 1
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def is_prime(n):
    if n <= 0:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return n > 1;

def __euler_loop(n):
    coprimes = [1]
    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return len(coprimes)

def totient(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Can't compute totient function for {n}".format(n = n))
    if n == 1:
        return 1
    elif is_prime(n):
        return n -1
    else:
        return __euler_loop(n)

if __name__ == '__main__':
    # for i in PrimeGenerator(under = 100):
        # print i

    print(totient(10))