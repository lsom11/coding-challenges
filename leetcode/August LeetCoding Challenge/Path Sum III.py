class Solution:
    def cumSum(self, root):
        self.n += 1
        for child in filter(None, [root.left, root.right]):
            child.val += root.val
            self.cumSum(child)
                
    def dfs(self, root, sum):
        if not root: return None
        
        self.count[root.val + sum] += 1
        self.result += self.count[root.val]
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)
        self.count[root.val + sum] -= 1
 
    def pathSum(self, root, sum):
        if not root: return 0
        
        self.n, self.result, self.count = 0, 0, defaultdict(int)
        self.cumSum(root)
        self.count[sum] = 1
        self.dfs(root, sum)
        return self.result  - self.n*(sum == 0) 