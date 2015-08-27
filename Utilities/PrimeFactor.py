from collections import Counter

def prime_factors(x):
    factors = []
    while x%2 == 0:
        factors.append(2)
        x /=2
    i = 3
    while i * i <= x:
        while x%i == 0:
            x /=i
            factors.append(i)
        i += 2
    if x>1:
        factors.append(x)
    return factors

def num_of_divisors(x):
    primes = prime_factors(x)
    things = Counter(primes)
    result = 1
    for i in things.values():
        result *= (i + 1)
    return result

if __name__ == '__main__':
    print num_of_divisors(28)