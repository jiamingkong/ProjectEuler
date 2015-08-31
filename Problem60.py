from Utilities.PrimeGenerator import PrimeGenerator, is_prime
from itertools import permutations


def check_pair(a, b):
    if is_prime(a * (10**len(str(b))) + b) and is_prime(b * (10**len(str(a))) + a):
        return True
    else:
        return False


def main(length):
    candidate = list(PrimeGenerator(under=10000))
    scores = {i: 0 for i in candidate}
    link = {i: [] for i in candidate}

    for a, b in permutations(candidate, 2):
        if check_pair(a, b):
            link[a].append(b)
            link[b].append(a)
            scores[a] += 1
            scores[b] += 1
    possible = sorted([j for j in scores if scores[j] >= length - 1])
    for comb in permutations(possible, length):
        success = True
        for a, b in permutations(comb, 2):
            if b not in link[a] or a not in link[b]:
                success = False
                break
        if success:
            print comb, sum(comb)


if __name__ == '__main__':
    main(5)
    # print check_pair(7, 109)
