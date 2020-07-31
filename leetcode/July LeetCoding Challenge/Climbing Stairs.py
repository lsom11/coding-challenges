class Solution:
    def climbStairs(self, n):
        dp = (1, 1)
        for i in range(n-1):
            dp = (dp[1], dp[0] + dp[1])
        return dp[1]