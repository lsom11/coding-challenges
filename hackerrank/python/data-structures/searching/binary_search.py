def binary_search(arr, elem):
    left = 0
    right = len(arr) - 1

    # while the left is less than the right we continue the loop, this search is in O(log n) time assuming the array is already sorted
    while left < right:
        mid = left + (right - 1) / 2

        if arr[mid] == elem:
            return mid

        if arr[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1

    return -1
