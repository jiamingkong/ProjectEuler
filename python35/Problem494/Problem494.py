from Collatz import test_excessive_pattern, number_to_sigma, get_possible_witness, grow, override_grow, reverse_Collatz
from seq_generator import generate
from itertools import combinations
import pdb
# from multiprocessing import Process, Queue


def find_excessive_generator(length):
    result = 0
    for i in generate("", "", 0, length):
        if test_excessive_pattern(i) != None:
            print(i)
            result += 2
        else:
            result += 1
    return result


def list_all_special():
    for i in range(3, 161):
        result, sigma = number_to_sigma(i)
        if len(sigma) in [15, 16, 17, 20, 50, 81]:
            print(len(sigma), "\n", result, "\n", ''.join(sigma)[:-1])


def get_p_q(sequence):
    y_itcp = y_intercept(sequence)
    return sequence.count('d'), sequence.count('u'), y_itcp


def chain_seq(sequence):
    index = 0
    while index < len(sequence):
        yield sequence[index:]
        index += 1


def get_x(p, q, r, s, y1, y2):
    if y1 > y2:
        return (2**(r - s)) / (2**r - 2 ** p * 3 ** (s - q)) * (3 ** s)
    else:
        return (2**(p - q)) / (2**p - 2 ** r * 3 ** (s - q)) * (3 ** s)


def test_intersection_point(sequence):
    possible_p_q = []
    for i in chain_seq(sequence):
        possible_p_q.append(get_p_q(i))
    max_x = 0
    for i, j in combinations(possible_p_q, 2):
        p, q, y1 = i
        r, s, y2 = j
        _x = get_x(p, q, r, s, y1, y2)
        # print(_x)
        if _x > max_x:
            max_x = _x
    print(max_x)


def y_intercept(sequence):
    seed = 0
    return override_grow(seed, sequence)


def main():
    list_all_special()
    sigma = 'ududdududududdudddudududdududdududududududddududududddduddudduddddudddudududdddd'
    test_intersection_point(sigma + 'u')

def grow_it(number, target_length, ):
    # counter = target_length - len()
    # whi
    a,b = reverse_Collatz(number)
    print(a,b)
    pdb.set_trace()


if __name__ == '__main__':
    i = 14
    result = find_excessive_generator(i)
    print((i + 1, result))
    # list_all_special()
    # main()
    # grow_it(159)
    # f = open("ProjectEuler494.txt", "w")
    # f.write(str(result))
    # print(test_excessive_pattern(sigma))
    # for i in get_possible_witness(sigma):
        # print(i)

    # y_intercept('ududdududududdudddudududdududdududududududddududududddduddudduddddudddudududdddd')