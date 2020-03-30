class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0: return 0
        
        valid_size = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                print(nums[valid_size])
                nums[valid_size] = nums[i]
                valid_size += 1
        
        return valid_size
        