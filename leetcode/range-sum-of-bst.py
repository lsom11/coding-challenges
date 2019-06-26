# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = 0
        stack = [root]
        if root is None:
            return False

        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    total += node.val
                if L < node.val:
                    stack.append(node.left)
                if R > node.val:
                    stack.append(node.right)

        return total
