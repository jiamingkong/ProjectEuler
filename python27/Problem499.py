from math import exp

def main():
    k = 15
    x = 1
    return 1.0 - exp(- k * x)

if __name__ == '__main__':
    print(main())