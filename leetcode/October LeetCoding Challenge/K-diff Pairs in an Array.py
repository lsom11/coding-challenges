class Solution:
    def findPairs(self, nums, k):
        count = Counter(nums)
        print(count)
        if k > 0:
            res = sum([i + k in count for i in count])
        else:
            res = sum([count[i] > 1 for i in count])
        return res