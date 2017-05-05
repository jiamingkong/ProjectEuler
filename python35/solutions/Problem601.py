from Utilities.timeit import timeit
from Utilities.PrimeFactor import prime_factors
from Utilities.PrimeGenerator import PrimeGenerator
from itertools import combinations
from Utilities.gcd import lcm
# this is actually founded.
jumps = {
    3: 1,  # 2
    6: 1,  # 5
    30: 2,  # 7
    210: 1,  # 2
    420: 1,  # 2
    1260: 2,  # 3
    13860: 2,  # 11
    180180: 3,
    360360: 1,
    6126120: 2,
    116396280: 4,
    2677114440: 2,
    13385572200: 2,
    40156716600: 2,
    1164544781400: 2,
    36100888223400: 1,
    72201776446800: 5,
    2671465728531600: 4,
    # 232792560: 4,
    # 698377680: 4,
    # 349188840: 4,
    # 1396755360: -4,
}


lcm_dict = {
    3: 3,
    4: 6,
    6: 30,
    7: 210,
    8: 420,
    10: 1260,
    12: 13860,
    15: 180180,
    16: 360360,
    18: 6126120,
    22: 116396280,
    24: 2677114440,
    26: 13385572200,
    28: 40156716600,
    30: 1164544781400,
    31: 36100888223400,
    36: 72201776446800,
    40: 2671465728531600
}


def streak(n):
    if n % 2 == 0:
        return 1
    else:
        s = 1
        while (n + s) % (s + 1) == 0:
            s += 1
        return s


# @timeit
def p(s, N):
    counter = 0
    collector = []
    for n in range(2, N):
        if jump_streak(n) == s:
            counter += 1
            collector.append(n)
    return counter


# @timeit
def super_p(s, N):
    # print(lcm_dict)
    if s <= 4:
        return p(s, N)
    elif s not in lcm_dict:
        return 0
    else:
        l = lcm_dict[s] * 2 + 1
        j = lcm_dict[s] * 2
        counter = 0
        collector = []
        while l < N:
            if streak(l) == s:
                counter += 1
                collector.append(l)
                l += j
                # print(l)
            else:
                l += j
        return counter
        # print(lcm_dict[s], (lcm_dict[s] * 2 + 1), streak(lcm_dict[s] * 2 + 1), N)
        # return int((N-1 - 2 * lcm_dict[s])/(lcm_dict[s]*4) + 1)


def jump_streak(n):
    if n % 2 == 0:
        return 1
    base = 2
    for k, v in jumps.items():
        if ((n - 1) / 2) % k == 0:
            base += v
    return base


def find_jumpers(start_jump):
    # global jumps
    # print("Starting from {sj}".format(sj = start_jump))
    test_num = start_jump * 2 + 1
    while streak(test_num) == jump_streak(test_num):
        test_num += start_jump
        # print(test_num)
        # print((test_num - 1)/ 2, ":", streak(test_num) - jump_streak(test_num))
        # start_jump = (test_num-1)/2
    return (test_num - 1) / 2, streak(test_num) - jump_streak(test_num)


def find_all_jumpers(start_jump, under=4 ** 31):
    global jumps
    while start_jump < under:
        start_jump, gap = find_jumpers(start_jump)
        jumps[start_jump] = gap
        print("    {sj}: {gp},".format(sj=int(start_jump), gp=int(gap)))


def find_possible_combinations(score):
    for i in range(1, len(jumps)):
        for j in combinations(jumps.keys(), i):
            if sum([jumps[v] for v in j]) == score:
                yield lcm(*j)

if __name__ == '__main__':
    # for i in range(232792561, 10**11, 210):
    #     if streak(i) != jump_streak(i):
    #         print(i-1, streak(i), jump_streak(i))
    #
    #
    # for i in jumps:
    #     print(prime_factors(i))
    # print(streak(180180 * 2 + 1), jump_streak(180180 * 2 + 1))
    # last = max(jumps.keys())
    # print(find_jumpers(last))
    # find_all_jumpers(last)
    # print(p(12, 4 ** 12))
    # a = set()
    # for i in find_possible_combinations(15):
    #     a.add(i)

    # print(i
    cum = 0
    for i in range(1, 32):
        result = super_p(i,4**i)
        print(i, result)
        cum += result

    print(cum)
    # print(super_p(6, 1000000))
    # print([streak(i) for i in range(2, 14)])