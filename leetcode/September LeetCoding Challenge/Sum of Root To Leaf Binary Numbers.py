class Solution:
    def sumRootToLeaf(self, root):
        def dfs(node):
            if not node.left and not node.right: self.sum += node.val
            for child in filter(None, [node.left, node.right]):
                child.val += node.val * 2
                dfs(child)
          
        self.sum = 0
        dfs(root)
        return self.sum