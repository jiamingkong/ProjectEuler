'''
There are definitely some easier ways to calculate the number of paths available if you are going diagonal. 2 * 2, 3 * 3, 20 * 20, however those methods will fail when you have something like 19 *20. I will write a general purpose function here.
'''

def main(a, b):
    grid = {}
    for i in range(0, a+1):
        grid[(i,0)] = 1
    for j in range(0, b+1):
        grid[(0,j)] = 1
    grid[(a-1,b-1)] = 0
    for i in range(1,a+1):
        for j in range(1,b+1):
            grid[(i,j)] = grid[(i-1, j)] + grid[(i, j-1)]
    return grid[(a,b)]

if __name__ == '__main__':
    print(main(20, 20))
    # print main(19, 20)