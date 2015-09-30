def twoSum(num, target):
    _dict = {}
    for i in range(len(num)):
        x = num[i]
        if target-x in _dict:
            return (_dict[target-x] + 1, i + 1)
        _dict[x] = i


if __name__ == '__main__':
    print(twoSum([1,2,3,4,5,6], 12))