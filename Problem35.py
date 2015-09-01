from Utilities.PrimeGenerator import is_prime

def num_rotate(number):
    l = str(number)
    for i in xrange(len(str(number))):
        yield int(l[-i:] + l[:-i])


def main():
    result = 0
    for i in xrange(1,1000000):
        possible = True
        for j in num_rotate(i):
            if not is_prime(j):
                possible = False
                break
        result += possible
    print result


if __name__ == '__main__':
    main()