# from ..Utilities import choose


def choose(total, subset):
    subset = min(subset, total - subset)

    res = 1
    for i in range(1, subset+1):
        res *= total - subset + 1
        res /= i

    return res

def CatalanNumber(n):
    return choose(2 * n, n) / (n + 1)

def main():
    result = 0
    n = 12
    for i in range(2, n/2+1):
        result += choose(n, i) * choose(n-i, i) / 2
        result -= choose(n, 2 * i) * CatalanNumber(i)

    return result

if __name__ == '__main__':
    print(main())