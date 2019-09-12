# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        if root.val < val:
            if root.right != None:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        else:
            if root.left != None:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)

        return root
