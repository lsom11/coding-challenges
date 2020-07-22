class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        d = {}
        def dfs(node, level):
            
            if level not in d:
                d[level] = []
            d[level].append(node.val)
            
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
                
        if root:
            dfs(root, 1)
        
        res = []
        for i in d:
            if i % 2 == 0:
                d[i] = d[i][::-1]
            res.append(d[i])
        return res