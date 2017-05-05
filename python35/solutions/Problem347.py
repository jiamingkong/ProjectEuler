from Utilities.PrimeGenerator import PrimeGenerator


def gen_distinct_primefacs(n):
    """Generates a list of a list of prime factors for all numbers <= n"""
    prime_facs = [[] for i in range(n+1)]
    for prime in PrimeGenerator(under=n+1):
        for i in range(prime, n+1, prime):
            prime_facs[i].append(prime)
    return prime_facs

def S(n):
    prime_factors = gen_distinct_primefacs(n)
    pairs = {}
    for i in range(1, n+1):
        p = prime_factors[i]
        if len(p) == 2:
            pairs[tuple(p)] = i
    return sum(pairs.values())

print(S(10**7))