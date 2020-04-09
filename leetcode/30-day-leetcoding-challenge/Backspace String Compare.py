class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S, T = self._helper(S), self._helper(T)
        return S == T
    
    def _helper(self,s):
        while "#" in s:
            i = s.index("#")
            s = s[:i-1] + s[i+1:] if i > 0 else s[i+1:]
        return s