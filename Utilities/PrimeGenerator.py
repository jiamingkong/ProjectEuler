import math

def PrimeGenerator(count = None):
    D = {}
    q = 2
    c = 0
    if count is None:
        test = lambda x: True
    else:
        test = lambda x: x < count
    while test(c):
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
    for i in PrimeGenerator(100):
        print i