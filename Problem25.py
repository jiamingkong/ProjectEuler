def unlimited_fib():
    a =0
    b =1
    counter = 1
    while True:
        yield (counter, b)
        a, b = b, a + b
        counter += 1

def main():
    for counter, number in unlimited_fib():
        if len(str(number)) == 1000:
            print counter
            break

if __name__ == '__main__':
    main()