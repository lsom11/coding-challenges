class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(num**0.5%1.0==0.0):
            return True
        else:
            return False