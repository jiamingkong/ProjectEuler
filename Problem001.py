
def find_multiples(start, end, numbers):
    return filter(lambda x: any([x % i == 0 for i in numbers]), xrange(start, end))

if __name__ == '__main__':
    print sum(find_multiples(1, 1000, [3, 5]))
