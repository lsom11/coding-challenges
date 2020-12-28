class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) == len(set(nums)):
            return 0
        sum = 0
        for i,n in enumerate(nums):
            sum += nums[i:].count(n) -1
        print(sum)
        return sum