# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddHead, evenHead = ListNode(val=None), ListNode(val=None)
        counter, cur, oddEvenCurs = 1, head, [evenHead, oddHead]
        while cur:
            parity = counter & 1
            oddEvenCurs[parity].next = cur
            cur = cur.next
            oddEvenCurs[parity], oddEvenCurs[parity].next  = oddEvenCurs[parity].next, None
            counter += 1
        oddEvenCurs[1].next = evenHead.next
        return oddHead.next 