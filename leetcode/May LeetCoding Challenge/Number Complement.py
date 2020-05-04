class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        bit = 1
        while temp:
            num = num ^ bit
            bit = bit << 1
            temp = temp >> 1
        return num