class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
	    # subtract counts of corresponding words, keeping non-negative values
	    return not len(Counter(ransomNote) - Counter(magazine))