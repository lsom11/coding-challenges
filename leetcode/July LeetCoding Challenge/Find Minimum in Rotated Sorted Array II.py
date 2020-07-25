class Solution:
    def findMin(self, nums):
        def bin_dfs(start, end):
            if end - start <=  1:
                self.Min = min(nums[start], nums[end], self.Min)
                return

            mid = (start + end)//2
            if nums[end] <= nums[mid]:
                bin_dfs(mid + 1, end)
            if nums[end] >= nums[mid]:
                bin_dfs(start, mid)
        
        self.Min = float("inf")
        bin_dfs(0, len(nums) - 1)
        return self.Min