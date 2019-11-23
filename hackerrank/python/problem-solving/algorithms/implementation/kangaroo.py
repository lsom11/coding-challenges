# v1j + x1 = v2j + x2
# j = x2-x2 / v1-v2
# if x is a whole number and is greater than 0 we return yes


def kangaroo(x1, v1, x2, v2):
    if v1 == v2 and x1 == x2:
        return 'YES'
    elif v1 == v2:
        return 'NO'

    x = (x2-x1) / (v1-v2)
    if (x == round(x) and x > 0):
        return 'YES'
    else:
        return 'NO'
