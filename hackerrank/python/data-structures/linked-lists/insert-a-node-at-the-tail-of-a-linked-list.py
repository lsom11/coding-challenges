def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)

    if not head: 
        head = node
        return head
    current = head

    while current.next is not None:
        current = current.next
    current.next = node
    return head