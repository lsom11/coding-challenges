class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = root

    def breadth_first_traversal(self):
        queue = []
        data = []
        current = self.root

        queue.append(current)

        while(len(queue)):
            node = queue.pop(0)
            data.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return data

    # left node right

    def in_order_traversal(self):
        def traverse(current):
            if current is not None:
                traverse(current.left)
                print(current)
                traverse(current.right)

        traverse(self.root)

    # node left right
    def pre_order_traversal(self):
        def traverse(current):
            if current is not None:
                print(current)
                traverse(current.left)
                traverse(current.right)

        traverse(self.root)

    # left right node
    def post_order_traversal(self):
        def traverse(current):
            if current is not None:
                traverse(current.left)
                traverse(current.right)
                print(current)

        traverse(self.root)
