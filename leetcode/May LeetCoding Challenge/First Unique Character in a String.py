from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct=OrderedDict()
        for i in range(len(s)):
            if s[i] in dct:
                dct[s[i]]=-1
            else:
                dct[s[i]]=i
        ans=-1
        for key in dct:
            if dct[key]!=-1:
                ans=dct[key]
                break
        return ans