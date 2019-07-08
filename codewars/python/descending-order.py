# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.


def Descending_Order(num):
    l = [x for x in str(num)]
    reverse_str = sorted(l, reverse=True)
    joined_str = ''.join(reverse_str)
    return int(joined_str)


Descending_Order(123456789)
Descending_Order(15)
