class Solution(object):
    def numIslands(self, grid):
        islands_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islands_count += 1
                    self.callBFS(grid, i, j)

        return islands_count
    
    def callBFS(self, grid, i, j):
        print(i, j)
        # check boundaries
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        self.callBFS(grid, i + 1, j) # up
        self.callBFS(grid, i - 1, j) # down
        self.callBFS(grid, i, j + 1) # left
        self.callBFS(grid, i, j - 1) # right
        
        