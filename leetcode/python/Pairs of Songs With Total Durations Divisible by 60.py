class Solution:
    def numPairsDivisibleBy60(self, time):
        d, T = Counter(), 60
        for t in time: d[t%T] += 1
        ans = sum(d.get(i,0)*d.get(T-i,0) for i in range(1, T//2))
        q1, q2 = d.get(0,0), d.get(T//2, 0)
        return ans + q1*(q1-1)//2 + q2*(q2-1)//2