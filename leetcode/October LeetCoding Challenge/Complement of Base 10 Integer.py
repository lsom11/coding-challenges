class Solution:
    def bitwiseComplement(self, N):
         return (1<<(len(bin(N)) - 2)) - 1 - N