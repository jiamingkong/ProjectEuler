import numspell

def count_num(speller, number):
    return len(speller.spell(number).replace(" ", "").replace("-", ""))

def main():
    speller = numspell.Speller('en')
    result = 0
    for i in xrange(1, 1001):
        result += count_num(speller, i)
    print result

if __name__ == '__main__':
    main()
