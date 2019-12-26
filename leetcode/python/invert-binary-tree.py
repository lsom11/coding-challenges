# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None: 
            return None 
        else:
            right = self.invertTree(root.left)
            left = self.invertTree(root.right)
            root.left = left
            root.right = right
        return root