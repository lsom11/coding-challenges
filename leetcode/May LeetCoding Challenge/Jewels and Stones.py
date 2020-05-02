class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        
        for l1 in J:
            for l2 in S:
                if l1 == l2:
                    res += 1
        
        return res