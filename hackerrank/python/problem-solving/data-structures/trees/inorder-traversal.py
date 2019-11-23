def inOrder(root):
    inorder_list = []
    # VISIT LEFT THEN NODE THEN RIGHT

    def traverse(node):
        if node.left is not None:
            traverse(node.left)
        inorder_list.append(node.info)
        if node.right is not None:
            traverse(node.right)

    traverse(root)
    for num in inorder_list:
        print(num, end=' ')
