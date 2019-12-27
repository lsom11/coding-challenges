class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search problem
        if len(nums) == 0: return -1
        if len(nums) == 1: return nums[0]
    
        left = 0
        right = len(nums) - 1
        
        while left < right:
            print(left, right)
            midpoint = int(left + (right - left) / 2)
            # find condition - if mid less that nums youve found the rotation
            if midpoint > 0 and nums[midpoint] < nums[midpoint - 1]: 
                return nums[midpoint]
            # cut in half, but see where its not sorted, if edge is less than mid (left) its sorted
            elif nums[left] <= nums[midpoint] and nums[midpoint] > nums[right]:
                left = midpoint + 1
            else: right = midpoint - 1
                
            
        # edge case - boundaries end where we found it    
        return nums[left]