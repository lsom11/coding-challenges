class Solution:
    def helper(self, root):
        if not root or root.val == self.val: 
            self.Found = root
            return root
        
        if root.val < self.val:
            return self.helper(root.right)
        
        if root.val > self.val:
            return self.helper(root.left)
    
    def searchBST(self, root, val):
        self.val = val
        self.Found = None
        self.helper(root)
        return self.Found