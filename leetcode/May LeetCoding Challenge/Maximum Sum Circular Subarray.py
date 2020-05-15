class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(A):
            best = float("-inf")
            current = 0
            for n in A:
                current += n
                if current < n:
                    current = n
                if current > best:
                    best = current
            return best
    
        max_array = max(A)
        if max_array < 0:
            return max_array
        
        best_sum = kadane(A)
        total_sum = sum(A)
        worst_sum = kadane(map(lambda x: -x, A))
        
        return max(best_sum, total_sum + worst_sum)