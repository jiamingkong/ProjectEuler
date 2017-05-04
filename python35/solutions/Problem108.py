from Utilities.PrimeFactor import prime_factors
import pdb
from collections import Counter
from functools import reduce



def get_num_of_solutions(n):
    factors = prime_factors(n)
    return factors

def get_number_of_divisors(factors):
    # this is to compensate for the square of N
    factor_dict = Counter(factors)
    return reduce(lambda x, y: x*y, [2 * v + 1 for k, v, in factor_dict.items()])

def pipeline(n):
    num = get_number_of_divisors(get_num_of_solutions(n))
    return (num+1)/2


if __name__ == '__main__':
    n = 4
    while pipeline(n) < 1000:
        n+=1
    print(n)