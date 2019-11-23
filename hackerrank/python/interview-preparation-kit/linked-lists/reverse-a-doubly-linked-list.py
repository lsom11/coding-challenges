def reverse(head):
    temp = None
    current = head
    while current is not None:
        # create a temp, store prev,
        temp = current.prev
        # set prev to next
        current.prev = current.next
        # set next to temp
        current.next = temp
        # change current to the previous
        current = current.prev

    # FINAL IMPORTANT STEP - change head to final value and return it to complete the order
    if temp is not None:
        head = temp.prev

    return head
