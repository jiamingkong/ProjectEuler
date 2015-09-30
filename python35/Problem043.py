from itertools import permutations

def generator():
    num_list = list(map(str, list(range(0, 10))))
    for i in permutations(num_list, 10):
        if i[0] != '0':
            yield ''.join(i)


def check_number(i):
    if int(i[1:4]) % 2 == 0 and int(i[2:5]) % 3 == 0 and int(i[3:6]) % 5 == 0 and int(i[4:7]) % 7 == 0 and int(i[5:8]) % 11 == 0 and int(i[6:9]) % 13 == 0 and int(i[7:10]) % 17 == 0:
        return True
    else:
        return False

def main():
    result = 0
    for i in generator():
        if check_number(i):
            result += int(i)
            print(i)
    print(">>>", result)


if __name__ == '__main__':
    main()
