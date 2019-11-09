class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates_list = list()
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for key, val in d.items():
            if val > 1:
                duplicates_list.append(key)
        return duplicates_list