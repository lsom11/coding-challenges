class Solution(object):
    def middleNode(self, head):
        aptr = 0
        bptr = 0
        r = head
        curr = head
        while curr:
            curr = curr.next
            aptr += 1
            mid = aptr // 2
            while bptr < mid:
                r = r.next
                bptr += 1
        return r