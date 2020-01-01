# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is not None:
            print('not a root!')
            output = []
            depth = 0

            def trav(node, depth):
                depth += 1
                if len(output) < depth:
                    output.append([])
                output[depth - 1].append(node.val)
                if node.left is not None:
                    trav(node.left, depth)
                if node.right is not None:
                    trav(node.right, depth)
            trav(root, depth)
            return [sum(x)/len(x) for x in output]
        else:
            return []
