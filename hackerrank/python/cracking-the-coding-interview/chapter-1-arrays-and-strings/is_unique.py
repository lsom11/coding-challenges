def is_unique(S):
    dict = {}
    unique = True
    for char in S:
        if char in dict:
            unique = False
        else:
            dict[char] = 1

    return unique
