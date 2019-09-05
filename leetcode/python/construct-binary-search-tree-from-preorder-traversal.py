# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def bstFromPreorder(self, preorder):
        plen = len(preorder)
        if plen == 0:
            return None

        root = TreeNode(preorder[0])
        cur = root
        stack = [root]

        for i in range(1, plen):
            # next less than current we append current to stack and assign next to left
            if preorder[i] < cur.val:
                stack.append(cur)
                cur.left = TreeNode(preorder[i])
                cur = cur.left
            # if stack is empty we set next to right (has to be greater than cur)
            elif not stack:
                cur.right = TreeNode(preorder[i])
                cur = cur.right
            else:
                # if the last item in the stack is less than next we remove it and set next to right
                while stack and stack[-1].val < preorder[i]:
                    cur = stack.pop()
                cur.right = TreeNode(preorder[i])
                cur = cur.right
        return root


s = Solution()
s.bstFromPreorder([8, 5, 1, 7, 10, 12])  # [8,5,10,1,7,null,12]
