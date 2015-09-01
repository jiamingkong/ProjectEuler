from sets import Set


def trial(number):
    result = ''
    current = 1
    while len(result) < 9:
        result += str(number * current)
        current += 1
    if len(result) > 9:
        return False, -1
    if len(Set(list(result))) == 9 and '0' not in result:
        return True, int(result)
    else:
        return False, -1


def main():
    max_found = -1
    for i in xrange(1, 9999):
        work, result = trial(i)
        if work:
            print i, result
            if max_found < result:
                max_found = result
    print max_found

if __name__ == '__main__':
    main()
