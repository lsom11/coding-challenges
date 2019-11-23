def removeDuplicates(self, head):
        temp = head
        s = set()
        s.add(temp.data)
        current = temp.next
        while current:
            if current.data in s:
                temp.next = current.next
            else:
                s.add(current.data)
                temp = current
            current = current.next
        return head
