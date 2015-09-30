import os

def number_complete(filename):
    serial = __get_serial(filename)
    return "Problem{num}.py".format(num = "%03d"%serial)


def __get_serial(filename):
    _fn = filename.lower().split(".")[0].replace("problem", "")
    serial = int(_fn)
    return serial

def find_missing():
    current_max = -1
    found = []
    for i in file_yielder():
        c = __get_serial(i)
        if c > current_max:
            current_max = c
        found.append(c)
    for i in xrange(1,current_max + 1):
        if i not in found:
            print("Problem {n} missing!".format(n = i))


def file_yielder():
    for i in os.listdir(os.getcwd()):
        if i.endswith(".py") and i.startswith("Problem"):
            yield i


def rename_main():
    for i in file_yielder():
        os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), number_complete(i)))
        print(i, ">>", number_complete(i))

if __name__ == '__main__':
    rename_main()
    find_missing()