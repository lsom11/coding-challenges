import math

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_counts = [0] * 26
        for i in text:
            char_counts[ord(i) - ord('a')] += 1
        
        min_count = char_counts[1] # b
        min_count = min(min_count, char_counts[0]) # a
        min_count = min(min_count, char_counts[11] / 2) # l
        min_count = min(min_count, char_counts[14] / 2) # o
        min_count = min(min_count, char_counts[13]) # n
        
        return math.floor(min_count)

class SolutionTwo:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count('b'),text.count('a'),text.count('l')//2,text.count('o')//2,text.count('n'))