def find_pythagorean(total):
    for i in range(1, total-1):
        for j in range(i,total-i-1):
            if i * i + j * j == (total - i - j) ** 2:
                return i * j * (total - i - j)

if __name__ == '__main__':
    print(find_pythagorean(1000))