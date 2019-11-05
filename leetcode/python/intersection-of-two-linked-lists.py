# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        
        currentA = headA
        currentB = headB
        
        while currentA is not currentB:
            if currentA is None:
                currentA = headB
            else: currentA = currentA.next
                
            if currentB is None:
                currentB = headA
            else: currentB = currentB.next    
        
        return currentA