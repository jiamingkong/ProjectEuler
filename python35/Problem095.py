from Utilities.PrimeFactor import list_divisors
from Utilities.PrimeGenerator import is_prime


def get_proper_divisors(number):
    # print(number)
    return int(sum(list_divisors(int(number))) - number)


def main():
    result = 0
    limit = 1000000
    chain_length = 0
    mapping = {}
    current_chain = []
    for x in range(2, limit + 1):
        if is_prime(x):
            continue
        current_chain = []
        failed = False
        _x = x
        while _x not in current_chain:
            current_chain.append(_x)
            _x = get_proper_divisors(_x)
            if _x > limit or mapping.setdefault(_x, False):
                failed = True
                break

        if not failed:
            if len(current_chain) > chain_length:
                chain_length = len(current_chain)
                result = min(current_chain)

        for j in current_chain:
            mapping[j] = False

    return result


if __name__ == '__main__':
    # print(get_proper_divisors(12496))

    print(main())
