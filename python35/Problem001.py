
def find_multiples(start, end, numbers):
    return [x for x in range(start, end) if any([x % i == 0 for i in numbers])]

if __name__ == '__main__':
    print(sum(find_multiples(1, 1000, [3, 5])))
