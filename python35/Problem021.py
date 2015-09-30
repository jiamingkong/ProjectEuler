from Utilities.PrimeFactor import list_divisors

cache = {}

def main(under):
    global cache
    for i in range(2, under):
        divisor_sum = sum(list(list_divisors(i))) - i
        if divisor_sum < under:
            cache[i] = divisor_sum

    result = 0
    for i in range(2, under):
        if i in cache and cache[i] in cache and i != cache[i] and cache[cache[i]] == i:
            print(">>", i, cache[i])
            result += i
    print(result)

if __name__ == '__main__':
    main(10000)