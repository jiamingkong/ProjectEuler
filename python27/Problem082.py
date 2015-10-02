import numpy as np


def prepare(file):
    result = []
    with open(file, "r") as f:
        for i in f:
            result.append([int(x) for x in i.strip().split(",")])
    return np.asarray(result)


def main(file):
    numbers = prepare(file)
    w, h = numbers.shape
    solution = numbers[:, -1]

    for i in range(w-2, -1, -1):
        solution[0] += numbers[0, i]
        for j in range(1, w):
            solution[j] = min(
                [solution[j-1] + numbers[j, i], solution[j] + numbers[j, i]])

        for j in range(w-2, -1, -1):
            solution[j] = min([solution[j], solution[j+1] + numbers[j, i]])

    return min(solution)


if __name__ == '__main__':
    file = "resource_p82_matrix.txt"
    print main(file)
