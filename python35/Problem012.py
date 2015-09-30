from Utilities.PrimeFactor import num_of_divisors

def num_generator():
    start = 1
    result = 0
    while True:
        result += start
        start += 1
        yield result

def main():
    for i in num_generator():
        if num_of_divisors(i) >= 500:
            print(i)
            break

if __name__ == '__main__':
    print(main())