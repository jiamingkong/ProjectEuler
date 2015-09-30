'''
Note to self:

9 ** 5 = 59049
solve : n * 60000 < 10**n makes approx 5.5

'''

def test_number(number):
    sums = sum([int(x)**5 for x in list(str(number))])
    return sums == number


def main():
    result = sum(filter(test_number, range(500000)))
    return result


if __name__ == '__main__':
    print(main())