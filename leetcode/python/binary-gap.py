class Solution:
    def binaryGap(self, N: int) -> int:

        b_num = list(bin(N)[2:])

        if 1 == b_num.count('1'):
            return 0

        distance = 0
        max_distance = 0
        for char in b_num:
            if char == '1':
                max_distance = max(distance, max_distance)
                distance = 0
            else:
                distance += 1

        return max_distance + 1


s = Solution()
s.binaryGap(5)
s.binaryGap(6)
