from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):

        d = OrderedDict()
        for i in range(len(s)):
            try:
                if d[s[i]]:
                    d[s[i]]+=1
            except:
                d[s[i]]=1
        for k,v in d.items():
            if v == 1:
                return s.index(k)
        return -1