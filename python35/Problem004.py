from itertools import product

def is_palindrome(x):
    return int(str(x)[::-1]) == x



def main():
    current = 0
    for i in [x for x in product(range(100,1000), range(100, 1000)) if is_palindrome(x[0] * x[1])]:
        if i[0] * i[1] > current:
            current = i[0] * i[1]

    return current

if __name__ == '__main__':
    print(main())