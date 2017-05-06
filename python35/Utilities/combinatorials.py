def choose(total, subset):
    subset = min(subset, total - subset)

    res = 1
    for i in range(1, subset+1):
        res *= total - subset + 1
        res /= i

    return res


if __name__ == '__main__':
    print(choose(4,2))