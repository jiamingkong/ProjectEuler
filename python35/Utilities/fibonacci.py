def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        #        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

#--- find the nth Fibonacci number----------------------------------------


def fibonacci(n):
    """
    Find the nth number in the Fibonacci series.  Example:

    >>>fibonacci(100)
    354224848179261915075
    Algorithm & Python source: Copyright (c) 2013 Nayuki Minase
    Fast doubling Fibonacci algorithm
http://nayuki.eigenstate.org/page/fast-fibonacci-algorithms
    """
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]

# Returns a tuple (F(n), F(n+1))


def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (2 * b - a)
        d = b * b + a * a
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
