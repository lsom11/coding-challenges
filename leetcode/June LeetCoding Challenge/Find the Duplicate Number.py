class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if num in d: return num
            else: d[num] = 1