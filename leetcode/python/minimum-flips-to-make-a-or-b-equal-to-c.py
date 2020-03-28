class Solution(object):
    def minFlips(self, a, b, c):
        ret = 0
        while (a or b or c):
            if (c & 1):
                if (not (a & 1) and not (b & 1)):
                    ret += 1
            else:
                if (a & 1):
                    ret += 1
                if (b & 1):
                    ret += 1
            a //= 2
            b //= 2
            c //= 2
        return ret