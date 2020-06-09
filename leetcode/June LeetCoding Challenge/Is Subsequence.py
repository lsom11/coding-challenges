class Solution:
    def isSubsequence(self, s, t):
        s, t = "!" + s, "!" + t
        m, n = len(s), len(t)
        dp = [[0] * m for _ in range(n)] 
        for i in range(n): dp[i][0] = 1
   
        for i,j in product(range(1, n), range(1, m)):
            if s[j] == t[i]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
                    
        return dp[-1][-1]