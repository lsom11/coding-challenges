import unittest


class Solution:
    @staticmethod
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        indices_to_remove = []
        for idx, char in enumerate(S):
            if char == '(':
                if count != 0:
                    indices_to_remove.append(char)
                count += 1
            else:
                if count != 1:
                    indices_to_remove.append(char)
                count -= 1
        return ''.join(indices_to_remove)


Solution.removeOuterParentheses("(()())(())")  # "()()()"
