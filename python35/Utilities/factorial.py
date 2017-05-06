from math import sqrt, trunc
from Utilities.gcd import gcd

def factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


def main():
    result = 0
    limit = 1500000
    cache = {i: 0 for i in range(0, limit + 1)}
    for m in range(2, trunc(sqrt(limit)) + 1):
        for n in range(1, m):
            if (n + m) % 2 == 1 and gcd(n, m) == 1:
                a = m * m + n * n
                b = m * m - n * n
                c = 2 * m * n
                pa = a + b + c
                while pa <= limit:
                    cache[pa] += 1
                    if cache[pa] == 1:
                        result += 1
                    if cache[pa] == 2:
                        result -= 1
                    pa += a + b + c
    return result

if __name__ == '__main__':
    print(main())
