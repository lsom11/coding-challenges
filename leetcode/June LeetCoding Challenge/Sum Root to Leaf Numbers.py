class Solution:
    def sumNumbers(self, root):
        if not root: return 0
        
        if not root.left and not root.right:
            return int(root.val)
        
        if root.left: root.left.val = 10*root.val + root.left.val
        if root.right: root.right.val = 10*root.val + root.right.val
            
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)