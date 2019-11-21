"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):

        output_arr = list()

        if root is None:
            return output_arr
        
        stack = [root]
        
        while len(stack):
            node = stack.pop()
            output_arr.append(node.val)
            
            for child in node.children:
                stack.append(child)
                
        
        return output_arr[::-1]