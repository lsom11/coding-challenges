# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getHeight(self, node):
        # if left and right return the max of the two, otherwise traverse only through one
        if node.left and node.right:
            return 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        elif node.left:
            return 1 + self.getHeight(node.left)
        elif node.right:
            return 1 + self.getHeight(node.right)
        # base case, if leaf return 1 and we're done
        else: return 1
    
    def maxDepth(self, root: TreeNode) -> int:
        # if no root return 0
        if root:
            return self.getHeight(root)
        return 0


s = Solution()
s.maxDepth([3,9,20,null,null,15,7]) # 3