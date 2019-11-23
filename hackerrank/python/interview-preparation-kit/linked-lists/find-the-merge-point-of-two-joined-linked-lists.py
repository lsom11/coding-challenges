def findMergeNode(head1, head2):
    # set temp vars, lengths
    p1 = head1
    p2 = head2
    len1 = len2 = 0
    # if still items in p1, we increment the length and set to length next
    while p1:
        len1 += 1
        p1 = p1.next
    while p2:
        len2 += 1
        p2 = p2.next
    # if p1 is bigger than p2 we set the head1 to its next var
    if len1 > len2:
        for i in range(len1 - len2):
            head1 = head1.next
    else:
        for i in range(len2 - len1):
            head2 = head2.next
    # while the heads are not null, we look for the same value, if so return if not keep going
    while head1 and head2:
        if head1 == head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next
