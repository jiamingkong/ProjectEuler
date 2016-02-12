# combinatoric selections


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def main():
    counter = 0
    for n in range(10, 101):
        for j in range(2, n):
            if C(n, j) > 1000000:
                counter += 1
    print(counter)


if __name__ == '__main__':
    main()
