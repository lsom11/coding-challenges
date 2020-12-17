class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        output = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                print(output)
                output += 1
        return output