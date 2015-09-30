from itertools import product
from Utilities.gcd import fraction_reduce

def cancel(a,b):
    str_a, str_b = list(str(a)), list(str(b))
    for i in str_a:
        if i == '0':
            continue
        if i in str_b:
            str_a.remove(i)
            str_b.remove(i)
            x, y = int(''.join(str_a)), int(''.join(str_b))
            return x, y
    return 0, 1
            

def digit_cancelling(tuple):
    a, b = tuple
    if a >= b:
        return False
    x, y = cancel(a, b)
    if x == 0 or y == 0:
        return False
    if a * 1.0 / b == x * 1.0 / y:
        return True
    else:
        return False


def main():
    _a, _b = 1, 1
    for a, b in filter(digit_cancelling, product(xrange(11,100), xrange(11,100))):
        _a *= a
        _b *= b

    print _a, _b
    print ">> ", fraction_reduce(_a, _b)
    

if __name__ == '__main__':
    main()