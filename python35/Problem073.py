from Utilities.gcd import gcd


def find_range(d, low=1/3, high=1/2):
    # this function return the range of n that makes n/d lie between low and
    # high
    return range(int(d * low) + 1, int(d * high)+1)


def main():
    counter = 0
    for d in range(5, 12001):
        for n in find_range(d):
            if gcd(n, d) == 1:
                counter += 1
    print(counter)


if __name__ == '__main__':
    main()
    # print(find_range(5))
