def main():
    count = 0
    factorial = 1
    for n in range(2, 31):
        count = count * n + (2 ** (n-1) - 1) * factorial
        factorial = factorial * n
    print("%.2f" % (count/factorial))

if __name__ == '__main__':
    main()
