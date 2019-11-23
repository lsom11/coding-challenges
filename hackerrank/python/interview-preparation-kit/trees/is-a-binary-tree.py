""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(node):
    # create a stack and a pointer to prev not
    stack = []
    prev = None

    # if the node exists or the stack has items in it
    while node or stack:
        # if there is a node, append it to the stack and continue left
        while node:
            stack.append(node)
            node = node.left
        # pop the node off the stock, if its less than the prev its false, then work way down right
        node = stack.pop()
        if prev and node.data <= prev.data:
            return False
        prev = node
        node = node.right
    return True
