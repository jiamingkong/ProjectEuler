from .Collatz import test_excessive_pattern
from .seq_generator import generate
from multiprocessing import Process, Queue

def find_excessive_generator(length):
    result = 0
    for i in generate("", "", 0, length):
        if test_excessive_pattern(i) != None:
            print(i)
            result += 2
        else:
            result += 1
    return result


if __name__ == '__main__':
    i = 20
    result = find_excessive_generator(i)
    print((i+1, find_excessive_generator(i)))
    f = open("ProjectEuler494.txt", "w")
    f.write(str(result))