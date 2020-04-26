from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None) # This memoize the function calls with arguments and returned results so that you can call again later on with same parameters without incurring additional computation. Max_size specifies that our LRU cache can grow without bounds.
        def memo_solve(ptr1, ptr2):
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0
            
            # Case 1
            if text1[ptr1] == text2[ptr2]:
                return 1 + memo_solve(ptr1+1, ptr2+1)
        
            # Case 2
            else:
                return max(memo_solve(ptr1+1, ptr2), memo_solve(ptr1,ptr2+1))
                            # ^ Case 2 - Option 1           ^ Case 2 - Option 2
        return memo_solve(0,0) # Start the recursion stack from str1[0] and str2[0]		