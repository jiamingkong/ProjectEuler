import sys
import itertools


def reverse_generate(seed, target_length, container=[]):
    if len(seed) == target_length:
        container.append(seed)
        return

    if seed[0] == 'u':
        reverse_generate('d' + seed, target_length, container)
    else:
        reverse_generate('u' + seed, target_length, container)
        reverse_generate('d' + seed, target_length, container)


def _generate(pre0, pre1, cur_len, max_len, container=[]):
    if (cur_len == max_len - 1):
        container.append("".join([pre0, pre1, "0"]))
        return

    if (pre1 == '1'):
        cur_char = '0'
        _generate(pre0 + pre1, cur_char, cur_len + 1, max_len, container)
    else:
        cur_char = '0'
        _generate(pre0 + pre1, cur_char, cur_len + 1, max_len, container)
        cur_char = '1'
        _generate(pre0 + pre1, cur_char, cur_len + 1, max_len, container)


def generate(pre0, pre1, cur_len, max_len):
    '''
    Using yield from keyword to iterate all possible sequences of operators
    '''
    if (cur_len == max_len - 1):
        yield "".join((pre0, pre1, "d"))
        return

    if (pre1 == 'u'):
        yield from generate(pre0 + pre1, 'd', cur_len + 1, max_len)
    else:
        yield from generate(pre0 + pre1, 'd', cur_len + 1, max_len)
        yield from generate(pre0 + pre1, 'u', cur_len + 1, max_len)


def filter_generate(max_len):
    return filter(lambda i: 'uu' not in i,
                  (''.join(i) +
                   'd' for i in itertools.product('du', repeat=max_len - 1))
                  )


def math_gen(maxlen):
    pattern = "{{:0{}b}}".format(maxlen)
    upperbound = 2**maxlen
    for i in itertools.count(2):
        if i ^ i * 2 == i * 3:
            yield pattern.format(i)
        if i >= upperbound:
            break


if __name__ == "__main__":
    for i in generate("", "", 0, 6):
        print(i)
