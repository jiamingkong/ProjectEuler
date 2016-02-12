from datetime import datetime


def main():
    counter = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            if datetime(y, m, 1).weekday() == 6:
                counter += 1
    return counter

if __name__ == '__main__':
    print(main())
