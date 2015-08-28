# sorry I am too lazy to come up with anything faster. I know I can do a poly-nomial.


def main(side):
    n = 1
    result = 1
    mul = 2

    while n < side ** 2:
        for i in xrange(0, 4):
            n += mul
            result += n
        mul += 2
    return result

if __name__ == '__main__':
    print main(1001)
