if __name__ == '__main__':
    s = input()

    isAlphaNum = any(x.isalnum() for x in s)
    isAlpha = any(x.isalpha() for x in s)
    isDigit = any(x.isdigit() for x in s)
    isLower = any(x.islower() for x in s)
    isUpper = any(x.isupper() for x in s)
    print(isAlphaNum)
    print(isAlpha)
    print(isDigit)
    print(isLower)
    print(isUpper)
