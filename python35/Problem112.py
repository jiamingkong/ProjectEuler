# from functools import map


def is_bouncy(number):
    seperated = [int(i) for i in str(number)]
    if not all([i >= j for i, j in zip(seperated[1:], seperated[:-1])]) \
       and not all([i <= j for i, j in zip(seperated[1:], seperated[:-1])]):
        return True
    else:
        return False


def main():
    target = 99
    number = 99
    bouncy_count = 0
    while int(bouncy_count / number * 100) != target:
        number += 1
        if is_bouncy(number):
            bouncy_count += 1

    return number

if __name__ == '__main__':
    print(main())
    # print(is_bouncy(123))
    # print(is_bouncy(21570))
