class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m==n:
            return m
        
        while (m<n):
            n -= (n & -n)
        
        return n