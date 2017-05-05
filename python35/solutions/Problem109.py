


def run():
    res = 0
    singles = []
    doubles = []
    trebles = []

    for i in range(1, 21):
        singles.append(i)
        doubles.append(2 * i)
        trebles.append(3 * i)
    singles.append(25)
    doubles.append(50)
    scores = []
    scores += singles
    scores += doubles
    scores += trebles

    for s in doubles:
        if s < 100:
            res += 1
    for s1 in scores:
        for s2 in doubles:
            if s1 + s2 < 100:
                res += 1
    for i in range(len(scores)):
        for j in range(i, len(scores)):
            for s in doubles:
                if scores[i] + scores[j] + s < 100:
                    res += 1
    print(res)


if __name__ == '__main__':
    run()