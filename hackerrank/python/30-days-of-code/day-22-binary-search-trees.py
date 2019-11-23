
def getHeight(self, root):
    if root:
        left = 0
        right = 0
        if root.left:
            left = 1 + self.getHeight(root.left)
        if root.right:
            right = 1 + self.getHeight(root.right)
        return max(left, right)
    else:
        return 0
