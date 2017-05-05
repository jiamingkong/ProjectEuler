from math import sqrt
cache = {}


def pentagonal(n):
    global cache
    cache.setdefault(n, n * (3 * n - 1) / 2)
    return cache[n]


def is_pentagonal(x):
    check = (1.0 + sqrt(24 * x + 1.0)) / 6.0
    return int(check) == check


def check(a, b):
    a, b = min([a, b]), max([a, b])
    surp = pentagonal(a) + pentagonal(b)
    diff = pentagonal(b) - pentagonal(a)
    if is_pentagonal(surp) and is_pentagonal(diff):
        return True
    else:
        return False


def main():
    for k in range(1, 3000):
        for j in range(k+1, 3000):
            if check(k, j):
                print(pentagonal(j) - pentagonal(k))
                break


if __name__ == '__main__':
    main()
