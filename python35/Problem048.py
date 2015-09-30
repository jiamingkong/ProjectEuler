# Oh another BigInt challenge.... I know Python can bruteforce it without a second thinking.

def trunc(number, digits):
    if len(str(number)) > digits:
        return number % (10**digits)
    else:
        return number

def lazy_exp(base, power, digits):
    counter = 1
    number = base
    while counter < power:
        number *= base
        number = trunc(number, digits)
        counter += 1

    return number

def main():
    result = 0
    for i in range(1,1001):
        result += lazy_exp(i,i,10)
        result = trunc(result, 10)
    print(result)


if __name__ == '__main__':
    main()