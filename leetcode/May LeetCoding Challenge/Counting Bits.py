class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)
        for i in range(num + 1):
            result[i] = result[i // 2] + i % 2
        return result