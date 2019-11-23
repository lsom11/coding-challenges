size, rotations = input().split()

# get num of rotations
rotations = int(rotations)

# split array into a list
array_to_rotate = [x for x in input().split()]

# start array from slice of length of rotations and end with remainder
print(' '.join(array_to_rotate[rotations:] + array_to_rotate[:rotations]))
