
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        while i > 0 and arr[i - 1] > current:
            arr[i] = arr[i - 1]
            i -= 1
            arr[i] = current

    print(arr)

def main():
    insertion_sort([1, 2, 5, 4, 2])
    insertion_sort([20, 43, 22, 4, 2])
    insertion_sort([3, 2, 5, 4, 6])

if __name__ == '__main__':
    main()