from Utilities.PrimeGenerator import PrimeGenerator
from Utilities.MemCache import lru_cache_function
from Utilities.timeit import timeit
import numpy as np



@lru_cache_function(max_size=10000000)
def get_f(i, n,m):
    result = int((n / i / i + 3) / 4)
    for j in range(3, int(m /i+1), 2):
        result -= get_f(i*j, n, m)
    return result

@timeit
def main(n):
    m = int(np.sqrt(n))
    ans = get_f(1, n, m)
    gen = PrimeGenerator(under=m)
    for i in gen:
        if i%4==3:
            ans += get_f(i,n,m)

    print("answer = {i}".format(i=ans))

if __name__ == '__main__':
    # for i in [1e7,1e8,1e9,1e10,1e11,1e12]:
    #     main(i)
    main(1e16)