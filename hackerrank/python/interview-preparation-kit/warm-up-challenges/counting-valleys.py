n = int(input())
steps = input()

valleys = 0
altitude = 0
above_sea_level = True

for step in steps:
    if step == 'U':
        altitude += 1
        if altitude == 0:
            above_sea_level = True
    elif step == 'D':
        altitude -= 1
    if altitude == -1 and above_sea_level:
        above_sea_level = False
        valleys += 1


print(valleys)
