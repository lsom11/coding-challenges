class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=""
        for i in range(0,len(s2)-len(s1)+1):
            m=s2[i:i+len(s1)]
            if Counter(m)==Counter(s1):
                return True
        return False