class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        nums.sort(reverse = True)
        
        count = 0
        max_nums = list()
        for num in nums:
            if num not in max_nums:
                if count == 2:
                    return num
                else:
                    max_nums.append(num)
                    count += 1
        return max(nums)
                
                            
            