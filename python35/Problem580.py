from Utilities.PrimeGenerator import PrimeGenerator
from Utilities.MemCache import lru_cache_function
from Utilities.timeit import timeit
import numpy as np

'''
C(10^8)= 23272089
C(10^9)= 232721183
C(10^10)= 2327212928
C(10^11)= 23272130893
C(10^12)= 232721313487
C(10^13)= 2327213144648
C(10^14)= 23272131472160
C(10^15)= 232721314792035
'''



@lru_cache_function(max_size=10000000)
def get_f(i, n,m):
    # print(i)
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


@timeit
def get_f_faster(i, n):
    m = np.sqrt(n)
    return get_f(i, n, m)


@timeit
def count_prime(under):
    counter = 0
    for i in PrimeGenerator(under=under):
        counter += 1
    return counter

if __name__ == '__main__':
    for i in [1e8,1e9,1e10, 1e11, 1e12, 1e13, 1e14, 1e15, 1e16]:
        main(i)
    # main(1e16)

    # print(get_f(1, 1e12, np.sqrt(1e12)))
    # print(get_f(7, 1e7, np.sqrt(1e7)))
    # print(get_f_faster(7, 1e7))
    # print(get_f_faster(7, 1e8))
    # print(get_f_faster(7, 1e9))
    # print(get_f_faster(7, 1e10))
    # print(get_f_faster(9999837, 1e16))

    # print(count_prime(1e8))
    # print(count_prime(1e4))
    # print(count_prime(1e5))
    # print(count_prime(1e8))