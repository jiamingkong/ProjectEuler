from Utilities import PrimeGenerator
from heapq import heapify, heappop, heappush

def main():
    # the sorting thing here is very important, why is that?
    modulo = 500500507
    result = 1
    prime_list = list(PrimeGenerator(count=500500))
    heapify(prime_list)
    for i in range(500500):
        p = heappop(prime_list)
        result *= p
        heappush(prime_list, p*p)
        result %= modulo

    return result

if __name__ == '__main__':
    print(main())
