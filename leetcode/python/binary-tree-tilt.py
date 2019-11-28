# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSumAndTilt(self, root):
        if not root:
            return 0, 0
        leftSum, leftTilt = self.findSumAndTilt(root.left)
        rightSum, rightTilt = self.findSumAndTilt(root.right)
        return root.val + leftSum + rightSum, leftTilt + rightTilt + abs(leftSum - rightSum)

    def findTilt(self, root):
        return self.findSumAndTilt(root)[1]
