from Utilities.PrimeFactor import prime_factors


def count_prime_factors(x):
    return len(set(prime_factors(x)))


def main():
    n = 1
    continous = 0
    while True:
        if count_prime_factors(n) == 4:
            continous += 1
            if continous == 4:
                print(n-3)
                break
        else:
            continous = 0
        n += 1


if __name__ == '__main__':
    main()
