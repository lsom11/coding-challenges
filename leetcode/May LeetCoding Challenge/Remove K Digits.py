class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for ch in num:
            while k > 0 and len(stack) > 0 and int(stack[-1]) > int(ch):
                stack.pop()
                k -= 1
            stack.append(ch)
        
        while k > 0:
            stack.pop()
            k -= 1
        # print(stack)
        return "0" if len(stack) ==0 else str(int("".join(stack)))