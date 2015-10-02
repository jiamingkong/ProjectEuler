from Utilities.PrimeGenerator import PrimeGenerator
import pdb

def main():
    target = 2
    primes = [x for x in PrimeGenerator(under=1000)]
    # ways = {i:0 for i in range(0,target + 1)}
    while True:
        ways = [0] * (target + 1)
        ways[0] = 1
        for x in range(0,len(primes)):
            for y in range(primes[x], target + 1):
                ways[y] += ways[y - primes[x]]

        if ways[target] > 5000:
            break
        target += 1

    return target

if __name__ == '__main__':
    print(main())