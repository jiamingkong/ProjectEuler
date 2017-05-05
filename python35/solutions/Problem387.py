from Utilities.PrimeGenerator import fast_is_prime

"""
The trick here is that any Right truncatable Harshad number can at most contain 1 odd digit.

Why?
"""

LIMIT = 10 ** 14


def sumSRTHPRec(n, digitsum, limit):
    t = 0
    for d in range(0, 10):
        rtH = n*10 + d
        rtHdigitsum = digitsum + d
        if rtH > limit:
            return t
        if rtH % rtHdigitsum == 0:
            t += sumSRTHPRec(rtH, rtHdigitsum, limit)
            if fast_is_prime(rtH/rtHdigitsum):
                for i in [1, 3, 7, 9]:
                    srtHp = rtH*10 + i
                    if srtHp > limit:
                        return t
                    if fast_is_prime(srtHp):
                        t += srtHp
    return t


def sumSRTHarshadPrimes(limit):
    return sum(sumSRTHPRec(h, h, limit) for h in range(1, 10))


if __name__ == "__main__":
    # print(compute())
    print(sumSRTHarshadPrimes(LIMIT))
