import os

def number_complete(filename):
    _fn = filename.lower().split(".")[0].replace("problem", "")
    serial = int(_fn)
    return "Problem{num}.py".format(num = "%03d"%serial)

for i in os.listdir(os.getcwd()):
    if i.endswith(".py") and i.startswith("Problem"):
        os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), number_complete(i)))

        print i, ">>", number_complete(i)
        # S = raw_input()