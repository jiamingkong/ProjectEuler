'''
Took the algorithm from here.

http://stackoverflow.com/questions/2049582/how-to-determine-a-point-in-a-triangle
'''

import csv


class point(object):

    def __init__(self, x, y):
        super(point, self).__init__()
        self.x = x
        self.y = y


def sign(p1, p2, p3):
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)


def main():
    original = point(0, 0)
    counter = 0
    with open('p102_triangles.txt', "r") as f:
        reader = csv.reader(f)
        for i in reader:
            a, b, c, d, e, f = i
            p1 = point(int(a), int(b))
            p2 = point(int(c), int(d))
            p3 = point(int(e), int(f))
            if point_in_triangle(original, p1, p2, p3):
                counter += 1
    return counter


def point_in_triangle(pt, v1, v2, v3):
    b1 = sign(pt, v1, v2) < 0.
    b2 = sign(pt, v2, v3) < 0.
    b3 = sign(pt, v3, v1) < 0.
    return ((b1 == b2) and (b2 == b3))


if __name__ == '__main__':
    print(main())
