def main():
    d = 1
    n = 2
    for i in range(2, 101):
        _d = d
        c = (i%3 == 0) and 2 * int(i/3) or 1
        d = n
        n = c * d + _d
    print(sum(map(int, list(str(n)))))

if __name__ == '__main__':
    main()