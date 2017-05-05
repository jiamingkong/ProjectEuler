from math import sqrt, trunc


def is_pentagonal(x):
    r = sqrt(24 * x + 1)
    return (r == trunc(r) and r % 6 == 5)


def triangular_generator():
    n = 144
    while True:
        yield n * (2 * n - 1)
        n += 1


def main():
    for i in triangular_generator():
        if is_pentagonal(i):
            print(i)
            break


if __name__ == '__main__':
    # print is_pentagonal(40755)
    main()
