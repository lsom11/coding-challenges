class Solution(object):
    def findSpecialInteger(self, arr):
        if len(arr) == 1: return arr[0]
        
        l = len(arr) * 0.25
        d = dict()
        for num in arr:
            if num in d:
                d[num] += 1
                if d[num] > l: return num
            else: d[num] = 1
        
        
        