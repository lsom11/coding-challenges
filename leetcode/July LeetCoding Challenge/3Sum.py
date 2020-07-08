class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        nums = sorted(counter)
        ret = []
        for i, num in enumerate(nums):
            # case i. three numbers are the same - [0,0,0]
            if num==0:
                if counter[num] > 2:
                    ret.append([0, 0, 0])
            # case ii. two numbers are the same
            elif counter[num] > 1 and -2 * num in counter:
                ret.append([num, num, -2 * num])
            # case iii. not any of the three numbers are the same
            if num < 0:
                opposite = -num
                left = bisect_left(nums, opposite - nums[-1], i + 1)
                right = bisect_right(nums, opposite / 2, left)
                for a in nums[left:right]:
                    b = opposite - a
                    if b in counter and a!=b:
                        ret.append([num, a, b])
        return ret