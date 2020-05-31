class Solution:
  def minDistance(self, word1, word2):
    word1, word2 = "!" + word1, "!" + word2
    n_1, n_2 = len(word1), len(word2)
    dp = [[0] * n_2 for _ in range(n_1)]

    for i_1 in range(n_1): dp[i_1][0] = i_1
    for i_2 in range(n_2): dp[0][i_2] = i_2

    for i_1 in range(1, n_1):
      for i_2 in range(1,n_2):
        Cost = (word1[i_1] != word2[i_2])
        dp[i_1][i_2] = min(dp[i_1-1][i_2] + 1, dp[i_1][i_2-1] + 1, dp[i_1-1][i_2-1] + Cost)

    return int(dp[-1][-1])