class Solution(object):
    def maxSubArray(self, nums):
        windowSum = nums[0]
        maxSum = nums[0]
        
        for i in range(1,len(nums)):
            windowSum = max(windowSum+nums[i], nums[i])
            maxSum = max(windowSum, maxSum)
        return maxSum