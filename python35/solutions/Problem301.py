def compute():
	def count_reversibles(numdigits):
		if numdigits % 2 == 0:
			return 20 * 30**(numdigits // 2 - 1)
		elif numdigits % 4 == 3:
			return 100 * 500**((numdigits - 3) // 4)
		elif numdigits % 4 == 1:
			return 0
		else:
			raise AssertionError()

	ans = sum(count_reversibles(d) for d in range(2, 10))
	return str(ans)


if __name__ == "__main__":
	print(compute())
