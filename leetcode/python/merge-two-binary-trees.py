# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        # if val doesnt exist val becomes either t1 or t2, else null
        if not t1: return t2
        if not t2: return t1
        t1.val += t2.val
        # do same down left and right
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1
