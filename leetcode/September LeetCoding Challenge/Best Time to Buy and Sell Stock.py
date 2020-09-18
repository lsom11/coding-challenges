class Solution:
    def maxProfit(self, nums):
        ans, dp = 0, 0
        for i in range(0, len(nums)-1):
            q = nums[i+1] - nums[i]
            dp = max(dp + q, q)
            ans = max(ans, dp)
        return ans