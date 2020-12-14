class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 1, 0
        for i in range(n*n):
            matrix[y][x] = i + 1
            if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[y+dy][x+dx] != 0:
                dx, dy = -dy, dx
            x, y = x + dx, y + dy
        return matrix