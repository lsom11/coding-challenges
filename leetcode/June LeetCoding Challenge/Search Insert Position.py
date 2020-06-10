class Solution:
    def searchInsert(self, nums, target):
        return bisect.bisect_left(nums, target)