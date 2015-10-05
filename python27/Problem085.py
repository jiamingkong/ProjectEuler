def count_rects(w,h):
    return w * (w + 1) * h * (h + 1) / 4

def main():
    w = 3000
    h = 1
    target = 2000000
    error = target
    area = 0
    while w > h:
        rect = count_rects(w,h)
        if error > abs(rect - target):
            error = abs(rect - target)
            area = w * h
        if rect > target:
            w -= 1
        else:
            h += 1
    return area

if __name__ == '__main__':
    print(main())
