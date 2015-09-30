cache = {}

def add_to_set(current):
    global cache
    number = current ** 3
    key = ''.join(sorted(str(number)))
    cache.setdefault(key,[])
    cache[key].append(current)

def main():
    found = False
    current = 100
    while not found:
        add_to_set(current)
        for key,value in cache.items():
            if len(value) == 5:
                print(value[0] ** 3)
                found = True
                break
        current += 1


if __name__ == '__main__':
    # add_to_set(100)
    # print cache

    main()