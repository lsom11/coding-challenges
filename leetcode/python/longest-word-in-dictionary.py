class Solution:
    def longestWord(self, words: List[str]) -> str:
        # sort so decomposed version comes first
        words.sort()
        
        builtWords = set()
        result  = ""
        
        for word in words:
            substr = word[:-1]
            print(substr)
            # if length is 1 we can add to set or if the substr is in builtwords we can add
            if len(word) == 1 or substr in builtWords:
                # this check helps with words with same length, sorted alphabetically already
                if len(word) > len(result): result = word
                builtWords.add(word)
            
        return result
