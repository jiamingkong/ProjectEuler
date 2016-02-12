numbers = '''\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''


def main(string):
    array = build_array(string)
    step = 2
    result = dp_step(array[0], array[1])
    while step < len(array):
        result = dp_step(result, array[step])
        step += 1
    print(max(result))


def dp_step(upper, lower):
    _upper = [0] + upper + [0]
    result = []
    for i, num in enumerate(lower):
        result.append(max([_upper[i], _upper[i+1]]) + num)
    return result


def build_array(string):
    result = []
    for i in string.split("\n"):
        if i != "":
            result.append(list(map(int, i.split(" "))))
    return result

if __name__ == '__main__':
    main(numbers)
