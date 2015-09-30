def factorial(n):
    result =1
    while n > 1:
        result *= n
        n -= 1
    return result

def main():
    number = factorial(100)
    return sum(map(int, list(str(number))))

if __name__ == '__main__':
    print(main())