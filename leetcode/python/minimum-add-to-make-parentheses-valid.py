class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        stack = []
        for s in S:
            # if left paren add to stack
            if s == '(':
                stack.append(s)
            # if not left paren but stack has values pop from stack
            elif len(stack) > 0:
                stack.pop()
            # otherwise increment by 1    
            else:
                count += 1
        return count + len(stack)