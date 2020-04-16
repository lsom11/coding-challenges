class Solution:
    def checkValidString(self, s: str) -> bool:
        # balance of left parenthesis and right parenthesis
        leftBalance = rightBalance = 0
        n = len(s)
        for i in range(n):
            # if char is ( or * - we increment leftBalance value
            if s[i] in "(*":
                leftBalance += 1
            # else decrement it
            else:
                leftBalance -= 1
            # we check right balance value starting from the end (right side)
            if s[n-i-1] in "*)":
                rightBalance += 1
            else:
                rightBalance -= 1
            # if any balance goes negative we have the case where order of parenthesis is wrong
            # e.g. )(  -> leftBalance will be -1 and rightBalance will be -1 after first iteration
            # or ((( - leftBalance is OK, but rightBalance will be -1 after first iteration
            if leftBalance < 0  or rightBalance < 0:
                return False
        return True