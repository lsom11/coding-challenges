n = int(input().strip())

# counter of current consecutive ones
current_ones = 0
# counter of max consecutive ones
max_ones = 0

# instead of converting to binary we use remainders to see last number of binary, go until n is less than 0
# converting to a binary - n % 2 // 2 and round down
while n > 0:
    remainder = n % 2

    if remainder == 1:
        current_ones += 1
        if current_ones > max_ones:
            max_ones = current_ones
    else:
        current_ones = 0

    # divide n by 2 and reset it
    n = n // 2

print(max_ones)
