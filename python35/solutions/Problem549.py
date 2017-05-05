from Utilities import prime_factors
from Utilities import PrimeGenerator
from Utilities.MemCache import lru_cache_function
from collections import Counter
from Utilities.timeit import timeit
from functools import lru_cache
import pdb
import math


@timeit
def solve(N=10 ** 8):
    total = 0
    small_primes = list(PrimeGenerator(under=int(math.sqrt(N) + 1)))  # Now we need to store s(p^k) for the small primes.
    s_sto = []  # So s_sto[i][k] gives s( (p_i)^k ).
    for p in small_primes:
        s_sto.append([0, p])
        k = 2
        while p ** k < N:
            last = s_sto[-1][-1]
            # If last has p^i power, then it appears i times.
            mult = 0
            while last % (p ** mult) == 0:
                mult += 1
            mult -= 1
            if s_sto[-1][-mult] == last:
                s_sto[-1].append(last + p)
            else:
                s_sto[-1].append(last)
            k += 1
        # So every n < 10**8 is a product of small primes and AT MOST one big prime.
    s_array = [0 for i in range(N + 1)]
    for pi in range(len(small_primes)):
        k = 1
        pk = small_primes[pi]
        while pk <= N:
            i = pk
            while i <= N:
                s_array[i] = max(s_array[i], s_sto[pi][k])
                i += pk
            k += 1
            pk *= small_primes[pi]
        # Now, everything = 0 is a big prime.s
    for si in range(int(math.sqrt(N)), len(s_array)):
        if s_array[si] == 0:
            sik = si
            while sik <= N:
                s_array[sik] = max(s_array[sik], si)
                sik += si
    return sum(s_array)




if __name__ == '__main__':
    print(solve())


