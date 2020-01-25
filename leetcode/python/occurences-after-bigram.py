class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        word_list = list()
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                word_list.append(words[i + 2])
        return word_list    