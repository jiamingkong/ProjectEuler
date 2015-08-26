def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def lcm(*numbers):
    """Return lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)