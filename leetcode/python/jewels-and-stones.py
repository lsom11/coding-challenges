class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        d = dict()
        for char in S:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        for char in J:
            if char in d:
                count += d[char]
        return count
