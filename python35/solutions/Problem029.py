from sets import Set


def main():
    result = Set()
    for a in range(2, 101):
        for b in range(2, 101):
            result.add(a**b)

    return len(result)


if __name__ == '__main__':
    print(main())
