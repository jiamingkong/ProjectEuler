from Utilities import PrimeGenerator


def compute():
	LIMIT = 10**8
	MOD = 1000000009
	ans = 1
	for p in PrimeGenerator(under = LIMIT):
		power = count_factors(LIMIT, p)
		ans *= 1 + pow(p, power * 2, MOD)
		ans %= MOD
	return str(ans)


# Returns the number of factors of p (prime) in factorial(n).
def count_factors(n, p):
	if n == 0:
		return 0
	else:
		return n // p + count_factors(n // p, p)


if __name__ == "__main__":
	print(compute())