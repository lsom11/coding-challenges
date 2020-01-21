from collections import defaultdict

class Solution(object):
    def uncommonFromSentences(self, A, B):
        word_list = defaultdict()
        for word in A.split(" "):
            word_list[word] = word_list.get(word, 0)+1
        for word in B.split(" "):
            word_list[word] = word_list.get(word, 0)+1

        
        return [key for key in word_list.keys() if word_list[key] == 1]
        