class Solution:
    def subsets(self, nums):
        self.out = []
        self.dfs([-1],nums)
        return self.out

    def dfs(self, current, nums):
        self.out.append([nums[s] for s in current][1:])
        for i in range(current[-1] + 1, len(nums)):
            self.dfs(current + [i], nums)