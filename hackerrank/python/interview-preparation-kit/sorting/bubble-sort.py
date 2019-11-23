def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                count += 1
                a[j], a[j + 1] = a[j + 1], a[j]

    print('Array is sorted in ' + str(count) + ' swaps.')
    print('First Element: ' + str(a[0]))
    print('Last Element: ' + str(a[-1]))
