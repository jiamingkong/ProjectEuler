from Utilities.PrimeGenerator import totient


def main():
    max_found = None
    max_value = -1
    for i in range(1, 1000001):
        phi = totient(i)
        if i * 1.0 / phi > max_value:
            max_found = i
            max_value = i * 1.0 / phi

    print(max_found)

if __name__ == '__main__':
    main()
