# another cheating in python

def main():
    a = str(2**1000)
    return sum(map(int, list(a)))

if __name__ == '__main__':
    print(main())
