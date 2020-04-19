class Solution:
      def search(self, nums: List[int], target: int) -> int:
        def helper(l,r):
            if l > r:
                return -1
            m = (r+l)//2
            if nums[m] == target:
                return m
             # follow left half if left is sorted and target is in its range or right is sorted but target not in its range
            if nums[l] <= target < nums[m] or (nums[m] <= nums[r]  and not nums[m] < target <= nums[r]):
                return helper(l,m-1)
            else: 
                return helper(m+1, r)
        return helper(0,len(nums)-1)