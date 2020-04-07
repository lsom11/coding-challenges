class Solution(object):
    def countElements(self, arr):
        d = dict()
        for i in arr:
            d[i] = 1
        result = 0
        for x in arr:
            if x+1 in d:
                result +=1
        return result