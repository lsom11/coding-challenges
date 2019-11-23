# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        stack = list()
        
        # base case
        if root is None:
            return True
        
        stack.append(root)
        
        while len(stack) > 0:
            node = stack.pop()
            if node.val != root.val:
                return False
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        return True