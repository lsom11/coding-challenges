def compareTriplets(a, b):
    a_total = 0
    b_total = 0

    for idx, val in enumerate(a):
        if val > b[idx]:
            a_total += 1
        elif val < b[idx]:
            b_total += 1

    return a_total, b_total
