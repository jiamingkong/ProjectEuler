# Primes with Runs

# the hard part is to make primes that is 10 digits long

# I am going to use a prime table.. and brute force.


import time
import math


def is_prime(n):
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n == 1:
        return False
    # else only do a prime check if n is some multiple of 6 +/- 1.
    test = n % 6
    if test == 1 or test == 5:
        for i in range(7, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    return False


def pe_111_Primes_with_runs():
    S = [0] * 10

    # max num of zeroes would be 8, as first and last digits can't be zero
    print("Zero")
    for d1 in range(1, 10):
        for d10 in range(1, 10, 2):
            n = d1 * 1000000000 + d10
            # print(n)
            if is_prime(n):
                S[0] += n
                print(n)

    print("One-Nine (but no 2s or 8s found here)")
    for d in range(1, 10):
        nd = 1111111111 * d
        # try all the 10 digit nums with 9 d's in them for primeness
        # 10 places * 9 options = 90 tests
        for p in range(10):  # position (0 being least significant digit, 9 being the most significant)
            for o in range(10):  # other digit
                if o == d:
                    continue
                if o == 0 and p == 9:
                    continue
                # build up n
                n = nd
                n -= d * 10 ** p
                n += o * 10 ** p
                if is_prime(n):
                    S[d] += n
                    print(n)
    print("two digits")
    # 2s and 8s don't work with 9 digits the same
    for d in (2, 8):
        nd = 1111111111 * d
        # try all the 10 digit nums with 8 d's in them for primeness
        for p1 in range(1, 10):
            for o1 in range(10):
                if o1 == d:
                    continue
                if o1 == 0 and p1 == 9:
                    continue
                # build up n
                n1 = nd
                n1 -= d * 10 ** p1
                n1 += o1 * 10 ** p1
                for p2 in range(p1):
                    # range(p1) to avoid double counting
                    for o2 in range(10):
                        if o2 == d:
                            continue
                        # build up n
                        n = n1
                        n -= d * 10 ** p2
                        n += o2 * 10 ** p2

                        if is_prime(n):
                            S[d] += n
                            print(n)
    print(S)
    print(sum(S))


def main():
    global start_time
    start_time = time.time()

    pe_111_Primes_with_runs()

    print("Done in %s seconds." % (time.time() - start_time))
    return


if __name__ == '__main__':
    main()