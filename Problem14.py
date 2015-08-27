cache = {2:2, 1:1}

def Collatz_gen(x):
    while x != 1:
        if x%2 == 0:
            x/=2
            yield x
        else:
            x = 3 * x + 1
            yield x

def Collatz_length(x):
    global cache
    if x in cache:
        return cache[x]
    counter = 0
    for i in Collatz_gen(x):
        counter += 1
        if i in cache:
            cache[x] = cache[i] + counter
            break
    return cache[x]

def main():
    global cache
    starter = 2
    max_found = 0
    max_seed = None
    while starter < 1000000:
        curr = Collatz_length(starter)
        if max_found < curr:
            max_found = curr
            max_seed = starter
        starter += 1
    return max_seed

if __name__ == '__main__':
    print main()