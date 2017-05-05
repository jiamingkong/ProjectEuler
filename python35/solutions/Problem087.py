from Utilities.PrimeGenerator import PrimeGenerator
from math import sqrt
from itertools import product
import pdb


def main():
    limit = 50000000
    all_primes_squre = [i * i for i in PrimeGenerator(under=int(limit**(1/2)))]
    all_primes_cub = [
        i ** 3 for i in PrimeGenerator(under=int(limit ** (1/3)))]
    all_primes_quad = [i**4 for i in PrimeGenerator(under=int(limit ** (1/4)))]
    found_numbers = set()
    for i, j, k in product(all_primes_squre, all_primes_cub, all_primes_quad):
        cand = i + j + k
        if cand < limit:
            found_numbers.add(cand)
    print(len(found_numbers))

if __name__ == '__main__':
    main()
