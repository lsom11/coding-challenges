class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summed_nums = list()
        sum = 0
        for num in nums:
            summed_nums.append(num + sum)
            sum += num
        return summed_nums