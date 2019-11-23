def reversePrint(head):
    if not head:
        return
    if head.next is not None:
        reversePrint(head.next)
    print(head.data)
