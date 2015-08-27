from Utilities.PrimeFactor import list_divisors
from Utilities.two_sum import twoSum

MAX = 28123


def is_abundant(number):
    return sum(list(list_divisors(number))) - number - number > 0


def find_abundant(under):
    result = filter(is_abundant, xrange(2, under))
    return result


def main():
    abunds = find_abundant(MAX)
    result = 0
    for i in xrange(2, MAX + 1):
        if twoSum(abunds, i) is None:
            result += i
    print result


if __name__ == '__main__':
    print main()
