class Solution:
    def twoSum(self, numbers, target):
        remainder_map = {}
        for idx, num in enumerate(numbers):
            # subtract from total
            residual = (target - num)
            # if the remainder is in the dict we're done, print the sorted indices
            if residual in remainder_map:
                return sorted([remainder_map[residual] + 1, idx + 1])
            # else store a copy of the remainder with the index for future use
            if not num in remainder_map:
                remainder_map[num] = idx


s = Solution()
s.twoSum([2, 7, 11, 15])  # [1, 2]
