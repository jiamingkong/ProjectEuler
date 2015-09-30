from sets import Set

def pandigit(a, b):
    result = a * b
    s = str(a) + str(b) + str(result)
    if '0' in s:
        return False
    if len(s) == 9 and len(Set(s)) == 9:
        return True

    return False

def main():
    result = Set()
    for i in range(100):
        for j in range(10000):
            if pandigit(i,j):
                result.add(i * j)
                print(i, j, i * j)
    print("Sum >>", sum(list(result)))


if __name__ == '__main__':
    main()