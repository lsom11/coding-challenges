def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def helper(i, j):
            if i>=len(A) or j>=len(B):
                return 0
            
            at = None
            for ind in range(j, len(B)):
                if B[ind]==A[i]:
                    at = ind
                    break
        
            ans = 0
            if at!=None:
                ans = max(ans, 1+helper(i+1, at+1))
            ans = max(ans, helper(i+1, j))
            return ans
        
        return helper(0, 0)