from operator import __mul__

def generate(target_length, positions):
    result = " "
    current = 1
    while target_length > 0:
        str_current = str(current)
        result += str_current
        target_length -= len(str_current)
        current += 1
    return map(lambda x: int(result[x]), positions)


def main():
    numbers = generate(1000000, [1,10,100,1000, 10000, 100000, 1000000])
    print reduce(__mul__, numbers)


if __name__ == '__main__':
    main()