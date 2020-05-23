class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m=len(A)
        n=len(B)
        i=0
        j=0
        result=[]
        while(i<m and j<n):
                lo=max(A[i][0],B[j][0])
                hi=min(A[i][1],B[j][1])
                if(lo<=hi):
                    result.append([lo,hi])
                if(A[i][1]<B[j][1]):
                    i+=1
                else:
                    j+=1
        return result