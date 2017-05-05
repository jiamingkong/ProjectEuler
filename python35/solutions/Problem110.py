# because the requirement changed a bit from problem 108, the brute force won't work.
# need a smarter way to construct the number
# the idea was to automatically construct the number rather than doing it by hand.

# given the root N, the number of divisors of square(n) (aka F(n))
# will be cumprod(2a_i+1) where cumprod(p_i^a_i) = n

# !!! so this becomes an integer programming problem that is
# to make F(n) > 4_000_000 while minimizing cumprod(p_i^a_i)
# If I have an Mixed Integer Programming Solver who could take nonlinear constraints I will go for it...

# guess I will just go and brute force, this made me happy
# starting with worst situation, a_i = 1 for any i, we will go to 14 primes because 3**14 > 4m

from Utilities.PrimeGenerator import PrimeGenerator
import numpy as np
import pdb
from itertools import combinations_with_replacement


box = list(range(0, 10))
LIMIT = 4000000
all_primes = np.asarray(list(PrimeGenerator(count=14)))


def good_enough(array):
    return np.cumprod(np.asarray(array) * 2 + 1)[-1] > LIMIT

def n(array):
    return np.cumprod([i**j for i, j in zip(all_primes, array)], dtype=float)[-1]


def main():
    array = combinations_with_replacement(box, 14)
    min = 10e20
    for i in array:
        j = i[::-1]
        if sum(j) == 140:
            print("Search stopped")
            break
        if good_enough(j):
            number = n(j)
            if number < min:
                min = n(j)
                print(min)
    print(int(min))


if __name__ == '__main__':
    main()




