class Solution:
    def wordPattern(self, pattern, s):
        d_symb, d_word, words = {}, {}, s.split()
        if len(words) != len(pattern): return False
        for symb, word in zip(pattern, words):
            if symb not in d_symb:
                if word in d_word: return False
                else:
                    d_symb[symb] = word
                    d_word[word] = symb
            elif d_symb[symb] != word: return False
        return True