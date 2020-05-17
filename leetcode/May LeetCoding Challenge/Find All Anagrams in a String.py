class Solution:
    
    # Solution 1 : Sliding Window, Hash Table
    def findAnagrams(self, s, p):
        cnt_p = Counter(p); n = len(s); m = len(p); res = []
        for i in range(n-m+1):
            if i == 0: cnt_s = Counter(s[:m])
            else:
                prev = s[i-1]; curr = s[i+m-1]
                cnt_s[prev] -= 1; cnt_s[curr] += 1
                if cnt_s[prev] == 0: del cnt_s[prev]
            if cnt_s == cnt_p: res.append(i)
        return res        