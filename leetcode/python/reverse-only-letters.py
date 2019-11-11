class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = []
        for char in S:
            if char.isalpha():
                letters.append(char)
        string_builder = ''
        for char in S:
            if char.isalpha():
                string_builder += letters.pop()
            else:
                string_builder += char
        return string_builder