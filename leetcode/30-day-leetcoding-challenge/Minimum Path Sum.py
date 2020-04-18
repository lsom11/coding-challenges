class Solution(object):
    def helper(self, x, y, grid, cost):
        M, N = len(grid), len(grid[0])
        if x == M or y == N:
            return float('inf')
        elif cost[x][y] != -1:
            return cost[x][y]
        else:
            right, down = self.helper(x,y+1,grid,cost), self.helper(x+1,y,grid,cost)
            cost[x][y] = min(right, down) + grid[x][y]
        return cost[x][y]
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        cost = [[-1]*N for _ in range(M)]
        cost[M-1][N-1] = grid[M-1][N-1]
        return self.helper(0, 0, grid, cost)