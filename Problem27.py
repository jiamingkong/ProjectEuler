from Utilities.PrimeGenerator import is_prime, PrimeGenerator

def quadratic(n, a, b):
    return n * n + a * n + b

def test_length(a, b):
    n = 0
    while is_prime(quadratic(n,a,b)):
        n += 1
    return n


def main():
    b_candidate = [i for i in PrimeGenerator(under = 1000)]
    a_range = xrange(-999, 1000)
    max_n = 0
    max_parameter = None
    for a in a_range:
        for b in b_candidate:
            n = test_length(a,b)
            if n > max_n:
                max_n = n
                max_parameter = (a,b)

    return max_parameter

if __name__ == '__main__':
    a,b = main()
    print a * b
