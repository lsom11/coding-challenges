class Solution:
    def twoCitySchedCost(self, costs):
        FirstCity = [i for i,j in costs]
        Diff = [j - i for i,j in costs]
        return sum(FirstCity) + sum(sorted(Diff)[:len(costs)//2])