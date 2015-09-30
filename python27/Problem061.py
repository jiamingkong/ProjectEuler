solution = [0] * 6


def triangle(n):
    return n * (n + 1) / 2

def square(n):
    return n * n

def pentagonal(n):
    return n * (3 * n - 1) / 2

def hexagonal(n):
    return n * (2 * n - 1)

def heptagonal(n):
    return n * (5 * n - 3) / 2

def octagonal(n):
    return n * (3 * n - 2)


def generate(function, start, end):
    n = 1
    result = []
    current = triangle(n)
    while current < end:
        if current >= start:
            result.append(current)
        n += 1
        current = triangle(n)
    return result

def find_chain(numbers, last, length):
    global solution
    for i in xrange(6):
        print i, solution
        if solution[i] != 0:
            continue

        for j in xrange(len(numbers[i])):
            possible = True
            if numbers[i][j] in solution:
                possible = False
                break

            if possible and ((numbers[i][j] / 100) == (solution[last] % 100)):
                solution[i] = numbers[i][j]
                if length == 5:
                    if (solution[5] / 100) == (solution[i] % 100):
                        return True
                if find_chain(numbers, i, length + 1):
                    return True
        solution[i] = 0
    return False




def main():
    # solution = [0] * 6
    global solution
    all_numbers = map(lambda x: generate(x, 1000, 10000), [triangle, square,pentagonal,hexagonal,heptagonal, octagonal])
    for i in all_numbers:
        print i

    for i in all_numbers[-1]:
        solution[5] = i
        print i
        if find_chain(all_numbers, 5, 1):
            break
    print solution
    print ">> ", sum(solution)


if __name__ == '__main__':
    main()