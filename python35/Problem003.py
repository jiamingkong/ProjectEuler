# import pyprimesieve as sieve
from Utilities.PrimeFactor import prime_factors


if __name__ == '__main__':
    # first trial, not as easy as it seems, this will overflow!
    # print max([i[0] for i in sieve.factorize(600851475143)])

    # second trial did my own version.
    print(max(prime_factors(600851475143)))
