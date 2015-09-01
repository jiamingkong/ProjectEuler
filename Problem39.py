def check_right_angle(a,b,c):
    return a * a + b * b == c * c


def generate_sides(perimeter):
    for a in xrange(1,perimeter / 2):
        for b in xrange(a+1, perimeter / 2):
            c = perimeter - a - b
            yield a, b, c

def main():
    max_found = 0
    max_p = None
    for p in xrange(1, 1001):
        result = 0
        for a,b,c in generate_sides(p):
            if check_right_angle(a,b,c):
                result += 1
        if result > max_found:
            max_p = p
            max_found = result

    print max_p

if __name__ == '__main__':
    main()