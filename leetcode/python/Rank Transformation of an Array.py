class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {}
        start = 1
        
        for each in sorted(arr):
            if each in rank:
                continue
            else:
                rank[each] = start
                start += 1
            
        return [rank[each] for each in arr]