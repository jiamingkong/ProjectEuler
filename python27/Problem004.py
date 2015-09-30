from itertools import product

def is_palindrome(x):
    return int(str(x)[::-1]) == x



def main():
    current = 0
    for i in filter(lambda x: is_palindrome(x[0] * x[1]),\
                    product(xrange(100,1000), xrange(100, 1000))):
        if i[0] * i[1] > current:
            current = i[0] * i[1]

    return current

if __name__ == '__main__':
    print main()