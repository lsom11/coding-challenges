class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        sum = 0
        for char in s:
            if char == 'L': sum += 1
            else: sum -= 1
            if sum == 0: count += 1
        return count