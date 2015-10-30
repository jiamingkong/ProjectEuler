
from seq_generator import generate, math_gen
from multiprocessing import Pool


family = []
queue = []


def Collatz(number):
    '''
    This function performs the basic Collatz iteration.
    '''

    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(3 * number + 1)


def reverse_Collatz(number):
    '''
    This function seeks to reverse iterate the collatz sequence to 'grow' it.
    '''
    if (number - 1) % 3 == 0:
        a = int((number - 1)/3)
        if a % 2 != 0:
            return [int((number - 1) / 3), number * 2]
        # yield int((number-1)/3)
        # yield number * 2
    # else:
    return [number * 2]
        # yield number * 2


def end(number):
    return number is None or (number != 0 and is_power_of_two(number))


def is_power_of_two(number):
    return number & (number - 1) == 0


def category(a_list):
    global family
    gap = list(map(lambda x, y: x > y, a_list[:-1], a_list[1:]))
    if gap not in family:
        family.append(gap)
        return True
    else:
        return False


def iterate(n):
    result = []
    while not end(n):
        result.append(n)
        n = Collatz(n)
    return result


def number_to_sigma(number):
    result = []
    sigma = []
    while not end(number):
        result.append(number)
        number = Collatz(number)
        if number > result[-1]:
            sigma.append('u')
        else:
            sigma.append('d')
    return result, sigma


def to_standard(lst):
    """Converts a list of distinct elements into a permutation by replacing the
    i-th smallest element with the integer i."""
    result = [0 for i in range(len(lst))]
    for i, (_, j) in enumerate(sorted((lst[j], j) for j in range(len(lst)))):
        result[j] = i+1
    return result


def u(x):
    return 3*x + 1


def d(x):
    if x % 2 == 0:
        return x / 2
    else:
        raise ArithmeticError("Not a multiple of 2.")


def D(x):
    return 2 * x


def U(x):
    if (x-1) % 3 == 0:
        return (x - 1) // 3
    else:
        raise ArithmeticError("Not a multiple of 3")


def U_ovrd(x):
    return (x-1)/3


def D_ovrd(x):
    return 2 * x


mapper = {"u": U,
          "d": D,
          '1': U,
          '0': D}

override_mapper = {
    "u": U_ovrd,
    "d": D_ovrd,
    "1": U_ovrd,
    "0": D_ovrd
}


def override_grow(witness, sequence):
    _sequence = ["u"] + list(sequence)[::-1]
    result = [witness]
    for i in _sequence:
        result.append(override_mapper[i](result[-1]))
    return result[::-1][:-1]


def grow(witness, sequence):
    _sequence = ["u"] + list(sequence)[::-1]
    result = [witness]
    for i in _sequence:
        result.append(mapper[i](result[-1]))
    return result[::-1][:-1]


def Collatz_generator(length):
    result = ["d"]


def get_possible_witness(sequence, max_j=2):
    k = sequence.count('u')
    a = 4
    j = 0
    while j < max_j:
        yield 2**(a + j * (2 * (3 ** k))), j
        j += 1


def test_excessive_pattern(sequence):
    possibilities = 0
    seeds = []
    witnessed = []
    for i, c in get_possible_witness(sequence):
        try:
            list_1 = to_standard(grow(i, sequence))
            if list_1 not in witnessed:
                witnessed.append(list_1)
                seeds.append(c)
                possibilities += 1
            if possibilities == 2:
                return sequence
                break
        except:
            pass
    return None


def find_excessive_generator(pool, length):
    container = list(generate("", "", 0, length))

    result = pool.map(test_excessive_pattern, container)
    result = [x for x in result if x is not None]
    return result


def iter_find_ET(length):
    counter = []
    for i in math_gen(length):
        i = i.replace('1', "u").replace("0", 'd')
        if test_excessive_pattern(i) is not None:
            counter.append(i)
    return counter


def find_excessive_generator_by_extension(pool, length, container=[]):
    if container == []:
        generate("", "", 0, length - 2, container)
        result = pool.map(test_excessive_pattern, container)
        container = [x for x in result if x is not None]
    candidate = []
    for i in container:
        if i.startswith("u"):
            candidate.append('ud' + i)
            candidate.append('dd' + i)
        else:
            candidate.append('du' + i)
            candidate.append('dd' + i)
            candidate.append('ud' + i)

    result = pool.map(test_excessive_pattern, candidate)
    result = [x for x in result if x is not None]
    return result


if __name__ == '__main__':
    # p = Pool(6)
    # list_15 = find_excessive_generator(p, 14)
    # list_16 = find_excessive_generator(p, 15)
    # a = 18
    # list_17 = find_excessive_generator(p, a)
    # print list_17
    # for i in list_17:
    #     print i, i.count('u'), i.count('d')
    # print(
    #     (sorted(find_excessive_generator_by_extension(p, a + 1, list_17)), "Extension"))
    # print((sorted(find_excessive_generator(p, a + 2)), "Raw"))
    # print test_excessive_pattern("uuddddudududduddd")
    # print len(find_excessive_generator(p, 18))
    # print len(find_excessive_generator(p, 19))
    # print len(find_excessive_generator(p, 20))
    # print len(find_excessive_generator(p, 21))
    # print len(find_excessive_generator(p, 22))
    # print len(find_excessive_generator(p, 23))

    # print iter_find_ET(15)
    # print len(iter_find_ET(24))
    print(iterate(7))