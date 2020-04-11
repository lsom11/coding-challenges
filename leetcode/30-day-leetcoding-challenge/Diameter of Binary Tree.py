# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def dfs(v):
            if not v:
                return (0, 0)
            
            left_max_len, left_max_diam = dfs(v.left)
            right_max_len, right_max_diam = dfs(v.right)

            node_max_len = max(left_max_len, right_max_len) + 1
            node_max_diam = max(left_max_len + right_max_len, left_max_diam, right_max_diam)
            return (node_max_len, node_max_diam)
        
        _, root_max_diam = dfs(root)
        return root_max_diam