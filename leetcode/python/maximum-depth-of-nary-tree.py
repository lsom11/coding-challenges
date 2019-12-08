"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node', level = 1) -> int:
        if not root:
            return 0

        res = level
        if root.children:
            for c in root.children:
                res = max(res, self.maxDepth(c,level+1))

        return res