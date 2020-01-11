class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        while len(stones) > 1:
            stones.sort()
            x, y = stones[-2], stones[-1]
            stones = stones[:-2]
       
            if x != y:
                stones.append(y - x)
                
        return stones[0] if stones else 0