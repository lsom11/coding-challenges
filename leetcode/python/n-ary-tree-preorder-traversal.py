"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
PREORDER TRAVERSAL

Check if current node is empty or null
Display the data part of the root (or current)
Traverse the left
Traverse the right
"""

class Solution(object):
    def preorder(self, root):
        stack = list()
        output_arr = list()
        
        # base case
        if root is None:
            return output_arr
        
        stack.append(root)
        
        while(len(stack) > 0):
            node = stack.pop()
            output_arr.append(node.val)
            # preorder, need to reverse children so that first element gets popped first
            node.children.reverse()
            for child in node.children:
                stack.append(child)
        
        return output_arr