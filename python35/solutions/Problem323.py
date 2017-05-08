import itertools


def compute():
	def cdf(n):
		return (1 - 0.5**n)**32 if n >= 0 else 0.0

	ans = 0.0
	for n in itertools.count(1):
		p = cdf(n) - cdf(n - 1)
		if p < 1e-20:
			break
		ans += n * p
	return "{:.10f}".format(ans)


if __name__ == "__main__":
	print(compute())
