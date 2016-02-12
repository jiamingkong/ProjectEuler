def main():
    target = 100
    ways = {i: 0 for i in range(1, 101)}
    ways[0] = 1

    for i in range(1, 100):
        for j in range(i, target + 1):
            ways[j] += ways[j-i]

    return ways[target]


if __name__ == '__main__':
    print(main())
