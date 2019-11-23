def print_rangoli(size):
    alpha = string.ascii_lowercase

    L = []
    # loop through size
    for i in range(size):
        # create link from start of loop to end of loop
        s = "-".join(alpha[i:size])
        # append link to L starting from end working way to beginning of s and adding s without first index
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
