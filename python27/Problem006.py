if __name__ == '__main__':
    print sum(xrange(1,101)) ** 2 - sum(map(lambda x: x**2, xrange(1,101)))