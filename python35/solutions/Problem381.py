from Utilities import PrimeGenerator

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m




def S(p):
    return (3 * modinv((-8)%p, p)) % p

def main(n):
    return sum(S(p) for p in list(PrimeGenerator(under=n))[2:])

print(main(10**8))