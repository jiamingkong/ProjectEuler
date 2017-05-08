
import math

def compute():
	TURNS = 15
	# Dynamic programming
	ways = [[1]]
	for i in range(1, TURNS + 1):
		row = []
		for j in range(i + 1):
			temp = 0
			if j < i:
				temp = ways[i - 1][j] * i
			if j > 0:
				temp += ways[i - 1][j - 1]
			row.append(temp)
		ways.append(row)

	numer = 0
	for i in range(TURNS // 2 + 1, TURNS + 1):
		numer += ways[TURNS][i]
	denom = math.factorial(TURNS + 1)
	return str(denom // numer)


if __name__ == "__main__":
	print(compute())
