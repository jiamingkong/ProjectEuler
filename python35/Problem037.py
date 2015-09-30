from Utilities.PrimeGenerator import PrimeGenerator, is_prime

def check_number(number):
    possible = True
    for i in truncate_gen(number):
        if not is_prime(i):
            possible = False
    return possible
    
def truncate_gen(number):
    str_number = str(number)
    for i in range(1, len(str_number)):
        yield int(str_number[i:])
        yield int(str_number[:-i])

def main():
    found = 0
    result = []
    for i in PrimeGenerator():
        if i < 10:
            continue
        if check_number(i):
            result.append(i)
            found += 1
        if found == 11:
            break

    print(result)
    print(">>", sum(result))


if __name__ == '__main__':
    main()