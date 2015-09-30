def find_reminder(denom, nom):
    return denom / nom, denom % nom

def enlarge(remainder, nom):
    counter = 0
    while remainder < nom:
        counter += 1
        remainder *= 10
    return remainder, counter - 1

def find_cycle(nom):
    length = 0
    denom = 1
    remainder = None
    met_remainder = []
    while remainder != 1:
        denom, counter = enlarge(denom, nom)
        div, remainder = find_reminder(denom, nom)
        if remainder == 0:
            break
        length += counter + 1
        if remainder in met_remainder:
            break
        else:
            met_remainder.append(remainder)
        denom = remainder
    return length



if __name__ == '__main__':
    max_met = 0
    max_idx = None
    for i in range(2, 1000):
        curr = find_cycle(i)
        if max_met < curr:
            max_met = curr
            max_idx = i
    print(max_idx, max_met)
