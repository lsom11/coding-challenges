# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
            self.a=self.b=0 # a keeps track of position of x and b of y
            def dfs(node,pos):
                if not node : return 
                if node.val == x : self.a=pos # stores the positions of x
                if node.val == y : self.b=pos # stores the positions of y
                dfs(node.left,pos*2),dfs(node.right,pos*2+1) 
            dfs(root,1)
            return self.a//2 != self.b//2 and int(log(self.a,2))==int(log(self.b,2))