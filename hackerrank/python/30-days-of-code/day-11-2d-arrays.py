if __name__ == '__main__':
    arr = []

    def _get_hourglass_sum(matrix, row, col):
        sum = 0
        # get 7 elements that make up sum
        sum += matrix[row - 1][col-1]
        sum += matrix[row - 1][col]
        sum += matrix[row - 1][col + 1]
        sum += matrix[row][col]
        sum += matrix[row + 1][col-1]
        sum += matrix[row + 1][col]
        sum += matrix[row + 1][col + 1]
        return sum

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # this is the minimum sum possible (9 * 7)
    max_hourglass_sum = -63
    # row 0 and row n - 1 cant have hourglasses
    for i in range(1, 5):
        for j in range(1, 5):
            current_hourglass_sum = _get_hourglass_sum(arr, i, j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum

    print(max_hourglass_sum)
