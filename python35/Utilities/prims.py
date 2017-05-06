def weight(ax, u, v):
    return ax[u][v]


def adjacent(ax, u):
    lx = []
    for x in range(len(ax)):
        if ax[u][x] > 0 and x != u:
            lx.insert(0, x)
    return lx


def extract_min(qx):
    q = qx[0]
    qx.remove(qx[0])
    return q


def decrease_key(qx, kx):
    for i in range(len(qx)):
        for j in range(len(qx)):
            if kx[qx[i]] < kx[qx[j]]:
                s = qx[i]
                qx[i] = qx[j]
                qx[j] = s


def prim(vx, ax, r):
    u = 0
    v = 0

    px = [None]*len(vx)

    kx = [999999]*len(vx)

    qx = [0]*len(vx)
    for u in range(len(qx)):
        qx[u] = vx[u]

    kx[r] = 0
    decrease_key(qx, kx)

    while len(qx) > 0:
        u = extract_min(qx)

        adj = adjacent(ax, u)
        for v in adj:
            w = weight(ax, u, v)

            if qx.count(v) > 0 and w < kx[v]:
                px[v] = u
                kx[v] = w
                decrease_key(qx, kx)
    return px

# ax = [[0,  4,  0,  0,  0,  0,  0,  8,  0],
#       [4,  0,  8,  0,  0,  0,  0, 11,  0],
#       [0,  8,  0,  7,  0,  4,  5,  0,  2],
#       [0,  0,  7,  0,  9, 14,  0,  0,  0],
#       [0,  0,  0,  9,  0, 10,  0,  1,  0],
#       [0,  0,  4, 14, 10,  0,  2,  0,  0],
#       [0,  0,  0,  0,  0,  2,  0,  1,  6],
#       [8, 11,  0,  0,  1,  0,  1,  0,  7],
#       [0,  0,  2,  0,  0,  0,  6,  7,  0]]

# vx = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# px = prim(vx, ax, 0)
# print(px)
# print(sum([i for i in px if i != None]))