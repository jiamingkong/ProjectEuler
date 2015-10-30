import math
from .gcd import gcd
from math import log


def PrimeGenerator(count=None, under=None):
    D = {}
    q = 2
    c = 0
    if count is None:
        test = lambda c, q: True
    else:
        test = lambda c, q: c < count
    if under is not None:
        test = lambda c, q: q <= under

    while test(c, q):
        if q not in D:
            yield q
            c += 1
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
        if n % i == 0:
            return False
    return n > 1


def fast_is_prime(n):
    """
    http://mathworld.wolfram.com/StrongPseudoprime.html
    Zhang (2001, 2002, 2005, 2006, 2007) conjectured that
    """
    n = int(n)
    firstPrime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                  61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]
    lpow = pow
    if n >= 10**36:
        # w = range(2, int(2*log(n)**2)) # pour etre deterministe, ERH dependent !!!
        # (log 2)-1 log n log log n.
        logn = log(n)
        # meilleure borne, conjecture !!!
        w = range(2, int(logn*log(logn)/log(2)))

    elif n >= 1543267864443420616877677640751301:
        w = firstPrime[:20]
    # elif n >= 1543267864443420616877677640751301: w = firstPrime[:19]
    elif n >= 564132928021909221014087501701:
        w = firstPrime[:18]
    # elif n >= 564132928021909221014087501701: w = firstPrime[:17]
    elif n >= 59276361075595573263446330101:
        w = firstPrime[:16]
    elif n >= 6003094289670105800312596501:
        w = firstPrime[:15]
    elif n >= 3317044064679887385961981:
        w = firstPrime[:14]
    elif n >= 318665857834031151167461:
        w = firstPrime[:13]
    elif n >= 3825123056546413051:
        w = firstPrime[:12]  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif n >= 341550071728321:
        w = firstPrime[:9]  # [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif n >= 3474749660383:
        w = firstPrime[:7]  # [2, 3, 5, 7, 11, 13, 17]
    elif n >= 2152302898749:
        w = firstPrime[:6]  # [2, 3, 5, 7, 11, 13]
    elif n >= 4759123141:
        w = firstPrime[:5]  # [2, 3, 5, 7, 11]
    elif n >= 9006403:
        w = [2, 7, 61]
    elif n >= 489997:
        if n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17 and n % 19\
                and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43 and n % 47\
                and n % 53 and n % 59 and n % 61 and n % 67 and n % 71 and n % 73 and n % 79\
                and n % 83 and n % 89 and n % 97 and n % 101:
            # Fermat 2, 3, 5, special remix
            hn = n >> 1
            nm1 = n-1
            p = lpow(2, hn, n)
            if (p == 1 or p == nm1):
                p = lpow(3, hn, n)
                if (p == 1 or p == nm1):
                    p = lpow(5, hn, n)
                    return (p == 1 or p == nm1)
        return False
    elif n >= 42799:
        # Fermat 2, 5
        return n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17\
            and n % 19 and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43\
            and lpow(2, n-1, n) == 1 and lpow(5, n-1, n) == 1
    elif n >= 841:
        # Fermat 2
        return n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17\
            and n % 19 and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43\
            and n % 47 and n % 53 and n % 59 and n % 61 and n % 67 and n % 71 and n % 73\
            and n % 79 and n % 83 and n % 89 and n % 97 and n % 101 and n % 103\
            and lpow(2, n-1, n) == 1
    elif n >= 25:
       # divisions seules
        return n & 1 and n % 3 and n % 5 and n % 7\
            and n % 11 and n % 13 and n % 17 and n % 19 and n % 23
    elif n >= 4:
        return n & 1 and n % 3
    else:
        return n > 1

    if not(n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17
           and n % 19 and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43
           and n % 47 and n % 53 and n % 59 and n % 61 and n % 67 and n % 71 and n % 73
           and n % 79 and n % 83 and n % 89):
        return False

    # Miller-Rabin, avec témoins "w"
    s = 0
    d = n-1
    while not d & 1:
        d >>= 1
        s += 1
    for p in w:
        x = lpow(p, d, n)
        if x == 1:
            continue
        for _ in range(s):
            if x+1 == n:
                break
            x = x*x % n
        else:
            return False
    return True


def __euler_loop(n):
    coprimes = [1]
    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return len(coprimes)


def totient(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Can't compute totient function for {n}".format(n=n))
    if n == 1:
        return 1
    elif is_prime(n):
        return n - 1
    else:
        return __euler_loop(n)

if __name__ == '__main__':
    # for i in PrimeGenerator(under = 100):
        # print i

    # print(totient(10))
    print(fast_is_prime(3))
