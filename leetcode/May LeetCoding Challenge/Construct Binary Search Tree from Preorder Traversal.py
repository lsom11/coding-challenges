# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def help(root,val):
            if root:
                if val>root.val:
                    if root.right:
                        help(root.right,val)
                    else:
                        root.right=TreeNode(val)
                else:
                    if root.left:
                        help(root.left,val)
                    else:
                        root.left=TreeNode(val)
        root=TreeNode(preorder[0])
        for i in range(1,len(preorder)):
           help(root,preorder[i])
        return root