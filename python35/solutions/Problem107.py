from Utilities.prims import prim
import os
import csv

cwd = os.getcwd()

resource_file = os.path.join(cwd, "resources", "problem107", "p107_network.txt")

def to_int(x):
    if x == "-":
        return 0
    else:
        return int(x)

if __name__ == '__main__':
    ax = []
    with open(resource_file) as f:
        reader = csv.reader(f)
        for i in reader:
            ax.append(
                [to_int(j) for j in i]
                )

    vx = list(range(len(ax[0])))
    px = prim(vx, ax, 0)
    original_network = sum([sum(i) for i in ax]) / 2
    # that thing is symmetry...
    current_network = sum([i for i in px if i != None])
    # the minimum spanning tree is generated...
    print(original_network)
    print(current_network)
    print(original_network - current_network)