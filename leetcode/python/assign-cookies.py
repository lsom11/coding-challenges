class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        satisfied = 0
        while s and g:
            if s[-1] < g[-1]:
                g.pop()
            else:
                satisfied += 1
                s.pop()
                g.pop()
                print('cookies')
        return satisfied