class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        diff1, diff2 = -1, -1
        A_letters = set()
        for i in range(len(A)):
            if A[i] != B[i]:
                if diff1 == -1:
                    diff1 = i
                elif diff2 == -1:
                    diff2 = i
                else:
                    return False # More than 2 different places between A & B
            A_letters.add(A[i])
        if diff1 != -1 and diff2 != -1: # There are 2 different places
            return A[diff1] == B[diff2] and A[diff2] == B[diff1]
        if diff1 != -1: # Only have 1 different place
            return False
        return len(A_letters) < len(A) # No different between A & B, check if A contains at least 1 duplicate letters.