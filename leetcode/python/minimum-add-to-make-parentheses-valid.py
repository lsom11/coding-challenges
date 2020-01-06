class Solution(object):
    def minAddToMakeValid(self, S):
        stack = []
        # traverse and add to stack
        for parens in S:
            # if parens closed and open parens at top of stack, remove it, balanced
            if parens == ')' and stack and stack[-1] == '(':
                print(parens)
                stack.pop()
            # otherwise push to stack
            else:
                stack.append(parens)
        return len(stack)

class Solution:
    def minAddToMakeValid(self, S):
        # if balanced bracket remove it, return the length of the unbalanced bracket
        while '()' in S:
            S = S.replace('()', '')
        return len(S)