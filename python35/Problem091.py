from itertools import product


def three_side_square(x1, y1, x2, y2):
    l1 = x1 ** 2 + y1 ** 2
    l2 = x2 ** 2 + y2 ** 2
    l3 = (x1-x2) ** 2 + (y1 - y2) ** 2
    return l1, l2, l3


def has_right_angle(side1, side2, side3):
    s = sorted([side1, side2, side3])
    if s[0] == 0:
        return False
    return s[0] + s[1] == s[2]


def main():
    counter = 0
    for temp in product(range(0, 51), repeat=4):
        x1, y1, x2, y2 = temp
        if has_right_angle(*three_side_square(x1, y1, x2, y2)):
            counter += 1

    # the repetition is introduced by the sort function, divide by two, I know
    # I can remove the repetition by manually writing the loop. Yet I don't
    # want to. Just too lazy.
    return counter / 2


if __name__ == '__main__':
    print(main())
