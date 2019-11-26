# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        def dfs(node):
            if not node: return
            dfs(node.right)
            node.val += self.sum
            self.sum = node.val
            dfs(node.left)

        dfs(root)
        return root