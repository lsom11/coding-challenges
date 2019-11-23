def check_permutation(a, b):
    permutation = False
    dict = {}
    if (len(a) != len(b)):
        return permutation

    for char in a:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    for char in b:
        if char in dict:
            dict[char] -= 1
        else:
            print(permutation)
            return permutation

    if all(value == 0 for value in dict.values()):
        permutation = True

    print(permutation)
    return permutation


check_permutation('test', 'different')
check_permutation('test', 'estt')
check_permutation('abcd', 'd2cba')
check_permutation('dcw4f', 'dcw5f')
