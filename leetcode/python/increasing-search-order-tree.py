# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            # start with smallest numbers
            if node.left: inorder(node.left)
            # remove left nodes
            node.left=None
            # set node of current
            self.cur.right=node
            self.cur=node
            # traverse right side
            if node.right: inorder(node.right)
                
        ans=self.cur=TreeNode(None)
        inorder(root)
        return ans.right