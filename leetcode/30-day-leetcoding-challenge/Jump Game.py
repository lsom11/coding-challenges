class Solution:
    def canJump(self, nums: List[int]) -> bool:
        debit = 0
        for i in reversed(nums[:-1]):
            debit += 1
            if i - debit >= 0:
                debit = 0
        return debit <= 0