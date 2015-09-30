def check_bin_palindrome(number):
    bin_code = bin(number)[2:]
    if bin_code[::-1] == bin_code:
        return True
    else:
        return False

def check_dec_palindrome(number):
    return str(number)[::-1] == str(number)

def check_double_palindrome(number):
    return check_bin_palindrome(number) and check_dec_palindrome(number)

def main():
    result = filter(check_double_palindrome, xrange(1,1000000,2))
    print result
    print sum(result)
        


if __name__ == '__main__':
    main()
