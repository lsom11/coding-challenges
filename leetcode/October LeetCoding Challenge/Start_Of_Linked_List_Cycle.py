# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            
            slow = head.next
            fast = head.next.next
        
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            
            else:
                l = 1
                temp = slow.next
                while temp!=slow:
                    temp = temp.next
                    l+=1
                
            p1 = head
            p2 = head
            for i in range(l):
                p2 = p2.next
                
            while p1!=p2:
                p1 = p1.next
                p2 = p2.next
            
            return p1
                
                
        except:
            return None # No Cycle
