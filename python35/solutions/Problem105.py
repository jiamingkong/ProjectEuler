import pdb
import itertools
import csv

class DispersionError(Exception):
    pass

def test_special_sum(b):
    '''
        test set b for special_sum
    '''
    b = list(b)
    s = set(b)
    try:
        if len(s) < len(b):
            raise DispersionError('NOT ENOUGH')
        b.sort()
        for i in range(1,len(b)//2+1):
            if sum(b[:i+1]) <= sum(b[-i:]):
                raise DispersionError('too much')
        for i in range(2,len(b)//2+1):
            for c in itertools.combinations(b,i):
                sumc = sum(c)
                d = list(s-set(c))
                d.sort()
                for e in itertools.combinations(d,i):
                    sume = sum(e)
                    if sume == sumc:
                        raise DispersionError('not enough')
                    #if sumc < sume:
                    #    break
    except DispersionError as yuk:
        return (0,b,)
    else:
        return(sum(b),b,)


def main():
    filename = "p105_sets.txt"
    sum = 0
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for i in reader:
            b = [int(j) for j in i]
            result, _ = test_special_sum(b)
            sum += result
        print(sum)
            # print(i)
            # print(test_special_sum([int(j) for j in i]))
            # pdb.set_trace()

if __name__ == '__main__':
    main()