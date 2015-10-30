from Utilities.factorial import factorial

def choose(n, m):
    assert n >= m
    return int(factorial(n) / factorial(m) / factorial(n- m))


def main():
    # expectation = # E(x1 + x2 + x3 + x5 )

    return 7 * (1 - choose(60, 20) / choose(70, 20))


if __name__ == '__main__':
    print(main())