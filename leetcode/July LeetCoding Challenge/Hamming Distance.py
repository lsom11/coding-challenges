class Solution:
    def hammingDistance(self, x, y):
        Out, t = 0, x^y 
        while t:
            t, Out = t & (t-1), Out + 1
        return Out