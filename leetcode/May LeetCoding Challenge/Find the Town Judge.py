class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if N == 1:
            # Quick response for small case
            return 1
        
        # first cell is dummy, just for the convenience of indexing start from 1 to N
        trust_score = [ 0 for _ in range(N+1) ]
        
        for p1, p2 in trust:
            
            # decrease one point from p1 when p1 trusts other people
            trust_score[p1] -=1
            
            # increase one point to p2 when p2 is trusted by others
            trust_score[p2] +=1
            
            
        
        for person in range(1, N+1):
            
            # town judge will be trusted by other N-1 people, and town judge trust nobody.
            if trust_score[person] == N-1:
                return person
        
        return -1