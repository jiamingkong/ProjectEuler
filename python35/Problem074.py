from math import factorial


def loop_step(x):
    return sum(map(factorial, map(int, str(x))))


def find_loop_length(x):
    stepper = x
    cycle = 0
    encounter = []
    while stepper not in encounter:
        encounter.append(stepper)
        cycle += 1
        stepper = loop_step(stepper)
    return cycle


def main():
    counter = 0
    counter = filter(lambda x: find_loop_length(x) == 60, range(100, 1000001))
    # for i in counter:
    # print(i)
    return sum(1 for i in counter)


if __name__ == '__main__':
    print(main())
