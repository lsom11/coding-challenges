class Solution(object):
    def arrayPairSum(self, nums):
        N = 2
        sorted_nums = sorted(nums)
        pairs = [sorted_nums[n:n+N] for n in range(0, len(sorted_nums), N)]
        sum = 0
        for pair in pairs:
            first, second = pair
            print(first, second)
            sum += min(first, second)
        return sum

test = Solution()
test.arrayPairSum([[1,4,3,2]]) # 4