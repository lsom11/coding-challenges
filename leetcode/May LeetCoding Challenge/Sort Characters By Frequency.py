class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(c*x for x,c in Counter(s).most_common())