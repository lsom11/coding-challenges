class Solution(object):
    def findDuplicates(self, nums):
        for i in range(len(nums)):
            while i != nums[i] - 1 and nums[i] != nums[nums[i]-1]:
				nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        print[nums[it]]
        return [nums[it] for it in range(len(nums)) if it != nums[it] - 1]