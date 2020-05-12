class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if (nums[m] != nums[m + 1]) ^ (m % 2):
                r = m 
            else:
                l = m
        return nums[r] if r == len(nums) - 1 or nums[r] != nums[r + 1] else nums[l] 