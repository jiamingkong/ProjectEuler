from operator import __mul__
from functools import reduce

cache = {}


def factorial(x):
    global cache
    x = int(x)
    if x == 0 or x == 1:
        return 1
    if x not in cache:
        cache[x] = reduce(__mul__, range(1, x+1))
    return cache[x]


def main():
    result = 0
    for i in range(10, 100000):
        if sum(map(factorial, list(str(i)))) == i:
            result += i
    print(result)


if __name__ == '__main__':
    main()
