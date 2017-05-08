

limit = 1000

def main(limit):
    n = 21
    count = 0
    while n < limit:
        if n%1000000 == 1:
            print(n)
        reverse = 0
        temp_n = n

        power_of_ten = 1
        while temp_n:
            reverse = reverse * 10 + temp_n % 10
            temp_n /= 10
            if temp_n:
                power_of_ten *= 10

        if int(reverse) & 0x1:
            n += power_of_ten
            continue

        sum = n + reverse

        while sum & 0x1:
            sum /= 10

        if sum == 0:
            count += 2

        n += 2

    return count

if __name__ == '__main__':
    main(1000)
