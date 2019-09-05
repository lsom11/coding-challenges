class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        return min(d, key=lambda k: d[k])


s = Solution()
s.singleNumber([2, 2, 1])  # 1
