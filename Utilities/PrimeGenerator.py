import math

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
    for i in xrange(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return n > 1;

if __name__ == '__main__':
    for i in PrimeGenerator(under = 100):
        print i