class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = dict()
        for num in nums:
            if num in d:
                del d[num]
            else: d[num] = 1
        return d.keys()
