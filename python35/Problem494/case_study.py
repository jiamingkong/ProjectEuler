from Collatz import grow


def main():
    children = []
    target = []
    with open('31.txt', "r") as f:
        for i in f:
            if i.strip() != "-":
                children.append(i.strip())
                target.append(i.strip()[1:])
            else:
                break

    with open('30.txt', "r") as f:
        for i in f:
            print(i, sum(1 for cha in i if cha == "u"))
            for idx, j in enumerate(target):
                if j == i.strip():
                    print("\t+{suf}".format(suf=children[idx][0]))
            print("\n")


def read_file(filename):
    result = []
    with open(filename, "r") as f:
        for i in f:
            if i.strip() != "-":
                result.append(i.strip())
            else:
                break
    return result


def main_decimal():
    seqs = read_file('31.txt')
    for i in seqs:
        print(grow(16, i))


if __name__ == '__main__':
    main_decimal()
