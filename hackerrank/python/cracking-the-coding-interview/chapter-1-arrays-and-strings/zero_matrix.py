import unittest


class ZeroMatrixSolution:
    # O(N²)
    @staticmethod
    def zero_matrix(matrix):
        # all rows have same len, all cols have same length
        row = [False] * len(matrix)
        column = [False] * len(matrix[0])

        # check for 0s, set row or column to true accordingly
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    column[j] = True

        # loop through row and column, if true mutate matrix to 0 for that row and column
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == True or column[j] == True:
                    matrix[i][j] = 0

        return matrix


class TestStringCompression(unittest.TestCase):
    def setUp(self):
        pass

    def test_zero_matrix(self):
        self.assertEqual(ZeroMatrixSolution.zero_matrix([[1, 2, 3],
                                                         [1, 5, 0],
                                                         [7, 8, 9]]), [[1, 2, 0], [0, 0, 0], [7, 8, 0]])


if __name__ == '__main__':
    unittest.main()
