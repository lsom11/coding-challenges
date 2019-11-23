def pairs(k, arr):
    s = set(arr)
    total = 0

    for i in s:
       if i + k in s:
           total += 1
    return total
