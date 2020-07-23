class Solution:
    def singleNumber(self, nums):
        s = reduce(xor, nums)
        nz = s & (s-1) ^ s
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        return(num1, s ^ num1)