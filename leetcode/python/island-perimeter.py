class Solution:
	def islandPerimeter(self, grid):
		total = 0
		m,n = len(grid),len(grid[0])
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					total += 4
					if 0<=i-1<m and grid[i-1][j] == 1:
						total -= 1
					if 0<=i+1<m and grid[i+1][j] == 1:
						total -= 1
					if 0<=j-1<n and grid[i][j-1] == 1:
						total -= 1
					if 0<=j+1<n and grid[i][j+1] == 1:
						total -= 1
		return total