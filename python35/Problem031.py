def calc_ways(target, coins):
    ways = [1] * (target + 1)
    for i in coins[1:]:
        for money in range(i, target + 1):
            ways[money] += ways[money - i]
    return ways[target]

if __name__ == '__main__':
    print(calc_ways(200, [1, 2, 5, 10, 20, 50, 100, 200]))
