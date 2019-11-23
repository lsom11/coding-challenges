def preOrder(root):
    preorder_list = []
    # VISIT NODE THEN LEFT THEN RIGHT

    def traverse(node):
        preorder_list.append(node.info)
        if node.left is not None:
            traverse(node.left)
        if node.right is not None:
            traverse(node.right)
    traverse(root)
    for num in preorder_list:
        print(num, end=' ')
