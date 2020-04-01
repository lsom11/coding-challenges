class Solution(object):
    def singleNumber(self, nums):
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0)+1
        return min(d, key=d.get)