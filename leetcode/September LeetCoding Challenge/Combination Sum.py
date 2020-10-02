class Solution:
    def combinationSum(self, candidates, target):
        def BackTr(target, curr_sol, k):  
            if target == 0:
                self.sol.append(curr_sol)

            if target < 0 or k >= len(candidates):
                return

            for i in range(k, len(candidates)):
                BackTr(target - candidates[i], curr_sol + [candidates[i]], i)
        
        self.sol = []
        BackTr(target, [], 0)   
        return self.sol