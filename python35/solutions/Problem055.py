

def test_lychrel(number):
    is_lychrel = True
    for trial in range(50):
        number = reverse_add(number)
        if is_palindrome(number):
            is_lychrel = False
            break
    return is_lychrel


def reverse_add(number):
    return int(str(number)[::-1]) + number


def is_palindrome(number):
    return number == int(str(number)[::-1])


def main():
    counter = 0
    for x in range(10000):
        _x = x
        if test_lychrel(_x):
            counter += 1
    return counter


if __name__ == '__main__':
    print(main())
