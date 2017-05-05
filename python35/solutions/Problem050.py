from Utilities.PrimeGenerator import PrimeGenerator, is_prime


def main():
    n, maxlen = 1000000, 0
    Set = list(PrimeGenerator(under=10000))
    newb = 2
    for a in range(4):
        for b in range(newb, len(Set)):
            subset = Set[a:b]
            s = sum(subset)
            if is_prime(s) and s < n and len(subset) > maxlen:
                length = len(subset)
                sumprime = s
                maxlen = length
                newb = b
    print(sumprime)

if __name__ == '__main__':
    main()
