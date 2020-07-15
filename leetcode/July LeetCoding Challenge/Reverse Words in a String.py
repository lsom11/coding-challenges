class Solution:
    def reverseWords(self, s):       
        chars = [t for t in s]
        slow, n = 0, len(s)
        for fast in range(n):
            if chars[fast] != " " or (fast > 0 and chars[fast] == " " and chars[fast-1] != " "):
                chars[slow] = chars[fast]
                slow += 1
                
        if slow == 0: return ""       
        chars = chars[:slow-1] if chars[-1] == " " else chars[:slow]
        chars = chars[::-1]
        
        slow, m = 0, len(chars)
        for fast in range(m + 1):
            if fast == m or chars[fast] == " ":
                chars[slow:fast] = chars[slow:fast][::-1]
                slow = fast + 1
                
        return "".join(chars)