
def merge_the_tools(string, k):
    # get length by dividing length of string by k
    length = len(string)//k

    # loop through string
    for i in range(length):
        # init substring
        substring = ''
        # loop through string, slice from beginning in multiples of k
        for char in string[i * k: (i + 1) * k]:
            # keep going unless repeat char and add char to substring
            if char not in substring:
                substring += char
        # print the result
        print(substring)
