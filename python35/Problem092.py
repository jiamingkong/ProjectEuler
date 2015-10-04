

def step(number):
    return sum([int(x)*int(x) for x in str(number)])


def loop(number):
    while number not in [1, 89]:
        number = step(number)
    return number == 89


def main():
    counter = 0
    for i in range(10000001):
        if loop(i):
            counter += 1
    return counter

if __name__ == '__main__':
    print(main())