from math import sqrt

loop_cache = []

def find_sqrt(number):
    return int(sqrt(number))

def fraction_expansion(s):
    m = 0
    d = 1
    a = find_sqrt(s)
    yield m, d, a
    while True:
        new_m = d * a - m
        new_d = (s - new_m * new_m) / d
        new_a = int((sqrt(s) + new_m) / new_d)
        yield new_m, new_d, new_a
        m = new_m
        d = new_d
        a = new_a


def find_loop(generator):
    global loop_cache
    for i in generator:
        if i not in loop_cache:
            loop_cache.append(i)
        else:
            d = len(loop_cache) - loop_cache.index(i)
            loop_cache = []
            return d

def main():
    odd_period = 0
    for i in range(10001):
        if find_sqrt(i) **2 == i:
            continue
        else:
            if find_loop(fraction_expansion(i)) %2 == 1:
                odd_period += 1
    print(odd_period)


if __name__ == '__main__':
    # print find_loop(fraction_expansion(13))
    main()