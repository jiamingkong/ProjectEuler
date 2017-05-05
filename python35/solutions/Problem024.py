from itertools import permutations

things = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    counter = 0
    for i in permutations(things, 10):
        counter += 1
        if counter == 1000000:
            print(i)
            break

if __name__ == '__main__':
    main()
