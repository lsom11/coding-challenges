# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        l = len(arr)
        i = 0
        return self.checkpath(root, arr, l, i)
    
    def checkpath(self, root, arr, l, i):
        if root is None:
            return l ==0
        if (i == l-1) and (root.left == None and root.right == None) and (root.val == arr[i]): return True
        if (i<l) and (root.val == arr[i]):
            return (self.checkpath(root.left, arr, l, i+1) or (self.checkpath(root.right, arr, l, i+1)))