
def all_same(a_list):
    return all(x == a_list[0] for x in a_list)

def test_number(x):
    return all_same([''.join(sorted(str(i * x))) for i in range(1,7)])

def main():
    x = 123456
    while True:
        if test_number(x):
            print(x)
            break
        else:
            x += 1

if __name__ == '__main__':
    main()