def fib_generator(under):
    first = 0
    second = 1
    while second < under:
        yield second
        first, second = second, first + second

if __name__ == '__main__':
    print sum(filter(lambda x: x%2==0, fib_generator(4000000)))
        