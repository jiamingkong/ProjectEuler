'''
Note to self:

9 ** 5 = 59049
solve : n * 60000 < 10**n makes approx 5.5

'''

def test_number(number):
    sums = sum(map(lambda x: int(x)**5, list(str(number))))
    return sums == number


def main():
    result = sum(filter(test_number, xrange(500000)))
    return result


if __name__ == '__main__':
    print main()