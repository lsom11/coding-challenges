class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def levelOrder(root):
    # create a queue to hold nodes
    q = []
    visited = []

    # base case: no root
    if root is None:
        return
    q.append(root)

    # if there are no more items in the queue we break
    while len(q) > 0:
        node = q.pop(0)
        visited.append(node.info)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

    for node in visited:
        print(node, end=' ')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
