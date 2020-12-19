class Solution:
    def fourSumCount(self, A, B, C, D):
        Cnt1, Cnt2, ans = Counter(), Counter(), 0
        for a, b in product(A, B):
            Cnt1[a + b] += 1
            print(Cnt1)
        for c, d in product(C, D):
            Cnt2[c + d] += 1
            
        for val in Cnt1:
            if -val in Cnt2:
                ans += Cnt1[val]*Cnt2[-val]
                
        return ans