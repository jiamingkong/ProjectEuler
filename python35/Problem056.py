
def sum_digit(number):
    return sum([int(i) for i in str(number)])


def main():
    max_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            _sum = sum_digit(a**b)

            if _sum > max_sum:
                max_sum = _sum
    return max_sum

if __name__ == '__main__':
    print(main())
