class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        n = len(s)
        dp_solution = [[] for _ in range(n)] + [[""]]
        dp = [0] * n + [1]
        
        for k in range(n):
            for j in range(k,-1,-1):
                if s[j: k + 1] in wordSet:
                    dp[k] = max(dp[k], dp[j-1])

        if dp[-2] == 0: return []

        for k in range(n):
            for j in range(k,-1,-1):
                if s[j: k + 1] in wordSet:
                    for sol in dp_solution[j-1]:
                        dp_solution[k].append(sol + " " + s[j: k + 1])
                        
        return [s[1:] for s in dp_solution[-2]]